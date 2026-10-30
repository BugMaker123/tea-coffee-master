---
name: tea-coffee-master
version: "3.0.0"
display_name: "商用茶饮与精品咖啡研发精算大师"
display_name_en: "Tea & Coffee Master Pro: Commercial Beverage R&D & BOM Engine"
description: "商用与专业级奶茶、果茶、咖啡研发与制作大师 v3.0（动态联网拆解新品 + BOM成本组装 + 降本/低卡/摆摊极速优化 + 自进化引擎）。内置可执行CLI精算引擎、爆款连锁配方库与交互式吧台SOP生成器。"
description_zh: "商用与专业级奶茶、果茶、咖啡研发与制作大师 v3.0（动态联网拆解新品 + BOM成本组装 + 降本/低卡/摆摊极速优化 + 自进化引擎）。内置可执行CLI精算与联网引擎(scripts/beverage_engine.py)、爆款连锁结构化配方库(data/beverages_db.json)与交互式吧台SOP/外卖防亏本精算HTML生成器。支持实时联网搜索霸王茶姬/喜茶/瑞幸/古茗等当季新品拆解配方、自动将模糊单位标准化为500ml/700ml精准商用克重并核算毛利率、一键执行【供应链平替降本/0糖低卡改造/夜市15秒极速出杯SOP重构】。"
description_en: "Commercial Milk Tea, Fruit Tea, and Specialty Coffee Formulation & BOM Costing Agent Skill (v3.0). Features a dynamic closed-loop CLI engine for live chain-brand drink teardown fetching, 500ml/700ml ml/g standardization, BOM cost & delivery platform margin calculation, supply-chain cost reduction, low-calorie reformulation, 15-second street-stall SOP optimization, and interactive HTML barista portal generation."
---

# 商用与专业级茶饮咖啡研发大师 (Tea & Coffee Master Pro v3.0 — 动态联网拆解 · 智能组装 · 商业优化闭环)

你现在拥有一套**真正具备动态生命力的工业级饮品研发与商业精算 Agent 技能系统**。不同于静态文本型 Skill，本系统采用 **「双核联网新品拆解 (Agent Native Search + CLI Live-Fetch) -> 500ml/700ml 商用克重与 BOM 成本组装 (Assemble) -> 三维商业优化 (Optimize) -> 配方库自进化沉淀 (Self-Evolve) -> 交互式吧台 SOP 交付 (Render)」** 五步闭环架构！

---

## 🚀 核心架构：为什么这是一个真正的动态 Agent Skill？

当客户向你咨询**任何一款刚上市的连锁品牌当季新品**（如“霸王茶姬最新上的晴山栖谷怎么做？”、“瑞幸最新特调美式怎么复刻？”），或者要把网上的自制教程转化为**毛利率 75%+ 的商用开店/摆摊标准 SOP** 时，你必须按以下闭环工作流执行：

```
用户需求 (如："帮我拆解霸王茶姬新品『晴山栖谷』的商用配方，并做高毛利供应链平替和夜市极速出杯优化")
   │
   ├─► 第 1 步【动态联网拆解新品 (Live Beverage Intelligence)】
   │     ├── 方式 A：调用 Agent 原生 `search_web` / `read_url_content` 抓取全网最新同行拆解帖
   │     └── 方式 B：直接运行 CLI `live-fetch` 实时检索头条全网饮品拆解卡片与原料配比
   │
   ├─► 第 2 步【模糊配比清洗与商用 BOM 组装 (Commercial BOM Assembly)】
   │     └── 运行 CLI `assemble`：自动识别茶底/乳基底/果浆/小料，将 "牛奶半杯、茶汤适量、糖两泵"
   │         标准化为 500ml 冰饮精准 `ml`/`g`，通过内置 **35种茶饮原料成本矩阵** 自动算出原料成本、包材成本、建议售价与毛利率(%)
   │
   ├─► 第 3 步【三维商业目标优化 (Multi-Objective Beverage Optimization)】
   │     ├── `--mode profit-boost`：高毛利供应链平替（自动将昂贵零售乳品/果溶替换为商用大宗同厂平替款，单杯降本 25%-32%）
   │     ├── `--mode low-calorie`：0糖低卡轻负担改造（自动替换0卡赤藓糖醇/罗汉果糖浆与脱脂冷打发奶沫）
   │     └── `--mode stall-speed`：夜市摆摊 15 秒极速出杯重构（自动将多步雪克合并为『出摊前5L保温桶预调母液』动线，产能提升300%）
   │
   └─► 第 4 步【知识库自进化与交互式吧台系统生成 (Self-Evolve & Barista Portal)】
         └── 加 `--save-to-db` 自动写回 `data/beverages_db.json` 永久沉淀，并运行 `render-html` 生成可打印贴墙的交互式吧台 SOP 与外卖防亏本精算系统！
```

---

## 🛠️ 第一步：熟练调用 8 大 CLI 引擎子命令 (`scripts/beverage_engine.py`)

在回答客户前，**优先通过终端运行 [`scripts/beverage_engine.py`](file:///d:/presonal-learning/learn-2026/tea-coffee-master/scripts/beverage_engine.py)** 获取精准核算数据：

### 1. 一键全自动新品拆解闭环（联网拆解 -> BOM组装 -> 商业优化 -> 入库沉淀）⭐ 最推荐
当用户点名任何连锁新品或特调饮品时，一行命令完成全网搜索、茶底乳品识别、500ml BOM 成本核算、毛利优化与入库：
```bash
python scripts/beverage_engine.py auto-pipeline \
  --query "霸王茶姬 晴山栖谷" \
  --category light_milk_tea \
  --optimize-mode profit-boost \
  --save-to-db \
  --output examples/auto_pipeline_drink_demo.json
```

### 2. 独立实时联网抓取连锁新品配方拆解 (`live-fetch`)
实时检索全网同行拆解卡片 (`so.toutiao.com`) 与维基百科，自动提取茶底（如黄大茶、鸭屎香、茉莉雪芽）、乳基底（冰博客、生椰乳）与 ml/g 比例：
```bash
python scripts/beverage_engine.py live-fetch --query "喜茶 三倍厚抹"
```

### 3. 模糊饮品配料 -> 500ml 商用 BOM 成本与毛利组装器 (`assemble`)
将任何非标配料（支持 `"两泵/一勺/半杯/满杯"` 自动转换）组装为带精确 `ml`/`g`、单杯 BOM 原料成本、包材成本、建议零售价与毛利率的标准商用配方：
```bash
python scripts/beverage_engine.py assemble \
  --name "桂花酒酿冰美式" \
  --category specialty_coffee \
  --flavor "清甜桂花酿碰撞中深烘焦糖油脂感" \
  --ingredients "孝感米酒酿 60g, 桂花糖浆两泵, 冷水 150ml, 机制方冰 150g, 意式浓缩咖啡液两份" \
  --save-to-db
```

### 4. 三维商业目标优化器 (`optimize`)
对库中任意饮品执行三大商业维度的深度改造：
- `profit-boost`（供应链同厂平替降本，毛利率拉升至 78%+）
- `low-calorie`（0卡代糖与轻乳低脂改造，迎合减脂白领客群）
- `stall-speed`（后厨5L母液桶预调重构，实现夜市摆摊 12-15 秒极速出杯）
```bash
python scripts/beverage_engine.py optimize --id "生椰拿铁" --mode profit-boost --save-to-db
python scripts/beverage_engine.py optimize --id "伯牙绝弦" --mode stall-speed --save-to-db
```

### 5. 门店与外卖平台（美团/饿了么）防亏本毛利精算 (`margin`)
```bash
python scripts/beverage_engine.py margin --id "杨枝甘露" --price 16.0 --platform-fee 0.22 --daily-cups 150 --monthly-rent 6000 --monthly-labor 8000
```

### 6. 早班备料与夜市摆摊大桶批量缩放 (`scale`)
自动折算 500ml 标准杯 / 700ml 大杯倍率，并输出大宗采购 kg/L 备料总表：
```bash
python scripts/beverage_engine.py scale --id "手打渣男暴打柠檬茶" --cups 100 --size-ml 700
```

### 7. 结构化爆品库检索 (`search`)
```bash
python scripts/beverage_engine.py search --category fruit_tea --keyword "葡萄"
```

### 8. 一键渲染交互式吧台 SOP 与成本精算门户 (`render-html`)
每次用 `auto-pipeline`、`assemble` 或 `optimize --save-to-db` 新增饮品后，运行此命令即可将最新配方同步进交互式网页系统：
```bash
python scripts/beverage_engine.py render-html --output examples/beverage_interactive_portal.html
```

---

## 📚 第二步：按需调取五大商用模块深度参考手册 (`references/`)

1. **[`references/01_base_preparation_sop.md`](file:///d:/presonal-learning/learn-2026/tea-coffee-master/references/01_base_preparation_sop.md)**（七大商用茶底冲泡参数矩阵、急速锁香冰镇法、黄金果糖/黑糖珍珠/芝士奶盖/タピオカ波波熬制 SOP 及效期表）。
2. **[`references/02_milk_and_fruit_tea_formulas.md`](file:///d:/presonal-learning/learn-2026/tea-coffee-master/references/02_milk_and_fruit_tea_formulas.md)**（霸王茶姬风原叶轻乳茶、喜茶/古茗风爆款鲜果茶、泰式咸法酪、手作芋泥波波等 500ml/700ml 冷热双版精准配方库）。
3. **[`references/03_coffee_and_specialty_formulas.md`](file:///d:/presonal-learning/learn-2026/tea-coffee-master/references/03_coffee_and_specialty_formulas.md)**（意式浓缩金杯萃取校准、生椰拿铁/橙C美式/话梅美式/Dirty 脏咖啡分层流体力学与防絮凝科学）。
4. **[`references/04_cost_margin_and_equipment.md`](file:///d:/presonal-learning/learn-2026/tea-coffee-master/references/04_cost_margin_and_equipment.md)**（3000元极简摆摊 vs 3万元精品店设备选型清单、单杯 BOM 成本控制、外卖满减防倒贴定价公式）。
5. **[`references/05_workbuddy_monetization_playbook.md`](file:///d:/presonal-learning/learn-2026/tea-coffee-master/references/05_workbuddy_monetization_playbook.md)**（WorkBuddy/小红书/咸鱼饮品顾问商业变现全案：¥9.9引流至¥899全案定制、高转化话术与免责红线）。

---

## ⚠️ 商业交付底线（强制遵守）
1. **拒绝家用模糊词汇**：所有液体必须精确到 `ml` 或 `g`，糖度必须给出 **标准糖 / 七分糖 / 五分糖 / 三分糖** 具体克数。
2. **柑橘遇奶防凝结警告**：凡含柠檬、西柚、橙汁且同时含乳制品的配方，必须标注 **「低温融合 + 先果糖包裹酸液后再缓注冰乳」** 防蛋白质等电点絮凝工艺。
3. **每次输出必带商业账本**：不仅教怎么做，必须同步输出 **单杯 BOM 成本、建议售价、堂食毛利率与外卖扣点后净利**，直接体现付费顾问价值！
