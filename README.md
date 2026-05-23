# Expert Library — 圆桌讨论专家库

> 🔬 为 book-distillation-v4 的 Phase 1.5 圆桌深化Agent 训练专家角色
>
> 每个专家都是**有血有肉的人物档案**，包含核心立场、经典理论、发言风格、批评争议，
> 在圆桌讨论中能发出独特的、有锋芒的声音。

---

## 📊 训练进度

| 类型 | 已完成 | 总数 |
|:---|:---|:---|
| 商业管理 | **6** | 6 |
| 心理学 | 0 | 5 |
| 文学哲学 | 0 | 6 |
| 科技AI | 0 | 5 |
| 历史传记 | 0 | 4 |
| 自助成长 | 0 | 4 |
| 经济金融 | 0 | 5 |
| 科学科普 | 0 | 5 |
| 通用角色 | 0 | 3 |
| 跨界专家 | 0 | 7 |
| **总计** | **6** | **50** |

---

## ✅ 已训练专家

| # | 专家 | 类型 | 核心理论 | 语录 | L1 | L2 |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | [彼得·德鲁克](experts/business/peter-drucker.md) | 商业管理 | 目标管理、知识工作者、效能vs效率、创造顾客 | 7 | ✅ | ⏳ |
| 2 | [吉姆·柯林斯](experts/business/jim-collins.md) | 商业管理 | 第五级经理人、先人后事、刺猬理念、飞轮效应、斯托克代尔悖论、训练有素、技术加速器、衰落五阶段 | 8 | ✅ | ⏳ |
| 3 | [稻盛和夫](experts/business/inamori-kazuo.md) | 商业管理 | 敬天爱人、成功方程式、阿米巴经营、六项精进、经营十二条、心性修炼 | 9 | ✅ | ⏳ |
| 4 | [迈克尔·波特](experts/business/michael-porter.md) | 商业管理 | 五力模型、三大通用战略、价值链、钻石模型、战略vs运营有效性 | 8 | ✅ | ⏳ |
| 5 | [克莱顿·克里斯坦森](experts/business/clayton-christensen.md) | 商业管理 | 颠覆性创新、价值网络、创新者窘境、待完成的工作、独立组织原则、动机理论 | 8 | ✅ | ⏳ |
| 6 | [杰克·韦尔奇](experts/business/jack-welch.md) | 商业管理 | 数一数二战略、活力曲线、六西格玛、无边界组织、克劳顿村、坦诚文化 | 9 | ✅ | ⏳ |

---

## 🏗️ 评估体系

| 等级 | 名称 | 内容 | 检查方式 |
|:---|:---|:---|:---|
| L1 | 信息完整度 | 8项指标全部达标 | 自动检查 |
| L2 | 仿真发言测试 | 放入圆桌讨论中检验发言质量 | 模拟圆桌 |
| L3 | 跨专家去同质化 | 同类型专家间进行正交检验 | 对比分析 |

---

## 📁 目录结构

```
expert-library/
├── README.md              ← 你在这里
├── index.json             ← 可机器读取的专家索引
├── training-progress.md   ← 详细训练进度与日志
├── templates/
│   └── expert-profile-template.md  ← 档案模板
└── experts/
    ├── business/          ← 商业管理专家
    ├── psychology/        ← 心理学专家
    ├── philosophy/        ← 文学哲学专家
    ├── technology/        ← 科技AI专家
    ├── history/           ← 历史传记专家
    ├── self-help/         ← 自助成长专家
    ├── economics/         ← 经济金融专家
    ├── science/           ← 科学科普专家
    ├── generic/           ← 通用角色模板
    └── cross-domain/      ← 跨界专家
```

---

## 🚀 使用方式

1. **训练新专家**：激活 `expert-training` skill，按模板逐位训练
2. **续训**：检查 `training-progress.md` 找到断点，给 AI 发送 `续训 专家名`
3. **在蒸馏中使用**：将训练好的专家档案提供给 `book-distillation-v4` 的圆桌Agent

---

## 🔗 相关项目

- [book-distillation-v4](https://github.com/XCDaHuiGe/book-distillation) — 主蒸馏系统
- 训练 Skill：`C:\Users\gai\.trae-cn\skills\expert-training\SKILL.md`