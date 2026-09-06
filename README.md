# Paper Overview Draw.io

**给它一篇论文，画出 3 种构图 × 2 套配色，共 6 版可编辑的 Overview 图。**

这个 Skill 会先研究同领域顶会、顶刊论文的 overview，学习它们如何呈现科学对象、模型机制和任务，再结合你的论文，用 draw.io 完成三种不同构图，每种提供克制与鲜艳两套正式论文配色。保留用户选定旧图的设计感觉，优先用直接清楚的箭头，并以适量叠层、同系颜色与透明度丰富示意素材。支持生成正式的科研示意素材，也能用真实数据绘图，让 Overview 不再只是方框加箭头。

> Learn from relevant papers. Design three distinct compositions in two palettes. Deliver editable draw.io figures.

## 工作方式

1. **理解论文**：梳理贡献、输入、核心机制和输出，区分已实现方法与设想。
2. **现学参考**：查找同领域论文，实际阅读 overview 图和图注，不套固定风格库。
3. **设计六版**：三种构图各配克制、鲜艳两套配色；同一构图的内容、布局、素材和箭头保持一致。由内容决定多分图、视觉层次和阅读顺序，保留模型自己的设计空间。
4. **制作素材与绘图**：组合 draw.io 原生矢量对象、正式扁平线稿素材和有依据的数据图。
5. **检查并返修一次**：六版生成后，由独立子代理检查箭头、遮挡、对齐、可读性和科学关系；汇总问题后集中返修一次，再核对修复结果，不反复循环。

交付通常包括六份 `.drawio` 源文件、SVG/PDF、对比预览，以及简短图注和参考说明。

## 安装与使用

将仓库克隆到 Codex 的技能目录（目标目录应尚不存在）：

```bash
git clone https://github.com/elan6666/paper-overview-drawio.git ~/.codex/skills/paper-overview-drawio
```

在能识别该技能的 Codex 会话中使用：

```text
使用 $paper-overview-drawio，为这篇论文设计 Overview。
先研究同领域优秀论文的图示表达，再在 draw.io 中完成三种构图，每种提供两套配色，共六版。
素材采用正式、简洁的论文示意风格，最后对照参考图审阅改进。
论文路径：<你的论文或方法说明>
```

也可以指定目标期刊、页面宽度、配色或需要突出的创新点。工作流不强制某种图表、固定分图数量或固定模板。

## 运行环境

- 支持本地技能的代理环境，以及文件读写、论文检索和图像查看能力。
- 需要生成素材时，使用环境提供的 `imagegen` 技能和生图工具；本仓库本身不提供模型或 API 凭据。
- `.drawio` 可在 draw.io / diagrams.net 编辑。辅助导出脚本使用 draw.io Desktop，支持 `DRAWIO_PATH` 指定程序路径。
- 可选 Python 依赖：`python3 -m pip install -r requirements.txt`。简单源文件生成和语义检查只需要标准库；PDF 导出处理与预览使用 PyMuPDF。

## 素材与数据

文字、模块、连线和表征符号尽量保持原生可编辑。生成的细胞、DNA 等插图采用扁平二维轮廓和克制配色，避免写实、发光和过度细节。

生成插图通常是位图。包含这些插图的 SVG/PDF 属于混合媒体，不能宣称全矢量。若要求全矢量，应使用真正的矢量素材或重绘。

实测图表需要真实有效的数据和可复现处理；没有数据时使用明确的机制或任务示意，不编造实验结果。

## 仓库内容

| 路径 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | 技能入口与核心工作流 |
| [references/](references/) | 参考学习、构图、素材、draw.io 与交付说明 |
| [scripts/overview.py](scripts/overview.py) | 可选的简单场景编译、导出与技术检查 |
| [scripts/compare_preview.py](scripts/compare_preview.py) | 三版 PDF 等物理宽度对比预览 |
| [assets/examples/](assets/examples/) | 合成方法的最小辅助脚本测试样例 |
| [tests/](tests/) | 辅助脚本回归检查 |

**测试样例是简单的编译测试，不是最终论文图的视觉标准。** 实际设计应由论文内容与本轮参考学习驱动，可直接编写 mxGraph XML 或使用编辑器，不受小型辅助脚本限制。

运行辅助脚本测试：

```bash
python3 -m unittest discover -s tests -v
```

生成一份测试源文件：

```bash
python3 scripts/overview.py build \
  assets/examples/paper-contract.json \
  assets/examples/version-1.scene.json \
  --out outputs/example.drawio
```

该技能辅助设计与检查，不保证期刊接收；最终科学内容仍需作者核对。
