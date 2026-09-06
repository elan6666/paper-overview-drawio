# Optional native-scene helper format (version 1)

Use this format when the bundled compiler helps. Direct draw.io editor/XML workflows are equally valid and need not create these files. These helper constraints do not prescribe the design.

The compiler accepts UTF-8 JSON, uses only native mxGraph objects, and escapes labels as XML. Coordinates are pixels on the declared drawing canvas; publication font size is calculated from `width_mm / canvas.width`. Treat this as the actual final figure width, not the width of a large working canvas.

## Canonical paper-contract.json

```json
{
  "schema_version": 1,
  "paper": "Paper title",
  "message": "One accurate sentence",
  "width_mm": 180,
  "minimum_font_pt": 7,
  "nodes": [
    {"id": "control", "label": "Control expression", "role": "input", "evidence": "methods.md:12"},
    {"id": "encoder", "label": "Cell encoder", "role": "module", "evidence": "methods.md:18"}
  ],
  "edges": [
    {"id": "encode", "source": "control", "target": "encoder", "kind": "data", "evidence": "methods.md:18"}
  ]
}
```

Actual work must have a complete graph. Node roles are descriptive; reserve `role: decoration` for scene-only decoration without scientific semantics. Kinds are `data`, `conditioning`, `loss`, `update`, `callout`. Callouts are scene-only and may not claim a canonical scientific relationship. Canonical labels should be short; put explanation in evidence/caption. The example above is a schema snippet, not a valid complete paper.

## version-N.scene.json

```json
{
  "schema_version": 1,
  "name": "Version 1 - converging streams",
  "style_id": "S1",
  "canvas": {"width": 900, "height": 480},
  "fingerprint": {
    "flow_direction": "left-to-right",
    "panel_structure": "two-lanes",
    "focal_point": "fusion",
    "detail_strategy": "inline"
  },
  "groups": [
    {"id": "main", "label": "a  Prediction", "x": 20, "y": 20, "w": 860, "h": 440, "fill": "#F6F8FA"}
  ],
  "nodes": [
    {"id": "v_control", "semantic_id": "control", "label": "Control expression", "group": "main", "x": 40, "y": 150, "w": 190, "h": 65, "shape": "rect", "fill": "#E3EFF6", "font_size": 16},
    {"id": "v_encoder", "semantic_id": "encoder", "label": "Cell encoder", "group": "main", "x": 330, "y": 150, "w": 170, "h": 65, "shape": "roundrect", "fill": "#D9EAE8", "font_size": 16}
  ],
  "edges": [
    {"id": "v_encode", "semantic_id": "encode", "source": "v_control", "target": "v_encoder", "kind": "data", "points": [], "exit": [1, 0.5], "entry": [0, 0.5]}
  ]
}
```

Node coordinates are **absolute canvas coordinates even when grouped**. The compiler translates them into parent-relative geometry. Groups may not nest. Names/IDs must be unique and must not use reserved `0` or `1`. Supported shapes: `rect`, `roundrect`, `ellipse`, `text`, `cylinder`, `triangle`, `hexagon`. Optional node `rotation`, `stroke`, `font_color`, `bold`; optional `label_override_reason` for shortened semantic labels. Semantic labels must equal the contract unless a concrete override reason is provided. Node defaults: font 16 px, line 1 px. Group headings use 17 px; override with `font_size` if needed.

Decorative scene-only nodes use `role: decoration` and omit `semantic_id`. They are limited to non-claim marks such as panel labels, cell outlines, token rectangles and legends; scientific entities need a canonical ID. A matrix should be native rectangles, with its semantic ID assigned to a labeled container or its explanatory label. Don't store experimental values in decorative cells.

All canonical scientific edges must be represented using `semantic_id`, matching canonical endpoint IDs and kind. Optional `label`, `points` (`[[x,y],...]`), `exit`, `entry`, `dashed`, `stroke`. Points are absolute canvas coordinates. The compiler uses orthogonal connectors unless `routing: straight` is requested. `kind: callout` needs no semantic ID and draws a dashed non-arrow leader. Never encode stop-gradient as merely an unlabeled decorative slash; label it or include it in the contract.

## comparison.json

```json
{
  "selected_styles": ["S1", "S3", "FREE-central-story"],
  "selection_file": "style-selection.md",
  "semantic_contract": "paper-contract.json"
}
```

Exactly three scenes are checked. `style_id` is a free string: use a descriptive `FREE-...` name for the independently designed third version. Fingerprints describe layout choices for comparison, with no numerical diversity requirement. The compare command verifies IDs/kinds/labels, native-only shapes, canvas containment, approximate text fit and declared diversity. It does **not** prove visual quality or manuscript truth.
