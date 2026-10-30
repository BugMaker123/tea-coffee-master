---
name: beverage-pipeline
description: "一键联网拆解连锁新品饮品、组装500ml商用BOM成本配方、执行供应链降本/低卡/摆摊极速优化"
args:
  - name: drink
    description: "饮品或连锁新品名称（如：霸王茶姬 晴山栖谷、生椰拿铁、多肉葡萄）"
    required: true
  - name: mode
    description: "商业优化模式（profit-boost 供应链降本 | low-calorie 0糖低卡 | stall-speed 夜市15秒极速出杯）"
    required: false
---

# 饮品新品拆解与商业优化命令 (`/beverage-pipeline`)

针对用户指定的饮品 **{{drink}}**，执行全网拆解、BOM 成本精算与商业优化闭环：

1. 运行 `python scripts/beverage_engine.py auto-pipeline --query "{{drink}}" --optimize-mode {{mode}} --save-to-db`
2. 运行 `python scripts/beverage_engine.py render-html --output examples/beverage_interactive_portal.html`
3. 向用户输出完整的【500ml/700ml 冷热双版商用配方表（精确到ml/g）】、【糖度梯度矩阵】、【单杯BOM成本与外卖毛利精算表】及【商业优化方案】。
