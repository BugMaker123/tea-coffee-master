# 🧋☕ Tea & Coffee Master Pro v3.0 — 商用茶饮与精品咖啡研发 Agent Skill（动态联网拆解 · BOM组装 · 降本极速优化闭环）

[![Agent Skill](https://img.shields.io/badge/Agent_Skill-v3.0_Dynamic_Loop-purple.svg)](https://github.com/BugMaker123/tea-coffee-master)
[![Formulas](https://img.shields.io/badge/Commercial_Formulas-25%2B_Auto--Growing-green.svg)](./data/beverages_db.json)
[![Live Fetch](https://img.shields.io/badge/Live_Teardown-Toutiao%20%7C%20Wikipedia-blue.svg)](./scripts/beverage_engine.py)

**`tea-coffee-master` v3.0** 是一套专为 **WorkBuddy、Gemini CLI / Antigravity、OpenAI Codex、Claude Code** 打造的**工业级动态茶饮与咖啡研发顾问技能包**。

不同于静态文档型 Skill，**v3.0 核心构建了「全网实时拆解连锁新品 -> 500ml/700ml 商用克重与 BOM 成本组装 -> 供应链降本/低卡/摆摊极速优化 -> 数据库自进化沉淀 -> 交互式吧台 SOP 交付」的完整商业闭环**：
- 🌐 **实时联网拆解当季新品 (`live-fetch`)**：无论霸王茶姬、喜茶、古茗、瑞幸刚推出什么当季新品（如“霸王茶姬 晴山栖谷”），CLI 引擎可直接联网抓取全网同行拆解帖，自动识别核心茶底（如皖西黄大茶、玄米）、乳基底与配比。
- 💰 **模糊配料自动清洗与商用 BOM 组装 (`assemble`)**：自动将网上的 `"牛奶半杯、果糖两泵、冰块适量"` 转化为精准 500ml 商用 `ml`/`g`，并基于内置 **35 种茶饮原料成本矩阵** 自动算出单杯原料成本、包材成本、建议零售价与毛利率（%）。
- 🚀 **三维商业目标优化 (`optimize`)**：支持一键对任意饮品执行 **`profit-boost`（高毛利供应链同厂平替降本，单杯降本 25%-32%）**、**`low-calorie`（0卡代糖与脱脂冷打发奶沫改造）** 与 **`stall-speed`（夜市摆摊 5L 保温桶预调母液动线重构，12 秒极速出杯）**。
- 💾 **配方库自进化 (`--save-to-db`)**：每次联网拆解或优化的新饮品可自动写回 `data/beverages_db.json` 并一键重新渲染交互式吧台 SOP 网页系统，越用越值钱！

---

## 📦 仓库完整目录结构

```text
tea-coffee-master/
├── SKILL.md                                     # Agent 核心触发指令与五步动态商业闭环规范
├── README.md                                    # 多智能体安装指南与 v3.0 动态引擎说明
├── scripts/
│   ├── beverage_engine.py                       # 【核心引擎 v3.0】8大子命令：auto-pipeline / live-fetch / assemble / optimize / margin / scale / search / render-html
│   └── generate_beverage_db.py                  # 结构化饮品数据库初始化构建器
├── data/
│   └── beverages_db.json                        # 结构化爆品配方数据库（内置25+款基准爆品，支持联网自动扩充）
├── references/                                  # 5大商用模块深度SOP参考手册
│   ├── 01_base_preparation_sop.md               # 七大茶底冲泡参数、急速冰镇锁香、糖浆/珍珠/奶盖/冻类熬制SOP
│   ├── 02_milk_and_fruit_tea_formulas.md        # 原叶轻乳茶、爆款水果茶、暴打柠檬茶、手作芋泥麻薯精准配方库
│   ├── 03_coffee_and_specialty_formulas.md      # 意式浓缩校准、经典奶咖与果咖特调（生椰/橙C/话梅/Dirty）配方库
│   ├── 04_cost_margin_and_equipment.md          # 摆摊vs开店设备清单、BOM成本核算与美团/饿了么防亏本定价模型
│   └── 05_workbuddy_monetization_playbook.md    # WorkBuddy/小红书/咸鱼商业变现全案（定价阶梯、引流文案、交付物规范）
└── examples/
    ├── beverage_interactive_portal.html         # 【可直接交付客户】独立离线交互式吧台SOP、批量备料与外卖毛利精算系统
    └── auto_pipeline_drink_demo.json            # v3.0 一键联网拆解「霸王茶姬 晴山栖谷」->BOM组装->高毛利平替实测输出
```

---

## ⚡ CLI 引擎 8 大子命令快速实战 (`scripts/beverage_engine.py`)

零第三方依赖（基于 Python 3 标准库），开箱即用：

```bash
# 1. 【王牌功能】一键全自动闭环：联网拆解连锁新品 -> 提取茶底乳品组装BOM -> 供应链降本优化 -> 写入数据库
python scripts/beverage_engine.py auto-pipeline \
  --query "霸王茶姬 晴山栖谷" \
  --category light_milk_tea \
  --optimize-mode profit-boost \
  --save-to-db \
  --output examples/auto_pipeline_drink_demo.json

# 2. 独立联网搜索全网连锁新品配方拆解 (Toutiao SSR + Wikipedia ZH)
python scripts/beverage_engine.py live-fetch --query "喜茶 三倍厚抹"

# 3. 模糊饮品配料 -> 500ml 商用精准克重(ml/g) + BOM成本与毛利率组装器
python scripts/beverage_engine.py assemble \
  --name "桂花酒酿冰美式" \
  --category specialty_coffee \
  --flavor "清甜桂花酒酿碰撞中深烘意式浓缩" \
  --ingredients "孝感米酒酿 60g, 桂花糖浆两泵, 纯净水 150ml, 机制方冰 150g, 意式浓缩两份" \
  --save-to-db

# 4. 三维商业目标优化 (支持 profit-boost | low-calorie | stall-speed)
python scripts/beverage_engine.py optimize --id "生椰拿铁" --mode profit-boost --save-to-db
python scripts/beverage_engine.py optimize --id "伯牙绝弦" --mode stall-speed --save-to-db

# 5. 门店与外卖平台（美团/饿了么扣点）防亏本净利与回本周期精算
python scripts/beverage_engine.py margin --id "伯牙绝弦" --price 15.0 --platform-fee 0.22 --daily-cups 150 --monthly-rent 6000 --monthly-labor 8000

# 6. 早班备料与夜市摆摊批量缩放 (如放大至 80 杯 700ml 大杯)
python scripts/beverage_engine.py scale --id "手打渣男暴打柠檬茶" --cups 80 --size-ml 700

# 7. 检索饮品配方数据库
python scripts/beverage_engine.py search --category fruit_tea --keyword "柠檬"

# 8. 重新渲染客户级交互式吧台 SOP 与外卖防亏本精算门户
python scripts/beverage_engine.py render-html --output examples/beverage_interactive_portal.html
```

---

## 🛠️ 在各大智能体中安装使用

### 1. Gemini CLI / Antigravity
```bash
git clone https://github.com/BugMaker123/tea-coffee-master.git ~/.gemini/config/skills/tea-coffee-master
```
*(Windows PowerShell)*:
```powershell
git clone https://github.com/BugMaker123/tea-coffee-master.git "$HOME\.gemini\config\skills\tea-coffee-master"
```

### 2. OpenAI Codex CLI / Claude Code
```bash
git clone https://github.com/BugMaker123/tea-coffee-master.git ~/.codex/skills/tea-coffee-master
```

### 3. WorkBuddy
将本仓库导入 WorkBuddy 技能库，将 `SKILL.md` 设为系统指令，并挂载 `scripts/`、`data/` 与 `references/`，即可接单交付 **连锁新品1:1商用复刻、夜市摆摊极速菜单定制、外卖防亏本成本核算表与交互式吧台 SOP 系统**。
