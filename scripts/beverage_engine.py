#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tea & Coffee Master CLI Engine (scripts/beverage_engine.py)
Provides programmatic tools for AI agents:
1. search      - Filter commercial beverage recipes by category, keyword, or max BOM cost.
2. scale       - Scale any drink by cup size (500ml / 700ml / hot) and batch cups (1 to 200 cups).
3. cost-sim    - Calculate BOM cost, offline retail pricing, and Meituan/Eleme delivery pricing.
4. render-html - Render a standalone interactive HTML Barista SOP & Profit Simulator Portal.
"""

import argparse
import json
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = SKILL_ROOT / "data" / "beverages_db.json"


def load_db():
    if not DB_PATH.exists():
        gen_script = SKILL_ROOT / "data" / "generate_beverage_db.py"
        if gen_script.exists():
            import subprocess
            subprocess.run([sys.executable, str(gen_script)], check=True)
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def cmd_search(args):
    db = load_db()
    results = []
    for b in db["beverages"]:
        if args.category and args.category != "all" and b["category"] != args.category:
            continue
        if args.max_cost and b["bom_cost_cny"]["total_cost"] > args.max_cost:
            continue
        if args.keyword:
            kw = args.keyword.lower()
            if kw not in json.dumps(b, ensure_ascii=False).lower():
                continue
        results.append({
            "id": b["id"],
            "name": b["name"],
            "category": b["category"],
            "positioning": b["positioning"],
            "base_size_ml": b["base_size_ml"],
            "total_bom_cost_cny": b["bom_cost_cny"]["total_cost"],
            "suggested_retail_cny": b["bom_cost_cny"]["suggested_retail"],
            "gross_margin_pct": b["bom_cost_cny"]["gross_margin_pct"]
        })
    write_output({"total_matched": len(results), "results": results}, args.output)


def cmd_scale(args):
    db = load_db()
    target = None
    for b in db["beverages"]:
        if b["id"] == args.id or args.id in b["name"]:
            target = b
            break
    if not target:
        print(f"Error: Beverage '{args.id}' not found.", file=sys.stderr)
        sys.exit(1)

    size_factor = 1.0
    if args.cup_size == "700" and target["base_size_ml"] == 500:
        size_factor = 1.38
    elif args.cup_size == "500" and target["base_size_ml"] == 700:
        size_factor = 0.72

    total_multiplier = size_factor * args.cups
    scaled = json.loads(json.dumps(target))
    scaled["requested_cup_size"] = args.cup_size
    scaled["requested_batch_cups"] = args.cups
    for ing in scaled["ingredients_500ml_iced"]:
        ing["scaled_amount"] = round(ing["amount"] * total_multiplier, 1)
        ing["scaled_cost_cny"] = round(ing["cost"] * total_multiplier, 2)

    unit_cost = round(target["bom_cost_cny"]["total_cost"] * size_factor, 2)
    unit_price = round(target["bom_cost_cny"]["suggested_retail"] * (1.2 if size_factor > 1.1 else 1.0), 1)
    scaled["batch_economics"] = {
        "unit_cost_cny": unit_cost,
        "unit_retail_cny": unit_price,
        "total_batch_cost_cny": round(unit_cost * args.cups, 2),
        "total_batch_revenue_cny": round(unit_price * args.cups, 2),
        "total_batch_gross_profit_cny": round((unit_price - unit_cost) * args.cups, 2)
    }
    write_output(scaled, args.output)


def cmd_cost_sim(args):
    total_hard_cost = round(args.raw_cost + args.pkg_cost, 2)
    margin_ratio = args.target_margin / 100.0
    offline_price = round(total_hard_cost / (1.0 - margin_ratio), 1)
    offline_profit = round(offline_price - total_hard_cost, 2)

    # Delivery platform formula: (Price - Coupon) * (1 - Commission) - DeliverySubsidy = OfflinePrice
    comm = args.platform_fee / 100.0
    net_needed = total_hard_cost + offline_profit
    delivery_listed_price = round((net_needed + args.delivery_subsidy) / (1.0 - comm) + args.coupon_subsidy, 1)

    res = {
        "cost_breakdown": {
            "raw_material_cost_cny": args.raw_cost,
            "packaging_cost_cny": args.pkg_cost,
            "total_hard_cost_cny": total_hard_cost
        },
        "offline_pricing": {
            "target_gross_margin_pct": args.target_margin,
            "suggested_offline_price_cny": offline_price,
            "gross_profit_per_cup_cny": offline_profit
        },
        "delivery_platform_pricing": {
            "platform_commission_pct": args.platform_fee,
            "coupon_discount_per_cup_cny": args.coupon_subsidy,
            "merchant_delivery_subsidy_cny": args.delivery_subsidy,
            "suggested_listed_price_cny": delivery_listed_price,
            "actual_customer_paid_cny": round(delivery_listed_price - args.coupon_subsidy, 1),
            "merchant_net_profit_per_cup_cny": offline_profit
        },
        "daily_profit_projection": {
            "50_cups_daily_profit_cny": round(offline_profit * 50, 1),
            "100_cups_daily_profit_cny": round(offline_profit * 100, 1),
            "monthly_100_cups_profit_cny": round(offline_profit * 100 * 30, 1)
        }
    }
    write_output(res, args.output)


def cmd_render_html(args):
    db = load_db()
    beverages_json = json.dumps(db["beverages"], ensure_ascii=False)
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{args.title} - Tea & Coffee Master 商用SOP与毛利精算系统</title>
<style>
  :root {{
    --bg: #0c1322; --card: #162032; --border: #2a3950; --text: #f1f5f9;
    --muted: #94a3b8; --gold: #f59e0b; --emerald: #10b981; --cyan: #06b6d4;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; padding-bottom: 60px; }}
  header {{ background: linear-gradient(135deg, #162032 0%, #0c1322 100%); border-bottom: 1px solid var(--border); padding: 28px 20px; text-align: center; }}
  header h1 {{ color: var(--gold); font-size: 26px; margin-bottom: 6px; }}
  header p {{ color: var(--muted); font-size: 14px; }}
  .container {{ max-width: 1240px; margin: 24px auto; padding: 0 20px; }}
  .sim-panel {{ background: linear-gradient(135deg, rgba(16,185,129,0.12), rgba(245,158,11,0.08)); border: 1px solid var(--emerald); border-radius: 12px; padding: 20px; margin-bottom: 24px; }}
  .sim-panel h2 {{ font-size: 18px; color: var(--emerald); margin-bottom: 12px; }}
  .sim-inputs {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin-bottom: 14px; }}
  .sim-inputs input {{ width: 100%; padding: 7px 10px; background: #0c1322; color: #fff; border: 1px solid var(--border); border-radius: 6px; }}
  .sim-out {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; }}
  .stat-box {{ background: rgba(12,19,34,0.85); padding: 12px 16px; border-radius: 8px; border: 1px solid var(--border); }}
  .stat-box .big {{ font-size: 21px; font-weight: 700; color: var(--gold); }}
  .toolbar {{ display: flex; flex-wrap: wrap; gap: 12px; justify-content: space-between; align-items: center; background: var(--card); padding: 16px 20px; border-radius: 12px; border: 1px solid var(--border); margin-bottom: 24px; }}
  .tabs {{ display: flex; flex-wrap: wrap; gap: 8px; }}
  .tab-btn {{ background: #0c1322; color: var(--muted); border: 1px solid var(--border); padding: 8px 14px; border-radius: 8px; cursor: pointer; font-weight: 600; font-size: 13px; }}
  .tab-btn.active, .tab-btn:hover {{ background: var(--gold); color: #0c1322; border-color: var(--gold); }}
  .controls {{ display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }}
  .controls select, .controls input {{ background: #0c1322; color: #fff; border: 1px solid var(--border); padding: 7px 10px; border-radius: 8px; font-size: 13px; }}
  .btn-print {{ background: var(--emerald); color: #0c1322; border: none; padding: 8px 16px; border-radius: 8px; font-weight: 700; cursor: pointer; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(370px, 1fr)); gap: 20px; }}
  .card {{ background: var(--card); border: 1px solid var(--border); border-radius: 14px; padding: 20px; display: flex; flex-direction: column; gap: 12px; }}
  .card-title {{ font-size: 18px; font-weight: 700; color: #fff; }}
  .econ-bar {{ display: flex; justify-content: space-between; background: #0c1322; padding: 8px 12px; border-radius: 8px; font-size: 12px; border-left: 3px solid var(--emerald); }}
  .flavor {{ font-size: 12.5px; color: #fde68a; background: rgba(245,158,11,0.08); padding: 8px 10px; border-radius: 6px; }}
  .ing-table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
  .ing-table td {{ padding: 4px 0; border-bottom: 1px dashed rgba(255,255,255,0.07); }}
  .ing-val {{ text-align: right; color: var(--emerald); font-weight: 600; }}
  .steps {{ padding-left: 18px; font-size: 13px; color: #e2e8f0; display: flex; flex-direction: column; gap: 4px; }}
  .hot-note {{ font-size: 12px; color: var(--cyan); border-top: 1px solid var(--border); padding-top: 8px; }}
  @media print {{
    body {{ background: #fff; color: #000; }}
    .toolbar, .btn-print {{ display: none; }}
    .card {{ border: 1px solid #ccc; page-break-inside: avoid; background: #fff; color: #000; }}
  }}
</style>
</head>
<body>
<header>
  <h1>🧋 {args.title}</h1>
  <p>Tea & Coffee Master 吧台标准化出品 SOP、摆摊批量备料缩放与外卖防亏本精算系统</p>
</header>
<div class="container">
  <div class="sim-panel">
    <h2>💰 单杯 BOM 成本 & 美团/饿了么外卖满减防亏本精算器</h2>
    <div class="sim-inputs">
      <div><label style="font-size:12px;color:var(--muted)">液体+小料成本 (¥)</label><input type="number" id="c-raw" value="3.50" step="0.1"></div>
      <div><label style="font-size:12px;color:var(--muted)">杯+盖+吸管+袋包材 (¥)</label><input type="number" id="c-pkg" value="0.80" step="0.05"></div>
      <div><label style="font-size:12px;color:var(--muted)">目标毛利率 (%)</label><input type="number" id="c-margin" value="73" step="1"></div>
      <div><label style="font-size:12px;color:var(--muted)">外卖平台扣点 (%)</label><input type="number" id="c-comm" value="20" step="1"></div>
      <div><label style="font-size:12px;color:var(--muted)">单杯分摊满减补贴 (¥)</label><input type="number" id="c-coupon" value="5.0" step="0.5"></div>
    </div>
    <div class="sim-out" id="sim-out"></div>
  </div>

  <div class="toolbar">
    <div class="tabs">
      <button class="tab-btn active" onclick="setCat('all', this)">全部商用配方 ({len(db['beverages'])})</button>
      <button class="tab-btn" onclick="setCat('light_milk_tea', this)">🍃 霸王轻乳茶</button>
      <button class="tab-btn" onclick="setCat('classic_milk_tea', this)">🧋 厚乳与雪顶</button>
      <button class="tab-btn" onclick="setCat('lemon_fruit_tea', this)">🍋 暴打柠檬/果茶</button>
      <button class="tab-btn" onclick="setCat('specialty_coffee', this)">☕ 爆款特调果咖</button>
      <button class="tab-btn" onclick="setCat('base_topping', this)">🫖 茶底批量萃取</button>
    </div>
    <div class="controls">
      <select id="cup-size" onchange="render()">
        <option value="1">标准中杯 (500ml)</option>
        <option value="1.38">霸气大桶杯 (700ml x1.38)</option>
      </select>
      <label style="font-size:13px;color:var(--gold);font-weight:700">出杯/备料杯数: <span id="cups-lbl">1</span> 杯</label>
      <input type="range" id="cups-slider" min="1" max="100" value="1" oninput="document.getElementById('cups-lbl').innerText=this.value; render()">
      <button class="btn-print" onclick="window.print()">🖨️ 打印吧台贴墙 SOP 卡</button>
    </div>
  </div>

  <div class="grid" id="bev-grid"></div>
</div>

<script>
const BEVS = {beverages_json};
let curCat = 'all';

function calcSim() {{
  const raw = parseFloat(document.getElementById('c-raw').value) || 0;
  const pkg = parseFloat(document.getElementById('c-pkg').value) || 0;
  const margin = (parseFloat(document.getElementById('c-margin').value) || 70) / 100;
  const comm = (parseFloat(document.getElementById('c-comm').value) || 20) / 100;
  const coupon = parseFloat(document.getElementById('c-coupon').value) || 0;
  const hard = raw + pkg;
  const offlinePrice = (hard / (1 - margin)).toFixed(1);
  const profit = (offlinePrice - hard).toFixed(2);
  const deliveryListed = ((parseFloat(offlinePrice) + 2.0) / (1 - comm) + coupon).toFixed(1);
  document.getElementById('sim-out').innerHTML = `
    <div class="stat-box"><div>单杯总硬成本 (BOM+包材)</div><div class="big">¥ ${{hard.toFixed(2)}}</div><div style="font-size:12px;color:var(--muted)">原料 ¥${{raw.toFixed(2)}} + 包材 ¥${{pkg.toFixed(2)}}</div></div>
    <div class="stat-box"><div>线下堂食 / 夜市摆摊定价</div><div class="big">¥ ${{offlinePrice}}</div><div style="font-size:12px;color:var(--emerald)">单杯净赚毛利: ¥${{profit}}</div></div>
    <div class="stat-box"><div>美团/饿了么防亏挂牌价</div><div class="big">¥ ${{deliveryListed}}</div><div style="font-size:12px;color:var(--muted)">扣完20%佣金与满减后仍净赚 ¥${{profit}}</div></div>
    <div class="stat-box"><div>日销 80 杯月度毛利预测</div><div class="big">¥ ${{Math.round(profit * 80 * 30).toLocaleString()}} /月</div><div style="font-size:12px;color:var(--muted)">单日毛利 ¥${{Math.round(profit * 80)}}</div></div>
  `;
}}
['c-raw','c-pkg','c-margin','c-comm','c-coupon'].forEach(id => document.getElementById(id).addEventListener('input', calcSim));
calcSim();

function setCat(c, btn) {{
  curCat = c;
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  render();
}}

function render() {{
  const sizeMult = parseFloat(document.getElementById('cup-size').value) || 1;
  const cups = parseInt(document.getElementById('cups-slider').value) || 1;
  const mult = sizeMult * cups;
  const filtered = BEVS.filter(b => curCat === 'all' || b.category === curCat);
  document.getElementById('bev-grid').innerHTML = filtered.map(b => {{
    const rows = b.ingredients_500ml_iced.map(i => `<tr><td>${{i.item}}</td><td class="ing-val">${{Math.round(i.amount * mult * 10)/10}} ${{i.unit}}</td></tr>`).join('');
    const steps = b.sop_steps.map(s => `<li>${{s}}</li>`).join('');
    const totalCost = (b.bom_cost_cny.total_cost * mult).toFixed(2);
    const totalRev = (b.bom_cost_cny.suggested_retail * cups * (sizeMult > 1.1 ? 1.2 : 1)).toFixed(1);
    return `
      <div class="card">
        <div>
          <div class="card-title">${{b.name}}</div>
          <div style="font-size:12px;color:var(--gold)">🎯 定位：${{b.positioning}}</div>
        </div>
        <div class="econ-bar">
          <span>💰 ${{cups}}杯总成本: <b style="color:#fff">¥${{totalCost}}</b></span>
          <span>🏷️ 建议总营收: <b style="color:var(--gold)">¥${{totalRev}}</b></span>
          <span>📈 毛利率: <b style="color:var(--emerald)">${{b.bom_cost_cny.gross_margin_pct}}%</b></span>
        </div>
        <div class="flavor">✨ <b>感官风味卡：</b>${{b.flavor_profile}}</div>
        <table class="ing-table">${{rows}}</table>
        <ol class="steps">${{steps}}</ol>
        <div class="hot-note">🔥 <b>热饮转换 (400ml)：</b>${{b.hot_400ml_adjustment}}</div>
      </div>
    `;
  }}).join('');
}}
render();
</script>
</body>
</html>"""
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully rendered interactive HTML Barista SOP Portal: {out_path.resolve()}")


def write_output(data, output_path):
    text = json.dumps(data, ensure_ascii=False, indent=2)
    if output_path:
        p = Path(output_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Successfully wrote result to {p.resolve()}")
    else:
        print(text)


def main():
    parser = argparse.ArgumentParser(description="Tea & Coffee Master Commercial CLI Engine")
    sub = parser.add_subparsers(dest="command", required=True)

    p_search = sub.add_parser("search", help="Search beverage recipes")
    p_search.add_argument("--category", default="all")
    p_search.add_argument("--keyword", default=None)
    p_search.add_argument("--max-cost", type=float, default=None)
    p_search.add_argument("--output", default=None)
    p_search.set_defaults(func=cmd_search)

    p_scale = sub.add_parser("scale", help="Scale a beverage recipe by cup size and batch count")
    p_scale.add_argument("--id", required=True, help="Beverage ID (e.g. tea_01, cof_01) or name")
    p_scale.add_argument("--cup-size", choices=["500", "700"], default="500")
    p_scale.add_argument("--cups", type=int, default=1, help="Number of cups for batch prep")
    p_scale.add_argument("--output", default=None)
    p_scale.set_defaults(func=cmd_scale)

    p_cost = sub.add_parser("cost-sim", help="Calculate BOM cost, offline retail price, and delivery platform price")
    p_cost.add_argument("--raw-cost", type=float, required=True, help="Raw liquid + topping cost in CNY")
    p_cost.add_argument("--pkg-cost", type=float, default=0.80, help="Cup + lid + straw + bag cost in CNY")
    p_cost.add_argument("--target-margin", type=float, default=73.0, help="Target gross margin percentage")
    p_cost.add_argument("--platform-fee", type=float, default=20.0, help="Meituan/Eleme commission percentage")
    p_cost.add_argument("--coupon-subsidy", type=float, default=5.0, help="Coupon subsidy per cup in CNY")
    p_cost.add_argument("--delivery-subsidy", type=float, default=2.0, help="Merchant delivery fee subsidy in CNY")
    p_cost.add_argument("--output", default=None)
    p_cost.set_defaults(func=cmd_cost_sim)

    p_html = sub.add_parser("render-html", help="Render standalone interactive HTML Barista SOP & Cost Portal")
    p_html.add_argument("--title", default="饮品大师：商用奶茶·鲜果茶·特调咖啡吧台出品与毛利精算系统")
    p_html.add_argument("--output", required=True)
    p_html.set_defaults(func=cmd_render_html)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
