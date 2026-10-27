---
name: tea-coffee-master
description: "商用与专业级奶茶、果茶、咖啡研发与制作大师 v2.0。内置可执行CLI精算与批量缩放引擎(scripts/beverage_engine.py)、24+爆款连锁结构化配方库(data/beverages_db.json)与交互式吧台SOP/外卖防亏本精算HTML生成器。全面赋能饮品店创业、夜市摆摊及WorkBuddy付费咨询变现。"
---

# 饮品大师：商用配方缩放引擎 + BOM毛利精算器 + 吧台交互式SOP系统 (Tea & Coffee Master v2.0)

本 Skill 是集**可执行 CLI 精算脚本 (`scripts/`) + 24款主流连锁爆品结构化数据库 (`data/`) + 离线可打印吧台 SOP 网页系统 (`examples/`) + 5大商用开店百科 (`references/`)**于一体的工业级智能体技能。

当前 `SKILL.md` 所在目录记为 `<skill-root>`。

---

## 一、 核心可执行工具链 (Executable CLI Engine)

当用户需要查询饮品配方、将单杯配方放大为 700ml 大桶杯或夜市摆摊 50~100 杯批量备料、测算单杯 BOM 成本与美团/饿了么外卖防亏本满减定价、或导出可贴墙打印的吧台 SOP 卡时，**优先调用内置 CLI 引擎**：

### 1. 检索结构化商用饮品库 (`search`)
支持按分类（`light_milk_tea` 轻乳茶 / `classic_milk_tea` 厚乳雪顶 / `lemon_fruit_tea` 暴打柠檬与果茶 / `specialty_coffee` 特调果咖乳咖 / `base_topping` 茶底批量萃取与小料）、关键词或最高 BOM 成本检索：
```bash
python <skill-root>/scripts/beverage_engine.py search --category all --keyword "椰"
python <skill-root>/scripts/beverage_engine.py search --category lemon_fruit_tea --max-cost 3.5
```

### 2. 单杯规格转换与摆摊批量备料缩放 (`scale`)
支持一键切换 `500` (500ml中杯) 与 `700` (700ml大桶杯)，并支持按 `--cups N`（如出摊备料 50 杯）自动换算所有茶底、鲜奶、果糖克重以及整批总成本、总营收与总毛利：
```bash
python <skill-root>/scripts/beverage_engine.py scale --id tea_05 --cup-size 700 --cups 50
python <skill-root>/scripts/beverage_engine.py scale --id cof_01 --cup-size 500 --cups 20 --output batch_coconut_latte.json
```

### 3. 单杯 BOM 成本与美团/饿了么外卖防亏本定价模拟器 (`cost-sim`)
输入液体小料成本、包材成本、目标毛利率（默认73%）、外卖平台扣点（20%）及满减分摊金额，自动反推堂食定价、外卖防亏挂牌价与月度毛利预测：
```bash
python <skill-root>/scripts/beverage_engine.py cost-sim --raw-cost 3.55 --pkg-cost 0.80 --target-margin 73 --platform-fee 20 --coupon-subsidy 5.0
```

### 4. 一键渲染交互式吧台 SOP 卡与毛利精算 Web 系统 (`render-html`)
生成可离线在浏览器打开、内置外卖防亏计算器、500ml/700ml 规格切换、1~100 杯备料滑块与**一键打印贴墙吧台 SOP 卡 (PDF)** 的独立前端系统：
```bash
python <skill-root>/scripts/beverage_engine.py render-html --title "2026夏季爆单饮品吧台标准出品SOP" --output ./barista_sop_portal.html
```
- 预渲染演示成品：[`examples/beverage_interactive_portal.html`](./examples/beverage_interactive_portal.html)

---

## 二、 技能目录架构

```text
<skill-root>/
├── SKILL.md                               # 核心指令与 CLI 调度规范
├── scripts/
│   └── beverage_engine.py                 # 多子命令 CLI 引擎 (search / scale / cost-sim / render-html)
├── data/
│   ├── beverages_db.json                  # 24 款连锁爆品结构化商用数据库 (含BOM成本/糖度梯度/冷热转换)
│   ├── generate_beverage_db.py            # 基础数据库生成脚本
│   └── append_beverages.py                # 扩展爆款数据库脚本
├── examples/
│   ├── beverage_interactive_portal.html   # 可直接浏览器打开的吧台交互式SOP与毛利精算系统
│   └── sample_cost_simulation.json        # 外卖防亏定价测算JSON样例
└── references/                            # 5 大商用开店深层手册
    ├── tea_recipes_sop.md                 # 4大商用茶汤工业萃取参数、轻乳茶、柠檬茶与黑糖珍珠奶盖SOP
    ├── coffee_recipes_sop.md              # 9Bar意式浓缩校磨纠偏、生椰拿铁、冰博克Dirty与批量冷萃SOP
    ├── cost_calculator.md                 # 单杯BOM拆解表、73%毛利定价公式与外卖20%扣点满减倒推模型
    ├── equipment_and_supply.md            # 3000元摆摊/2.5万档口设备清单与菲诺/Oatly/塞尚大牌同厂平替
    └── marketing_and_menu.md              # 2-5-2-1金字塔菜单架构、外卖高转化命名法与私域复购裂变
```
