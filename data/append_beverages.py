#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Appends 12 additional flagship commercial beverage formulas to data/beverages_db.json
bringing total structured commercial formulas to 24.
"""

import json
from pathlib import Path

EXTRA_BEVERAGES = [
    {
        "id": "tea_08", "category": "light_milk_tea",
        "name": "去云南·玫瑰普洱轻乳茶 (春日桃桃/寻香普洱同款)",
        "positioning": "秋冬温润养胃爆款 / 差异化茶底",
        "flavor_profile": "前调墨红重瓣玫瑰花香 -> 中调勐海陈年熟普醇滑木质香 -> 尾韵厚牛乳甜香",
        "base_size_ml": 500,
        "sugar_levels_g": {"标准糖": 22, "七分糖(推荐)": 16, "五分糖": 11},
        "bom_cost_cny": {"raw_materials": 2.65, "packaging": 0.75, "total_cost": 3.40, "suggested_retail": 16.0, "gross_margin_pct": 78.8},
        "ingredients_500ml_iced": [
            {"item": "勐海玫瑰熟普洱茶汤", "amount": 190, "unit": "ml", "cost": 0.45},
            {"item": "巴氏鲜牛奶", "amount": 110, "unit": "ml", "cost": 1.30},
            {"item": "浓缩厚牛乳", "amount": 30, "unit": "ml", "cost": 0.70},
            {"item": "黄金果糖", "amount": 16, "unit": "g", "cost": 0.20},
            {"item": "机制方冰", "amount": 150, "unit": "g", "cost": 0.00}
        ],
        "sop_steps": [
            "雪克杯加入鲜奶110ml、厚牛乳30ml、黄金果糖16g与玫瑰熟普茶汤190ml。",
            "加冰150g雪克摇匀12次至泡沫丰富，滤冰入杯，表面撒可食用干玫瑰花瓣2片。"
        ],
        "hot_400ml_adjustment": "玫瑰熟普茶汤200ml + 鲜奶130ml + 厚乳30ml + 果糖15g，蒸汽打热至65℃（熟普极适合做热饮）。"
    },
    {
        "id": "tea_09", "category": "light_milk_tea",
        "name": "万里木兰·锡兰肉桂红茶轻乳",
        "positioning": "高级辛香东方茶拿铁",
        "flavor_profile": "斯里兰卡汀布拉红茶与微弱肉桂生姜暖香交织",
        "base_size_ml": 500,
        "sugar_levels_g": {"标准糖": 20, "七分糖": 15, "五分糖": 10},
        "bom_cost_cny": {"raw_materials": 2.60, "packaging": 0.75, "total_cost": 3.35, "suggested_retail": 15.0, "gross_margin_pct": 77.7},
        "ingredients_500ml_iced": [
            {"item": "锡兰高地红茶汤", "amount": 190, "unit": "ml", "cost": 0.40},
            {"item": "全脂鲜牛奶", "amount": 120, "unit": "ml", "cost": 1.40},
            {"item": "动物稀奶油", "amount": 20, "unit": "ml", "cost": 0.65},
            {"item": "黑糖/黄糖浆", "amount": 15, "unit": "g", "cost": 0.15},
            {"item": "机制冰块", "amount": 150, "unit": "g", "cost": 0.00}
        ],
        "sop_steps": [
            "雪克杯混合红茶汤、鲜奶、稀奶油与黄糖浆，加冰猛烈雪克10次。",
            "倒入出品杯，顶部轻筛极微量（0.1g）肉桂粉提香。"
        ],
        "hot_400ml_adjustment": "蒸汽加热至65℃，暖身驱寒效果极佳。"
    },
    {
        "id": "tea_10", "category": "classic_milk_tea",
        "name": "手捣荔浦芋泥波波厚乳茶",
        "positioning": "秋冬饱腹感销冠 / 代餐级奶茶",
        "flavor_profile": "绵密起沙带颗粒感的广西荔浦芋泥挂壁 + 软糯芋圆波波 + 茉莉绿茶鲜奶",
        "base_size_ml": 500,
        "sugar_levels_g": {"标准(芋泥已带甜仅加10g糖)": 10, "少甜(0额外加糖)": 0},
        "bom_cost_cny": {"raw_materials": 3.75, "packaging": 0.80, "total_cost": 4.55, "suggested_retail": 17.0, "gross_margin_pct": 73.2},
        "ingredients_500ml_iced": [
            {"item": "现蒸手捣荔浦奶香芋泥", "amount": 100, "unit": "g", "cost": 1.45},
            {"item": "小芋圆波波", "amount": 50, "unit": "g", "cost": 0.55},
            {"item": "茉莉绿茶/铁观音乌龙茶汤", "amount": 130, "unit": "ml", "cost": 0.25},
            {"item": "全脂鲜牛奶", "amount": 120, "unit": "ml", "cost": 1.40},
            {"item": "黄金果糖", "amount": 10, "unit": "g", "cost": 0.10},
            {"item": "冰块", "amount": 100, "unit": "g", "cost": 0.00}
        ],
        "sop_steps": [
            "【自制商用芋泥】荔浦芋头500g蒸熟趁热压泥（保留15%细小颗粒感），趁热拌入紫薯粉5g（天然浅紫调色）、炼乳40g、黄油20g、白糖30g与鲜奶120ml搅打顺滑。",
            "【抹壁打底】取100g芋泥用抹刀在杯内壁涂抹出厚重敦煌云纹挂壁，杯底加入50g温热小芋圆。",
            "【雪克注茶】雪克杯将绿茶汤130ml、鲜奶120ml、果糖10g与冰块100g摇匀，滤入杯中。"
        ],
        "hot_400ml_adjustment": "秋冬主力热饮：芋泥挂壁+芋圆打底，直接冲入65℃热鲜奶绿茶，无需加冰。"
    },
    {
        "id": "tea_11", "category": "classic_milk_tea",
        "name": "一点点同款·波霸奶绿配冰淇淋球",
        "positioning": "学生党与夜市怀旧流量王",
        "flavor_profile": "香草冰淇淋球融化在茉莉奶绿中的极致冰爽奶香 + Q弹混珠",
        "base_size_ml": 500,
        "sugar_levels_g": {"标准糖": 20, "七分糖": 14, "五分糖(推荐)": 10},
        "bom_cost_cny": {"raw_materials": 2.95, "packaging": 0.75, "total_cost": 3.70, "suggested_retail": 15.0, "gross_margin_pct": 75.3},
        "ingredients_500ml_iced": [
            {"item": "茉莉绿茶汤", "amount": 200, "unit": "ml", "cost": 0.35},
            {"item": "雀巢全脂牛乳/浓缩乳基底", "amount": 100, "unit": "ml", "cost": 1.20},
            {"item": "琥珀珍珠/混珠", "amount": 70, "unit": "g", "cost": 0.45},
            {"item": "大牌香草冰淇淋球(1大勺)", "amount": 50, "unit": "g", "cost": 0.85},
            {"item": "黄金果糖", "amount": 10, "unit": "g", "cost": 0.10},
            {"item": "冰块", "amount": 140, "unit": "g", "cost": 0.00}
        ],
        "sop_steps": [
            "出品杯底加入70g琥珀珍珠。",
            "雪克杯加入绿茶汤200ml、牛乳基底100ml、果糖10g与冰块140g摇匀倒入杯中至8分满。",
            "用冰淇淋挖球勺挖取一颗50g饱满香草冰淇淋球浮于液面顶部。"
        ],
        "hot_400ml_adjustment": "冰淇淋款仅限冷饮或去冰常温。"
    },
    {
        "id": "tea_12", "category": "classic_milk_tea",
        "name": "古茗同款·百香三重奏 / 椰果双响炮",
        "positioning": "低成本高毛利果味引流款",
        "flavor_profile": "海南金钻百香果酸香 + Q弹椰果与珍珠双料咀嚼感 + 茉莉绿茶",
        "base_size_ml": 700,
        "sugar_levels_g": {"标准糖(百香果极酸需足糖)": 45, "七分糖": 36, "五分糖": 28},
        "bom_cost_cny": {"raw_materials": 2.20, "packaging": 0.85, "total_cost": 3.05, "suggested_retail": 13.0, "gross_margin_pct": 76.5},
        "ingredients_500ml_iced": [
            {"item": "冷冻百香果原浆(带籽)", "amount": 55, "unit": "g", "cost": 1.00},
            {"item": "原味高纤椰果粒", "amount": 50, "unit": "g", "cost": 0.35},
            {"item": "琥珀珍珠/寒天晶球", "amount": 40, "unit": "g", "cost": 0.35},
            {"item": "茉莉绿茶汤", "amount": 260, "unit": "ml", "cost": 0.40},
            {"item": "黄金果糖", "amount": 45, "unit": "g", "cost": 0.35},
            {"item": "冰块", "amount": 220, "unit": "g", "cost": 0.00}
        ],
        "sop_steps": [
            "700ml大杯底加入50g椰果与40g珍珠/寒天晶球。",
            "雪克杯加入55g百香果原浆、45g果糖、260ml茉莉绿茶汤与220g冰块，大力雪克12次倒入杯中封口。"
        ],
        "hot_400ml_adjustment": "百香果浆40g + 绿茶220ml + 热水100ml + 果糖35g。"
    },
    {
        "id": "tea_13", "category": "lemon_fruit_tea",
        "name": "泰式暴打咸金桔手标绿茶柠檬茶",
        "positioning": "夜市解暑猎奇爆款 / 翠绿吸睛视觉",
        "flavor_profile": "泰国手标绿茶独特的斑斓香草香气 + 广式老盐咸金桔与香水柠檬的咸酸回甘",
        "base_size_ml": 700,
        "sugar_levels_g": {"标准糖": 40, "七分糖": 32, "五分糖": 24},
        "bom_cost_cny": {"raw_materials": 2.05, "packaging": 0.85, "total_cost": 2.90, "suggested_retail": 15.0, "gross_margin_pct": 80.7},
        "ingredients_500ml_iced": [
            {"item": "广东香水柠檬片", "amount": 45, "unit": "g", "cost": 0.80},
            {"item": "潮汕陈年咸金桔", "amount": 1, "unit": "颗(约12g)", "cost": 0.35},
            {"item": "新鲜香茅草段", "amount": 10, "unit": "g(拍裂)", "cost": 0.15},
            {"item": "泰国手标绿茶汤(翡翠绿色)", "amount": 260, "unit": "ml", "cost": 0.40},
            {"item": "黄金果糖", "amount": 40, "unit": "g", "cost": 0.35},
            {"item": "机制冰块", "amount": 250, "unit": "g", "cost": 0.00}
        ],
        "sop_steps": [
            "雪克杯放入香水柠檬片、1颗去核咸金桔、拍裂香茅草与50g冰块，用捣棒暴打15下。",
            "加入40g果糖、剩余200g冰块与260ml翡翠色泰式绿茶汤，猛烈雪克15次连渣入700ml大桶杯。"
        ],
        "hot_400ml_adjustment": "咸金桔热泡润喉化痰极佳，柠檬片减为2片防苦。"
    },
    {
        "id": "tea_14", "category": "lemon_fruit_tea",
        "name": "满杯霸气红西柚绿茶 (奈雪销冠同款)",
        "positioning": "经典微苦清爽鲜果茶代表",
        "flavor_profile": "南非红宝石西柚果粒爆汁微苦回甜 + 七窨茉莉绿茶清香",
        "base_size_ml": 500,
        "sugar_levels_g": {"标准糖(中和西柚微苦)": 32, "七分糖": 25, "五分糖": 18},
        "bom_cost_cny": {"raw_materials": 3.40, "packaging": 0.80, "total_cost": 4.20, "suggested_retail": 16.0, "gross_margin_pct": 73.8},
        "ingredients_500ml_iced": [
            {"item": "红西柚鲜果片(贴杯壁装饰)", "amount": 2, "unit": "大片", "cost": 0.80},
            {"item": "手剥红西柚果肉粒", "amount": 45, "unit": "g", "cost": 1.10},
            {"item": "红西柚冷冻原汁果溶", "amount": 35, "unit": "g", "cost": 0.90},
            {"item": "七窨茉莉绿茶汤", "amount": 200, "unit": "ml", "cost": 0.35},
            {"item": "黄金果糖", "amount": 32, "unit": "g", "cost": 0.25},
            {"item": "冰块", "amount": 160, "unit": "g", "cost": 0.00}
        ],
        "sop_steps": [
            "两片完整红西柚薄片紧贴500ml高透杯内壁做视觉环绕（切记剥果肉时彻底剥净白色苦味内皮）。",
            "雪克杯中放入45g红西柚果粒轻压3下，加入35g西柚果溶、32g果糖、200ml茉莉绿茶汤与160g冰块。",
            "雪克摇匀12次倒入贴好西柚片的杯中。"
        ],
        "hot_400ml_adjustment": "不宜高温煮西柚片，否则柚皮苷析出极苦。"
    },
    {
        "id": "tea_15", "category": "lemon_fruit_tea",
        "name": "喜茶同款·多肉桃桃乌龙冻冻",
        "positioning": "少女心粉色爆款 / 高客单果茶",
        "flavor_profile": "阳山水蜜桃甜润果肉 + 清香四季春茶冻 + 醇厚海盐芝士奶盖",
        "base_size_ml": 500,
        "sugar_levels_g": {"标准糖": 26, "七分糖": 20, "五分糖": 14},
        "bom_cost_cny": {"raw_materials": 4.25, "packaging": 0.85, "total_cost": 5.10, "suggested_retail": 18.0, "gross_margin_pct": 71.7},
        "ingredients_500ml_iced": [
            {"item": "鲜水蜜桃丁/黄金蜜桃果肉", "amount": 60, "unit": "g", "cost": 1.20},
            {"item": "水蜜桃冷冻果溶", "amount": 45, "unit": "g", "cost": 1.20},
            {"item": "桂花/四季春茶冻", "amount": 50, "unit": "g", "cost": 0.40},
            {"item": "四季春乌龙茶汤", "amount": 120, "unit": "ml", "cost": 0.25},
            {"item": "黄金果糖", "amount": 24, "unit": "g", "cost": 0.20},
            {"item": "冰块", "amount": 180, "unit": "g", "cost": 0.00},
            {"item": "海盐芝士奶盖", "amount": 60, "unit": "ml", "cost": 1.00}
        ],
        "sop_steps": [
            "杯底放50g茶冻与60g鲜蜜桃果肉丁捣压。",
            "冰沙机加入45g蜜桃果溶、120ml四季春茶汤、24g果糖与180g冰块打成粉嫩冰沙倒入杯中。",
            "顶部淋入60ml海盐芝士奶盖。"
        ],
        "hot_400ml_adjustment": "果溶与茶汤温热至55℃冲入蜜桃丁中。"
    },
    {
        "id": "cof_05", "category": "specialty_coffee",
        "name": "南洋风情·斑斓生椰冰拿铁",
        "positioning": "东南亚网红视觉分层款 (绿+白+棕三色)",
        "flavor_profile": "底层鲜榨斑斓叶糯米香 + 中层冷榨生椰乳 + 顶层醇苦意式浓缩",
        "base_size_ml": 500,
        "sugar_levels_g": {"标准(斑斓糖浆15g)": 15, "微甜": 8},
        "bom_cost_cny": {"raw_materials": 3.90, "packaging": 0.80, "total_cost": 4.70, "suggested_retail": 18.0, "gross_margin_pct": 73.9},
        "ingredients_500ml_iced": [
            {"item": "海南鲜榨斑斓叶汁/斑斓冻", "amount": 50, "unit": "g", "cost": 0.65},
            {"item": "菲诺特调生椰乳", "amount": 170, "unit": "ml", "cost": 2.00},
            {"item": "双份中深烘意式浓缩", "amount": 38, "unit": "ml", "cost": 1.15},
            {"item": "原味糖浆", "amount": 10, "unit": "g", "cost": 0.10},
            {"item": "机制冰块", "amount": 170, "unit": "g", "cost": 0.00}
        ],
        "sop_steps": [
            "杯底加入50g翠绿色的斑斓冻（或斑斓汁+糖浆混合液沉底）。",
            "加入170g满杯冰块，沿冰块缓慢倒入170ml纯白生椰乳形成下绿中白分层。",
            "顶部淋入38ml深棕意式浓缩，呈现绝美三色渐变。"
        ],
        "hot_400ml_adjustment": "斑斓汁与生椰乳一同蒸汽打热至62℃融合浓缩。"
    },
    {
        "id": "cof_06", "category": "specialty_coffee",
        "name": "海盐焦糖芝士奶盖冰美式",
        "positioning": "抗苦入门高毛利特调",
        "flavor_profile": "顶部咸甜绵密芝士奶盖融合焦糖香，大口饮用时包裹清爽冰美式",
        "base_size_ml": 500,
        "sugar_levels_g": {"标准(焦糖糖浆15g)": 15, "无额外糖(仅奶盖甜)": 0},
        "bom_cost_cny": {"raw_materials": 2.65, "packaging": 0.75, "total_cost": 3.40, "suggested_retail": 16.0, "gross_margin_pct": 78.8},
        "ingredients_500ml_iced": [
            {"item": "双份意式浓缩咖啡", "amount": 38, "unit": "ml", "cost": 1.15},
            {"item": "冰直饮水", "amount": 180, "unit": "ml", "cost": 0.05},
            {"item": "海盐焦糖风味糖浆", "amount": 15, "unit": "g", "cost": 0.35},
            {"item": "海盐芝士奶盖", "amount": 65, "unit": "ml", "cost": 1.10},
            {"item": "冰块", "amount": 160, "unit": "g", "cost": 0.00}
        ],
        "sop_steps": [
            "杯底加15g海盐焦糖糖浆、180ml冰水与160g冰块，倒入38ml双份浓缩搅匀成冰美式基底。",
            "液面顶部轻轻铺满65ml浓稠海盐芝士奶盖，表面筛少许法芙娜可可粉，配直饮口杯盖。"
        ],
        "hot_400ml_adjustment": "热美式基底65℃ + 顶部冰奶盖。"
    },
    {
        "id": "cof_07", "category": "specialty_coffee",
        "name": "夏日爆单·粉红胭脂芭乐(番石榴)冰美式",
        "positioning": "小红书高颜值果咖爆款",
        "flavor_profile": "广西红心芭乐浓郁热带脂粉果香 + 青柠酸爽 + 中浅烘花果调浓缩",
        "base_size_ml": 500,
        "sugar_levels_g": {"标准": 18, "微甜": 10},
        "bom_cost_cny": {"raw_materials": 3.80, "packaging": 0.80, "total_cost": 4.60, "suggested_retail": 18.0, "gross_margin_pct": 74.4},
        "ingredients_500ml_iced": [
            {"item": "红心芭乐(番石榴)冷冻原浆果泥", "amount": 75, "unit": "g", "cost": 1.90},
            {"item": "茉莉绿茶汤/冰纯净水", "amount": 120, "unit": "ml", "cost": 0.25},
            {"item": "鲜青柠汁", "amount": 8, "unit": "ml", "cost": 0.30},
            {"item": "黄金果糖", "amount": 15, "unit": "g", "cost": 0.20},
            {"item": "双份耶加雪菲SOE/果香拼配浓缩", "amount": 36, "unit": "ml", "cost": 1.15},
            {"item": "冰块", "amount": 180, "unit": "g", "cost": 0.00}
        ],
        "sop_steps": [
            "雪克杯将75g红心芭乐果泥、120ml茉莉绿茶汤、8ml青柠汁与15g果糖搅拌均匀倒入出品杯。",
            "铲入180g满杯冰块，顶部缓慢浇入36ml浓缩咖啡，形成下层珊瑚粉、上层琥珀棕的绝美撞色。"
        ],
        "hot_400ml_adjustment": "仅限冰饮。"
    },
    {
        "id": "base_02", "category": "base_topping",
        "name": "【商用备料】黄金Q弹慢熬黑糖珍珠 & 24小时不消泡海盐芝士奶盖SOP",
        "positioning": "全店小料与顶盖核心壁垒",
        "flavor_profile": "珍珠软糯Q弹透芯不硬 + 奶盖咸甜浓稠挂壁",
        "base_size_ml": 1000,
        "sugar_levels_g": {"标准商用": 0},
        "bom_cost_cny": {"raw_materials": 12.50, "packaging": 0.00, "total_cost": 12.50, "suggested_retail": 0.0, "gross_margin_pct": 0.0},
        "ingredients_500ml_iced": [
            {"item": "快煮木薯黑糖珍珠(干重)", "amount": 500, "unit": "g(配沸水3500ml)", "cost": 4.50},
            {"item": "台湾风味古法黑糖蜜", "amount": 220, "unit": "g", "cost": 2.50},
            {"item": "奶盖配方：安佳淡奶油250ml+Kiri奶油芝士60g+全脂奶60ml+炼乳30g+海盐2.5g", "amount": 400, "unit": "g", "cost": 5.50}
        ],
        "sop_steps": [
            "【煮珍珠口诀：煮25焖25】3500ml水大沸后扬入500g珍珠搅散防粘，中火加盖微沸煮25分钟；关火绝不揭盖焖25分钟。",
            "【冲水收蜜】沥出珍珠用直饮冷水冲洗2遍去粘液，入小锅加220g黑糖蜜与100ml水熬煮5分钟至挂勺，转入55℃恒温珍珠锅保存（4小时内最佳）。",
            "【打发不消泡奶盖】室温软化芝士60g加海盐2.5g、炼乳30g与牛奶60ml用均质机打至完全无颗粒，倒入4℃冷藏淡奶油250ml，中高速打发2.5分钟至酸奶般浓稠拉起小弯钩（7成发），冷藏可稳存24小时。"
        ],
        "hot_400ml_adjustment": "珍珠恒温55℃保温；奶盖4℃冷藏随用随取。"
    }
]

if __name__ == "__main__":
    db_file = Path(__file__).parent / "beverages_db.json"
    with open(db_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    existing_ids = {b["id"] for b in data["beverages"]}
    for item in EXTRA_BEVERAGES:
        if item["id"] not in existing_ids:
            data["beverages"].append(item)
    with open(db_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated {db_file}: total {len(data['beverages'])} commercial beverage formulas!")
