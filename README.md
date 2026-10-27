# 🧋 饮品大师 (Tea & Coffee Master Skill)

> **商用与专业级奶茶、鲜果茶、精品咖啡研发与制作全能 Skill**  
> 专为 **Gemini、Codex、Claude Code、WorkBuddy、OpenDevin** 等 AI 智能体打造的商业级饮品研发与变现实战技能。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/AI_Agents-Gemini_|_Codex_|_Claude_|_WorkBuddy-orange.svg)](#一键安装与使用指南)

---

## 🌟 核心特色与商业价值

普通菜谱 AI 只能输出模糊的家庭配方（“适量”、“少许”），无法用于商业开店或摆摊。**本 Skill 定位为 20 年经验的饮品研发总监 + 爆款开店实战顾问**：

1. **精准毫米级商用配方**：精确到克（g）、毫升（ml）、秒（s）、水温（℃）。
2. **4 大商用茶汤工业级萃取**：茉莉绿茶、鸭屎香乌龙、阿萨姆红茶、四季春的茶水比、焖泡温控与防涩急速锁香。
3. **爆款网红单品全覆盖**：伯牙绝弦同款茉莉轻乳茶、暴打鸭屎香柠檬茶（700ml）、菲诺生椰拿铁、冰博克 Dirty、多肉葡萄冻冻、芝士海盐奶盖与慢熬黑糖珍珠。
4. **单杯 BOM 成本与毛利精算**：包含液体、小料、包材（高透杯/盖/吸管/袋）综合成本拆解，锁定 **68%~78% 线下毛利率**，附带外卖平台防亏本倒推公式。
5. **供应链大牌平替**：菲诺、Oatly、塞尚厚乳的性价比大宗平替清单，成本直降 30%~40%。
6. **轻启动设备清单**：3000元摆摊极简版、2.5万元档口外卖版、6万元精品综合店。
7. **爆款营销与外卖文案**：2-5-2-1 菜单金字塔结构，感官风味雷达文案与高转化外卖命名法。

---

## 📦 项目目录结构

```text
tea-coffee-master/
├── SKILL.md                          # 智能体核心技能入口 (包含YAML元数据与执行工作流)
├── README.md                         # 详细中英文安装与使用说明
├── WORKBUDDY_SETUP_GUIDE.md          # 针对 WorkBuddy / Dify 等平台的变现与配置指南
├── install.ps1                       # Windows 一键自动安装脚本
├── install.sh                        # macOS / Linux 一键自动安装脚本
└── references/                       # 5 大商用级专业参考知识库
    ├── tea_recipes_sop.md            # 奶茶与鲜果茶商用配方与出品 SOP
    ├── coffee_recipes_sop.md         # 经典意式与商业特调果咖配方 SOP
    ├── cost_calculator.md            # 单杯 BOM 成本精算表与商业定价模型
    ├── equipment_and_supply.md       # 设备采购清单与原料大牌平替供应链
    └── marketing_and_menu.md         # 爆款菜单设计、外卖命名法与营销文案
```

---

## 🚀 一键安装与使用指南 (Installation)

### 1. 在 Gemini / Antigravity 中安装

#### 方式 A：一键命令行自动安装

**Windows (PowerShell)**:
```powershell
irm https://raw.githubusercontent.com/BugMaker123/tea-coffee-master/main/install.ps1 | iex
```

**macOS / Linux (Bash)**:
```bash
curl -fsSL https://raw.githubusercontent.com/BugMaker123/tea-coffee-master/main/install.sh | bash
```

#### 方式 B：手动 Git Clone
将本仓库克隆至你的 Gemini / Antigravity skills 目录：
```bash
# Windows
git clone https://github.com/BugMaker123/tea-coffee-master.git "$env:USERPROFILE\.gemini\config\skills\tea-coffee-master"

# macOS / Linux
git clone https://github.com/BugMaker123/tea-coffee-master.git ~/.gemini/config/skills/tea-coffee-master
```

---

### 2. 在 Codex / ChatGPT / OpenAI Custom GPTs 中使用

1. 打开 [OpenAI Custom GPTs](https://chat.openai.com/gpts/editor) 或 Codex 控制台。
2. 在 **Instructions (系统提示词)** 中：直接复制粘贴本仓库中的 [`SKILL.md`](./SKILL.md) 全文。
3. 在 **Knowledge (知识库文件)** 中：将 `references/` 目录下的 5 份 `.md` 文件打包或逐个上传：
   - `tea_recipes_sop.md`
   - `coffee_recipes_sop.md`
   - `cost_calculator.md`
   - `equipment_and_supply.md`
   - `marketing_and_menu.md`
4. 发布即可获得顶级的“饮品研发与商业化专家”。

---

### 3. 在 WorkBuddy / Dify / 微信智能体中配置

详细图文操作与三大变现赚钱玩法，请查阅专属指南：
👉 [**WorkBuddy 部署与赚钱变现全攻略**](./WORKBUDDY_SETUP_GUIDE.md)

---

### 4. 在 Claude Code / Cursor / OpenDevin 中使用

直接在项目中将本仓库作为子模块或文件夹引入：
```bash
git submodule add https://github.com/BugMaker123/tea-coffee-master.git .skills/tea-coffee-master
```
并在 Prompt 或系统指令中引入 `.skills/tea-coffee-master/SKILL.md`。

---

## 💡 典型使用示例 (Prompt Examples)

安装完成后，你可以向智能体提问：

- 💬 *"请给我一份【生椰拿铁 + 暴打鸭屎香柠檬茶】的详细商用配方、操作SOP与单杯硬成本测算。"*
- 💬 *"我准备在大学城夜市摆摊，手头预算只有 5000 元，请给我一套高性价比设备采购清单和平替原料推荐。"*
- 💬 *"我要在美团上线 8 款饮品，请帮我设计 2-5-2-1 爆款菜单架构，并写出能保证 75% 毛利的满减定价方案。"*
- 💬 *"请为我的新品「茉莉初雪轻乳茶」写一组适合发朋友圈和小红书的高颜值感官风味文案。"*

---

## 📄 许可证 (License)

本项目采用 [MIT 许可证](LICENSE)。欢迎个人使用、开店实操与商业化定制！
