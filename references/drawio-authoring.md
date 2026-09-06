# Native draw.io authoring

## Authoring strategy

Create an original scene from the paper contract; don't vector-trace the entire reference image. Keep the source easily editable: individual text labels, connectors with arrowheads on the same edge, groupable modules, separate token/matrix cells and native circle graph nodes. Graph edges should reference actual node IDs rather than floating line endpoints.

Use meaningful group/node IDs. Author geometry with measured columns/rows and generous label clearance. Use a low number of turns in each scientific path; place a real fusion node where streams meet. A connector crossing is not a junction. Label ambiguous line types directly. Do not use a line plus a separate triangle to simulate an arrow.

The helper accepts simple scenes but does not choose positions. Use explicit waypoints for return paths. Never run automatic layout over a carefully composed final scene unless it is intentionally being redesigned.

## Vector boundary

A .drawio file or an SVG container can still contain PNG/JPEG. “Vector” here means no embedded raster images and no screenshot-as-background. Keep structural elements, labels and connectors native and editable. Mixed-media output may contain isolated generated illustrations; follow illustrations-and-data-panels.md and disclose bitmap inserts. When all-vector output is required, use native elements and verified vector assets. Complex biological icons should become simple schematic cells/organs if their exact appearance is not part of the science. AI image outputs cannot be made vector merely by changing extension or embedding them in SVG.

For actual measured plots, use the paper's real source data and a plotting tool, export vector, then inspect imported structure. Such imports require a direct-XML route beyond the small compiler. Document which parts are native editable vs imported vector paths; do not call imported paths semantically editable charts. Never convert text to outlines unless the export requirement demands it; preserve a text-editable source.

## Runtime

`overview.py export` locates native draw.io Desktop. On macOS it launches a separate CLI profile so the user's interactive session remains untouched, exports PNG/SVG/PDF serially, and checks artifact existence. It then scales the PDF with vector form objects (no rasterization) and sets SVG physical dimensions to the contract width. PDF text remains extractable. `DRAWIO_PATH` overrides discovery. The CLI can need a graphical session on Linux; report failure rather than substituting a browser screenshot as vector output.

The CLI may warn about SVG foreignObject fallback. Keep labels plain (`html=0;whiteSpace=nowrap;overflow=visible`); use explicit line breaks instead of HTML. In draw.io 31.4.2, `whiteSpace=wrap` can trigger foreignObject labels and PNG fallbacks even when `html=0`; this was detected in the forward test. Do not use it for the all-vector route. Verify PDF text extraction and inspect SVG in a real viewer. Do not assume native XML success equals a successful export.

Maintain revisioned output directories. After user edits to .drawio, that edited file is authoritative; do not blindly regenerate from an old scene. Reconcile geometry/content back to the scene or create a separate new revision with a clear note.
