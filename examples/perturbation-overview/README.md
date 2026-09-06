# 六版完整示例 / Six-version example

[中文项目说明](../../README.md) · [English project README](../../README.en.md) · [提示词与方法说明 / Prompts and method brief](PROMPTS.md)

三种构图分别强调预测、视图学习与共享表征。每种构图的克制与鲜艳配色共享相同文字、几何和连线路径。此处使用中性名称；图形是方法与任务示意，不是实验结果。

The three compositions emphasize prediction, view learning and shared representations. Each restrained/vivid pair shares the same labels, geometry and connector routes. Neutral names are used throughout; these are method and task schematics, not experimental results.

## Files / 文件

| Design / 构图 | Palette / 配色 | Downloads / 下载 |
| --- | --- | --- |
| 1 | restrained | [PNG](figures/design-1-restrained.png) · [DRAWIO](figures/design-1-restrained.drawio) · [SVG](figures/design-1-restrained.svg) · [PDF](figures/design-1-restrained.pdf) |
| 1 | vivid | [PNG](figures/design-1-vivid.png) · [DRAWIO](figures/design-1-vivid.drawio) · [SVG](figures/design-1-vivid.svg) · [PDF](figures/design-1-vivid.pdf) |
| 2 | restrained | [PNG](figures/design-2-restrained.png) · [DRAWIO](figures/design-2-restrained.drawio) · [SVG](figures/design-2-restrained.svg) · [PDF](figures/design-2-restrained.pdf) |
| 2 | vivid | [PNG](figures/design-2-vivid.png) · [DRAWIO](figures/design-2-vivid.drawio) · [SVG](figures/design-2-vivid.svg) · [PDF](figures/design-2-vivid.pdf) |
| 3 | restrained | [PNG](figures/design-3-restrained.png) · [DRAWIO](figures/design-3-restrained.drawio) · [SVG](figures/design-3-restrained.svg) · [PDF](figures/design-3-restrained.pdf) |
| 3 | vivid | [PNG](figures/design-3-vivid.png) · [DRAWIO](figures/design-3-vivid.drawio) · [SVG](figures/design-3-vivid.svg) · [PDF](figures/design-3-vivid.pdf) |

## 图注 / Captions

1. **预测主线。** 从匹配 control 表达到扰动后表达的预测路径，辅以公共生物先验、图视图学习与任务示意。**Prediction first.** The path from matched control expression to predicted perturbed expression, supported by public biological priors, graph-view learning and task illustrations.
2. **视图学习。** 突出 Student 与 EMA Teacher 的 global/local 视图机制，并展开预测、基因上下文与基准任务。**View learning first.** Student and EMA Teacher learning across global/local views, with supporting prediction, gene-context and benchmark panels.
3. **共享表征。** 先解释公共基因上下文与共享表征，再并列展示训练机制与条件预测路径。**Shared representations first.** Public gene context and shared representations precede parallel learning and conditional-prediction panels.

六版均保留有意义的多视图与多基因状态；单个 encoder 使用单框，不添加装饰性叠层。文字、箭头、模块和图节点原生可编辑；细胞与 DNA 为已嵌入的生成 PNG。无需下载外部素材。

All six retain meaningful multi-view and multi-gene representations. Single encoders use single boxes without decorative stacks. Labels, arrows, modules and graph nodes are native editable objects. Generated cell and DNA PNGs are embedded, so no external asset download is needed.

## Re-export / 重新导出

在仓库根目录运行，需要 draw.io Desktop 与 Python 依赖。新输出保存在被 Git 忽略的 outputs/ 中，不覆盖本例。

Run from the repository root with draw.io Desktop and the Python dependencies available. Exports go to ignored outputs/ rather than overwriting this example.

```bash
python3 -m pip install -r requirements.txt
for source in examples/perturbation-overview/figures/*.drawio; do
  python3 scripts/overview.py export "$source" \
    --out-dir outputs/perturbation-overview \
    --contract examples/perturbation-overview/export-contract.json
done
```

PDF 导出宽度为 180 mm。两套配色应一起维护；内容或位置改变时同步更新配对文件。

PDF exports are 180 mm wide. Maintain each color pair together when changing its content or geometry.

## 参考学习 / Reference study

本例表达曾参考同领域论文图示：scFoundation（主框架、内部机制与任务分图）、CellFM（模型与上下文分区），以及用户提供的 scLong 与 scDFM 图例（清楚连线与更鲜明的模块配色）。这里只发布自行绘制的示例，不附参考论文图片。示例图经过多轮设计，提示词的复用范围见 PROMPTS.md。

The visual study informing this example included scFoundation (framework, mechanism and task panels), CellFM (model and context organization), and user-supplied scLong and scDFM examples (clear connectors and stronger module colors). Only the authored example is distributed here; reference-paper images are not bundled. The figures went through multiple design interactions; PROMPTS.md explains the scope of prompt reuse.
