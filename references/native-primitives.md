# Native visual vocabulary

Use these recipes when a diagram would otherwise become a wall of generic boxes. Simple diagrams can remain typographic. Every symbol needs a clear role; decoration must not imply evidence.

| Scientific role | Native construction | Meaning guard |
|---|---|---|
| Control/perturbed cell | Outer ellipse + smaller off-center nucleus ellipse; distinct label and border treatment | Schematic cell, not microscopy evidence; do not imply paired observations |
| Gene-expression vector | 6–10 equally sized thin rectangles in a row/column, nearby descriptive label | Illustrative entries, not actual values unless data-backed |
| Token sequence | Repeated labeled rectangles; mask tokens use a distinct fill + M label | Actual masking ratio belongs in caption only if verified |
| Gene/prior graph | A few native circle nodes and thin no-arrow edges, grouped under an explicit schematic label | Anonymous connectivity is an illustrative glyph; specific named gene edges require evidence |
| Encoder/decoder | Rectangle or native trapezoid-like shape, short internal label, input/output direction clear | Width changes do not assert dimensional compression unless stated |
| Repeated blocks | 2–3 visible offset native rectangles with a verified ×L label | Do not imply a measured layer count from decorative repetition |
| Frozen module | Native module box + direct 'Frozen' label or small padlock-style vector mark | Frozen status must be in contract |
| Addition/concatenation | Circle with '+' for addition; separate 'Concat' box for concatenation | These are different operators, never interchange them for aesthetics |
| Auxiliary objective | Short labeled connection to explicit loss node, separate from inference flow | Do not add objective terms absent from the method |
| Task split | Aligned rows/columns with small anonymous node/cell symbols and explicit train/test labels | Condition counts, seen/unseen status and split rules need manuscript evidence |

The small scene compiler provides basic native shapes and computational arrows. Complex vector glyph groups, non-arrow illustrative relations and imported verified vector plots can be authored directly in mxGraph XML. Apply the same contract and exported vector/font audits. Do not flatten the whole diagram into one SVG/image shape to satisfy file-format checks.

Reference grammar: TxPert uses short embedding strips and graph nodes; CellFM uses token rows and module zooms; scLong uses grouped vector symbols; DINO favors plain mathematical nodes. Choose the least complex symbol that makes the paper easier to read.
