# Paper Overview Draw.io

[中文](README.md) · **English**

**Turn a paper into six editable overview figures: 3 compositions × 2 palettes.**

Study actual figures from relevant papers, then design complementary panels around your method. The skill supports formal scientific artwork, clear connectors, and one consolidated repair pass following independent subagent review. Deliverables include `.drawio` sources and PNG, SVG and PDF exports.

## Six-version example

This neutrally titled example illustrates a perturbation-prediction method. The three compositions emphasize **prediction, view learning and shared representations**. Each has restrained and vivid palettes with identical content and geometry. Click any image to view it at full size.

| Palette | 1 · Prediction first | 2 · View learning first | 3 · Shared representations first |
| --- | --- | --- | --- |
| Restrained | [![Prediction: restrained](examples/perturbation-overview/figures/design-1-restrained.png)](examples/perturbation-overview/figures/design-1-restrained.png) | [![View learning: restrained](examples/perturbation-overview/figures/design-2-restrained.png)](examples/perturbation-overview/figures/design-2-restrained.png) | [![Shared representations: restrained](examples/perturbation-overview/figures/design-3-restrained.png)](examples/perturbation-overview/figures/design-3-restrained.png) |
| Vivid | [![Prediction: vivid](examples/perturbation-overview/figures/design-1-vivid.png)](examples/perturbation-overview/figures/design-1-vivid.png) | [![View learning: vivid](examples/perturbation-overview/figures/design-2-vivid.png)](examples/perturbation-overview/figures/design-2-vivid.png) | [![Shared representations: vivid](examples/perturbation-overview/figures/design-3-vivid.png)](examples/perturbation-overview/figures/design-3-vivid.png) |

[Sources and exports for all six figures](examples/perturbation-overview/README.md) · [Complete prompts and method brief in Chinese and English](examples/perturbation-overview/PROMPTS.md)

This example was developed through multiple design and feedback interactions. The prompts consolidate that process; they are not a verbatim single-turn transcript. Use the included source files for exact reuse. Graphs, vectors and tasks are schematic, with no empirical performance results. Text, modules and arrows are native editable objects; the cell and DNA illustrations are embedded generated bitmaps.

## Install and use

Clone this repository into your Codex skills directory. The destination should not already exist:

```bash
git clone https://github.com/elan6666/paper-overview-drawio.git ~/.codex/skills/paper-overview-drawio
```

Then use it in a session that supports the skill:

```text
Use $paper-overview-drawio to design an overview for this paper.
Study relevant paper figures first, then produce 3 compositions × 2 palettes: 6 versions.
Use formal, simple scientific artwork, clear arrows and scientifically meaningful repetition.
Have an independent subagent inspect the rendered figures, then apply one consolidated repair pass.
Paper path: <your paper or method brief>
```

You can specify a target journal, figure width, preferred colors, key contributions, or an existing editable figure whose design you want to preserve.

## Workflow

1. **Understand the method:** identify contributions, inputs, mechanisms and outputs; distinguish implementations from proposals.
2. **Study relevant figures:** inspect actual overviews and captions rather than selecting from a fixed style library.
3. **Design six versions:** three substantively different compositions, each in restrained and vivid palettes.
4. **Draft, then refine in the app:** create an editable `.drawio` draft, then use computer-use tools inside draw.io to refine connectors, alignment, spacing and styles. Save before exporting; add formal artwork or genuine data plots when useful.
5. **Review and repair once:** an independent subagent checks all six exports for arrows, overlap, alignment, legibility, unjustified repetition and scientific relationships. Apply one consolidated repair pass and verify the fixes.

Visual richness should come from scientific objects and mechanisms. A single encoder is normally one module. Use stacking, repetition and opacity only when their scientific meaning can be explained. Keep labels short and put longer explanations in captions.

## Requirements and outputs

- An agent environment supporting local skills, file access, paper retrieval and image inspection. In-app refinement also requires working computer-use tools. Interaction failures and file-based fallbacks must be disclosed rather than described as UI edits.
- For generated assets, the environment's `imagegen` skill and generation tool. This repository does not supply models or API credentials.
- Edit `.drawio` sources in draw.io / diagrams.net. The export helper uses draw.io Desktop; set `DRAWIO_PATH` to override its location.
- Optional dependencies: `python3 -m pip install -r requirements.txt`. Simple scene compilation and semantic checks use the standard library; PDF processing and previews use PyMuPDF.
- SVG/PDF files may embed raster illustrations. Their extension does not imply all-vector content. Empirical plots require valid source data and reproducible processing; never fabricate results.

## Repository contents

| Path | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Skill entry point and workflow |
| [examples/perturbation-overview/](examples/perturbation-overview/) | Complete six-version example, sources, prompts and notes |
| [references/](references/) | Peer study, composition, artwork, draw.io and delivery guidance |
| [scripts/overview.py](scripts/overview.py) | Optional simple-scene compilation, export and technical checks |
| [scripts/compare_preview.py](scripts/compare_preview.py) | Equal-width PDF comparison for three compositions; run separately for each palette |
| [assets/examples/](assets/examples/) | Minimal compiler fixtures, not a visual standard for finished paper figures |
| [tests/](tests/) | Helper regression checks |

```bash
python3 -m unittest discover -s tests -v
```

The example does not prescribe layouts for other papers. Each design should follow its paper and current reference study. Authors remain responsible for checking the scientific content.
