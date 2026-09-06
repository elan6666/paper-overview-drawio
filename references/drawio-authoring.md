# Native draw.io authoring

## Authoring strategy

Create an original scene from the paper contract; don't vector-trace the entire reference image. Keep the source easily editable: individual text labels, connectors with arrowheads on the same edge, groupable modules, separate token/matrix cells and native circle graph nodes. Graph edges should reference actual node IDs rather than floating line endpoints.

Use meaningful group/node IDs. Author geometry with measured columns/rows and generous label clearance. Use a low number of turns in each scientific path; place a real fusion node where streams meet. A connector crossing is not a junction. Label ambiguous line types directly. Do not use a line plus a separate triangle to simulate an arrow.

The helper accepts simple scenes but does not choose positions. Use explicit waypoints for return paths. Never run automatic layout over a carefully composed final scene unless it is intentionally being redesigned.

## File draft, then app refinement

Create the native source first, then open that file in draw.io Desktop for visual refinement through computer-use tools. Inspect the actual canvas, select objects and use the editor controls to adjust routes, placement and styles. Read the updated UI after interactions and verify the result. Save the app-edited file before exporting; CLI export of that saved file is fine. Preserve a versioned copy and treat app edits as authoritative rather than regenerating over them.

If the app can be observed but interaction fails, distinguish these states. Reading an accessibility tree or screenshot does not prove that selection, dragging or saving works. Report the concrete failure and disclose any file-based fallback. Do not claim UI refinement when only XML or CLI operations were performed.

### Recover a non-interactive window

If computer use reports `noWindowsAvailable` even though an old draw.io window remains readable, refresh the tool session and inspect the app again. If that window still cannot be clicked, try creating a new window through the app's New command (Cmd+N on macOS), then open a versioned copy of the saved draft through File → Open. Preserve the original window and any unsaved work; do not force-quit the app as a routine recovery step.

Verify the fresh window with an actual selection or drag, a small edit and Save. Leave text-edit mode before saving, wait for the saved status, then independently inspect the file for the intended content or geometry change. Refresh accessibility indices and screenshots after window changes. A fresh window restored drag, text, fill and save operations in an observed macOS session where resetting the tool alone did not; treat this as a recovery workaround, not a confirmed diagnosis or guaranteed fix. If it still fails, report the remaining limitation and use the disclosed file-based fallback.

## Vector boundary

A .drawio file or an SVG container can still contain PNG/JPEG. “Vector” here means no embedded raster images and no screenshot-as-background. Keep structural elements, labels and connectors native and editable. Mixed-media output may contain isolated generated illustrations; follow illustrations-and-data-panels.md and disclose bitmap inserts. When all-vector output is required, use native elements and verified vector assets. Complex biological icons should become simple schematic cells/organs if their exact appearance is not part of the science. AI image outputs cannot be made vector merely by changing extension or embedding them in SVG.

For actual measured plots, use the paper's real source data and a plotting tool, export vector, then inspect imported structure. Such imports require a direct-XML route beyond the small compiler. Document which parts are native editable vs imported vector paths; do not call imported paths semantically editable charts. Never convert text to outlines unless the export requirement demands it; preserve a text-editable source.

## Runtime

`overview.py export` locates native draw.io Desktop. On macOS it launches a separate CLI profile so the user's interactive session remains untouched, exports PNG/SVG/PDF serially, and checks artifact existence. It then scales the PDF with vector form objects (no rasterization) and sets SVG physical dimensions to the contract width. PDF text remains extractable. `DRAWIO_PATH` overrides discovery. The CLI can need a graphical session on Linux; report failure rather than substituting a browser screenshot as vector output.

The CLI may warn about SVG foreignObject fallback. Keep labels plain (`html=0;whiteSpace=nowrap;overflow=visible`); use explicit line breaks instead of HTML. In draw.io 31.4.2, `whiteSpace=wrap` can trigger foreignObject labels and PNG fallbacks even when `html=0`; this was detected in the forward test. Do not use it for the all-vector route. Verify PDF text extraction and inspect SVG in a real viewer. Do not assume native XML success equals a successful export.

Maintain revisioned output directories. After user edits to .drawio, that edited file is authoritative; do not blindly regenerate from an old scene. Reconcile geometry/content back to the scene or create a separate new revision with a clear note.
