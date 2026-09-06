# Illustrations and data panels: optional design tools

An overview can weave together architecture, biological entities, representation glyphs, dataset context and applications. Choose the elements that help explain this paper. Neither a chart nor an illustration is mandatory, and a figure does not become better merely by adding more objects.

CellFM Fig. 1 offers inspiration for combining model structure with dataset and application panels; TxPert Fig. 2b shows how cell and graph symbols explain task splits. Appearance alone does not establish the software used or whether a task thumbnail represents measured data.

## Biological illustrations

Use native draw.io groups for simple cells, nuclei, tokens or graph glyphs. For a complex illustration that benefits from generation, read the installed imagegen skill and use its built-in route. Isolated assets with a consistent palette, viewpoint and preferably transparent background are easier to compose than a generated full overview. Keep explanatory labels and arrows separate and editable.

An example prompt direction is a formal flat 2D cell symbol: thin charcoal outline, white interior, solid nucleus, a few simple internal marks, transparent background and no text. Avoid realistic anatomy, glow, texture and volumetric shading for this user. Adapt it to the scientific role; do not treat it as a fixed prompt. Inspect outputs for misleading biological details and save selected assets with the project. Retain prompts when useful for revisions.

Respect the user's vector preference. Generated bitmaps may be included when allowed, with clear disclosure. For all-vector output, simplify/redraw as genuine vector shapes instead. Embedding a PNG inside an SVG does not vectorize it.

## Real-data graphics

Python can produce a suitable chart from the available evidence. For example, composition counts might benefit from a bar or donut; an expression matrix from a heatmap; observations from a distribution or scatter plot; measured relationships from a network. These are suggestions, not required chart choices. Choose based on the message and available data, and feel free to use another form.

Use actual data for empirical graphics. Keep enough provenance and plotting code to reproduce or revise the panel: source, relevant filtering/transformations, units and any stochastic seed. Explain uncertainty where present. If data are unavailable, use an unmistakable schematic or omit the panel rather than generating plausible-looking results. Follow project data/compute boundaries.

Matplotlib, Seaborn and domain tools are possible routes. Set fonts and panel dimensions for the final composition and prefer vector export when appropriate. In Matplotlib, `svg.fonttype = 'none'` and `pdf.fonttype = 42` help preserve text; some heatmap/image artists still embed rasters. A non-rasterized `pcolormesh` is one option for a vector heatmap, not a mandatory plotting method. Inspect exports rather than trusting the filename.

## Composition and review

Import each useful asset into draw.io while keeping the structural backbone editable. The optional small scene compiler handles native shapes only; use the editor or direct XML for richer compositions instead of letting the helper limit the figure.

Retain standalone plot SVG/PDF and source scripts. An imported plot may be vector yet not editable as chart data in draw.io; values can be revised through its script. Inspect the composed export because imports can change fonts or become rasterized. Report the actual editability and bitmap boundary plainly.

Use a brief asset note if several external assets need tracking. A formal JSON manifest is optional. The bundled strict vector audit rejects image elements, including some vector wrappers and all mixed-media figures; a failure requires inspection, not an unsupported pass claim. For permitted mixed media, visually check the inserts and verify that unintended rasterization has not flattened the surrounding structure or text.
