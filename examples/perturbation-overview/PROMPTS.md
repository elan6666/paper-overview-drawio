# 生成提示词 / Prompts

[中文 README](../../README.md) · [English README](../../README.en.md) · [Example files](README.md)

## 来源说明 / Provenance

这六张图来自一次多轮绘图协作：先形成三种构图，再恢复选定旧稿、整理箭头、派生两套配色，并删除无科学含义的叠层。下面是依据实际指令与方法说明整理的**可复用提示词**，不是逐字单轮记录，也不保证再次运行得到相同像素。精确复用请使用随附 `.drawio` 源文件。

The six figures were developed through multiple interactions: three compositions were established, selected drafts were restored, connectors were refined, two palettes were applied, and decorative stacks were removed. The prompts below **consolidate the instructions and method brief used in that process**. They are not a verbatim single-turn transcript or a guarantee of pixel-identical regeneration. Use the included `.drawio` files for exact reuse.

## 中文：完整绘图提示词

```text
使用 $paper-overview-drawio，根据下方方法说明制作正式论文 Overview。

先学模式：先研究同领域优秀论文的 overview，查看实际图与图注，学习它们
如何组织科学对象、方法机制、输入输出和任务分图。不要套用固定风格库，
不要只做简单的方框流程图。参考图只用于学习表达，不复制其科学内容或数据。

输出 3 种有实质区别的构图，每种提供两套配色，共 6 版：
- 克制配色：白色或浅灰背景，低饱和青绿、蓝、紫与珊瑚色。
- 鲜艳配色：增强上述色系的填色和对比，仍保持正式、平面的论文风格。
同一构图的两套配色必须使用相同内容、坐标、文字、素材与连线路径。

本例的三种叙事：
1. 预测主线：上方解释 control-conditioned prediction，下方展开生物先验、
   graph-view learning 和任务范围。
2. 视图学习：上方展开 Student / EMA Teacher 学习机制，其他分图解释预测、
   公共基因上下文、global/local views 和任务。
3. 共享表征：上方解释公共生物上下文生成基因表征，中间并列学习机制与预测，
   下方展示任务范围。优先保留这种构图的清楚层次。
这是本例的内容安排，不是要求其他论文套用相同布局。

绘制要求：
- 使用 a/b/c 等互补分图；图内以短标签为主，较长解释放到图注。
- 箭头直接、起终点明确；优先直线，只在真实分支、汇合或避障时转弯。
  不要用细小坐标偏差产生阶梯线；避免穿字与无意义交叉。
- 单个 encoder 画成单个模块。不要为增加复杂度叠加 encoder 或向量底片。
  重复、颜色与透明度必须表达实际视图、样本、基因状态或其他明确关系。
- 生物素材采用正式的二维平面示意、细轮廓、简化结构；不写实，不发光，
  不做立体渲染。可以用生图模型制作独立细胞/DNA素材，检查后嵌入。
- 用 draw.io 原生对象保留文字、模块、图节点、向量条与连线的可编辑性。
- 图形表示机制或任务示意。没有真实数据就不画伪造的热图、散点或性能结果。
- 已有选定图稿时直接从其可编辑源文件修改，保留被选中的设计感觉。

完成后由独立 subagent 查看实际导出的六张图，检查箭头、遮挡、对齐、
可读性、无意义重复及科学关系。汇总后集中返修一次，再核对既定修复项。
交付六份 draw.io、PNG、SVG、PDF，3×2 对比预览、简短图注及参考说明。
公开示例使用中性标题 Overview，不出现原论文名称或内部版本标识。
```

## English: complete drawing prompt

```text
Use $paper-overview-drawio to create a formal paper overview from the method brief below.

Study actual overview figures and captions from relevant leading papers first.
Learn how they organize scientific objects, mechanisms, inputs, outputs and tasks.
Do not use a fixed style menu or reduce the result to a generic box-and-arrow diagram.
Learn visual grammar without copying another paper's scientific claims or data.

Deliver three substantively different compositions, each in two palettes: six versions.
- Restrained: white or pale gray backgrounds, muted teal, blue, purple and coral.
- Vivid: stronger fills and contrast within those color families, still flat and formal.
Keep content, geometry, labels, assets and connector routes identical within each pair.

For this example, use three narratives:
1. Prediction first: control-conditioned prediction above biological priors,
   graph-view learning and benchmark tasks.
2. View learning first: Student / EMA Teacher learning above prediction,
   public gene context, global/local views and tasks.
3. Shared representations first: public biological context above parallel learning
   and prediction panels, with task scope below. Preserve this composition's hierarchy.
These arrangements are specific to this example, not templates for every paper.

Use complementary a/b/c panels, short in-figure labels and longer explanations in captions.
Prefer direct arrows with clear endpoints. Bend only for actual branches, merges or
obstacles. Avoid tiny routing steps, text intersections and unnecessary crossings.
A single encoder is one module: do not stack copies or add backing strips for decoration.
Repetition, color and opacity must communicate actual views, samples, gene states or
another identifiable relationship.

Use formal flat 2D biological artwork with thin outlines and simplified anatomy;
no photorealism, glow or 3D rendering. Generate isolated cell/DNA assets when useful
and inspect them before placing them. Keep labels, modules, graph nodes, vector strips
and connectors native and editable in draw.io. Do not fabricate empirical heatmaps,
scatterplots or performance claims. Preserve a selected existing draft by editing its
source instead of reconstructing its style from prose.

Have an independent subagent inspect all six rendered figures for connector clarity,
overlap, alignment, legibility, unjustified duplication and scientific relationships.
Collect one issue list, apply one consolidated repair pass and verify those fixes.
Deliver six draw.io sources with PNG/SVG/PDF exports, a 3-by-2 preview, captions and
reference notes. Use the neutral title Overview; omit the original paper's name and
internal version identifiers from the public example.
```

## 方法说明 / Method brief

**中文。** 本例展示一种基于图的扰动预测方法。公共 STRING 与 GO 关系和可学习的基因 ID 输入共享 Student 图编码器，得到依赖上下文的基因状态。预测路径在完整、未增强的图上运行 Student，对扰动靶点状态求和为 z；匹配 control 表达 x 经过 basal encoder 得到 s，decoder 从 s + z 预测扰动后表达。训练同时使用两个 global views 和八个以靶点为中心的 local views。Student 接收 global/local views；Teacher 仅接收未做节点遮罩的 global 输入，但使用相同采样的 DropEdge 拓扑。Teacher 编码器和 projector 经 EMA 更新。条件一致性与 masked-node 一致性作用于相应表征；spread 正则化 Student 的 projector 前 global 状态。图中联合目标为 Lpred + 0.8 Lcond + 0.4 Lmask + 0.1 Lspread，Lpred 为预测和观测扰动表达间的 MSE。任务示意区分细胞系内未见单基因扰动与由已见单靶点组成的未见组合；基准范围包括 K562、RPE1、Jurkat、HepG2 与 Norman。所有网络与向量都是机制示意，不表示新实验结果。

**English.** This example illustrates graph-based perturbation prediction. Public STRING and GO relations and learned gene IDs feed a shared Student graph encoder to produce contextual gene states. The prediction path runs the Student on the complete, unaugmented graph and sums target states into z. A basal encoder maps matched control expression x to s; a decoder predicts perturbed expression from s + z. Training uses two global views and eight target-centered local views. The Student receives global and local views. The Teacher receives only global inputs without node masking, using the same sampled DropEdge topology. Its encoder and projector are updated by EMA. Condition and masked-node consistency operate on the appropriate representations; spread regularizes Student global states before projection. The illustrated objective is Lpred + 0.8 Lcond + 0.4 Lmask + 0.1 Lspread, with MSE prediction loss. Task panels distinguish within-cell-line unseen single-target perturbations from unseen combinations of seen individual targets; the benchmark scope includes K562, RPE1, Jurkat, HepG2 and Norman. Graphs and vectors are schematic, not new empirical results.

## 素材提示词 / Asset prompt templates

以下是与最终素材风格一致的复用模板，而非已保留的逐字原始生图请求。现有示例已在源文件中嵌入素材，无需重新生成。

These are reusable templates matching the retained assets, not archived verbatim image-generation requests. The source files already embed the assets.

**Cell / 细胞**

```text
An isolated generic cell icon for a formal scientific paper figure. Flat 2D schematic,
thin clean black outlines, a simple nucleus and very few simplified organelles,
minimal muted teal accents, transparent background, no text. No photorealism,
3D depth, shadows, glow, gradients or intricate anatomical texture.
```

**DNA / DNA**

```text
An isolated DNA double-helix icon for a formal scientific paper figure. Simple flat
2D line drawing, thin clean dark outlines, a few restrained teal accents,
transparent background, no text or labels. No 3D rendering, glow or texture.
```
