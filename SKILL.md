---
name: paper-overview-drawio
description: >-
  Design rich, editable paper overview figures in draw.io by first researching how current same-field papers present their methods. Use when the user requests overview/overall/framework figures, 论文总览图 or three alternative scientific figure designs. Combine formal schematic artwork and meaningful panels, then refine against peer figures with independent review.
---

# Paper Overview in Draw.io

Create a scientific overview that helps readers see the paper's idea, objects and mechanism. **Learn from relevant papers at the time of the task**, rather than choosing from a fixed distilled style library. Deliver three distinct, polished draw.io compositions. A generic box-and-arrow diagram is a starting sketch, not the intended finished result.

## Understand the paper, then learn from its field

Read the user's manuscript or method description and establish the actual contribution, inputs, learning mechanism and outputs. If using a repository, distinguish historical variants from the configuration being illustrated. Choose the level of abstraction appropriate for an overview; do not reproduce an entire implementation just to make it look complex.

Search for closely related papers in leading journals and conferences for this field. Prefer verified publisher/proceedings sources and inspect actual overview figures and captions, using available local PDFs when they match. Read a useful handful deeply rather than accumulating titles. Identify how peers organize the biological problem, architecture, internal mechanism, data context and applications; study the glyphs, panel hierarchy, typography and information density. [Live reference study](references/live-reference-study.md) offers practical guidance.

Keep a short record of the reference figures and what informed the design. Select references for relevance and visual usefulness, not prestige alone. If current sources are inaccessible, use available verified local material and disclose the limitation instead of claiming a fresh visual inspection. There is no required style taxonomy or reference count.

## Design three complete alternatives

Develop three different ways of telling this paper's story using what you just learned and your own design judgment. They may borrow visual grammar, combine inspirations or take an original direction; there is no two-plus-one quota. Explain their strengths briefly and proceed to drawing unless the user asks to discuss first.

Aim for the explanatory depth of the relevant peer figures. Complementary panels such as a/b/c often help: a main biological/model story, an expanded key mechanism, or a supported task/data context. Let the content decide the organization. Richness should come from visual explanations of cells, targets, graphs, representations and transformations—not extra boxes, decoration or a mandatory number of blocks. [Composition notes](references/selection-and-design.md) give soft suggestions.

## Make useful assets and compose in draw.io

Use draw.io as the editable workspace, through native objects, direct mxGraph XML or the editor. Keep text, connectors, modules and representation glyphs editable. The optional [scene helper](references/scene-format.md) supports small native diagrams but is not a limit on the figure or a required pipeline.

Actively consider generated assets when they help explain biological or experimental objects. Use the installed `imagegen` skill and built-in image generation; read its instructions at use time. For the user's preferred paper style, favor **formal flat 2D schematic artwork, thin clean outlines, restrained solid colors and simplified anatomy**. Avoid realistic cells, 3D/glowing renders or intricate textures unless requested. Generate isolated assets rather than a complete figure so scientific labels and relations remain editable. Match the actual reference images and inspect the result at its placed size; revise unsuitable assets rather than accepting them because generation succeeded.

Native diagrams and generated illustrations can work together. Graph nodes, masks, embedding strips and operators often benefit from native vector construction. [Asset notes](references/illustrations-and-data-panels.md) and [visual vocabulary](references/native-primitives.md) are optional aids. Use enough meaningful visual material to explain the paper without turning it into a collage.

If real data improve the overview, use Python or a suitable plotting tool and choose the visual form freely. Empirical charts need real, valid source data and reproducible transformations. Do not create plausible-looking results to fill a panel; a clearly schematic task illustration is different from an experimental chart. Respect project data/compute boundaries.

Generated illustration inserts are usually bitmaps. When allowed, preserve the vector backbone and disclose that mixed-media boundary. If all-vector output is explicitly required, redraw suitable simple artwork as genuine vectors. A PDF/SVG extension does not make a bitmap vector. Retain original assets, prompts and plot scripts where useful for revisions.

## Review against peers and improve

Render all three and inspect the full figure, dense details and final publication size. Check scientific meaning, readable text, connectors, hierarchy, visual consistency and how imports survived export. Place the new figures beside the actual peer overviews: is the central idea visible, are objects and mechanisms explained, and does each panel earn its space?

Use an independent subagent review when available: provide the target-method evidence, reference figures and actual rendered outputs. Ask for specific scientific or visual shortcomings, especially generic-flowchart appearance, ornamental complexity, inconsistent illustration style and weak differences between versions. Repair consequential findings, rerender and have the affected parts rechecked. If subagents are unavailable, perform the comparison yourself and state that limitation.

Finish when the figures have no unresolved high-priority in-scope defects and are reasonably comparable in visual explanation and finish to the selected peers. Do not invent a numeric beauty threshold or imply this establishes journal acceptance. Plugin Eval may help improve skill structure and helper code; its static score cannot certify figure aesthetics.

## Deliver

Provide three editable `.drawio` files, SVG/PDF exports and a comparable-size preview. Briefly explain the design differences, recommend one and include useful captions and reference links. Disclose bitmap inserts, schematic versus measured panels and any scientific uncertainty. Preserve user revisions with versioned outputs.

Use [export notes](references/drawio-authoring.md) and [quality notes](references/quality-and-delivery.md) as needed. Optional scripts support export and technical checks; manifests, JSON contracts and scoring forms are not prerequisites for ordinary design. The small bundled example is a helper smoke fixture only—not an aesthetic standard or a substitute for a real-paper test.
