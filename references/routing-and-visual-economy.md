# Routing, related elements and concise labels

Use these suggestions to make the scientific relationships easy to see. Adapt them to the paper and its reference figures; they are not a fixed layout or a quota for arrows, colors or text.

## Make paths readable before styling

Arrange the major stages along a clear reading direction, then leave corridors for branches and auxiliary paths. Align related inputs and outputs; direct short connections or a small number of aligned orthogonal segments usually read better than tightly nested elbows. Curves can work when they clarify the route.

Attach each connector to a visible source and destination, preferably using native object IDs and explicit entry/exit anchors. A line beginning in empty space near a cell or graph can look detached even if its intended source is obvious to the author. In compact compositions, route from a group's boundary or a labeled output instead of threading through its internal marks.

Separate routes that carry different signals. Parallel paths benefit from distinct, consistently spaced lanes and separate module ports. When one signal branches, make the shared source and split explicit. When streams combine, show the actual operator or an unambiguous merge. Do not merge unrelated signals into a tidy-looking shared trunk. A crossing alone does not indicate a connection.

Keep arrows clear of text, icons and unrelated modules. If routes become tangled, move or resize modules, swap the placement of supporting panels, or repeat a clearly identified input glyph where it represents the same input. Small duplication can be clearer than a long crossing, provided it does not imply a new computation. Route training-only updates or feedback around the main path when useful. Use restrained line styles and a short key only when they distinguish real roles.

For example, if global views feed both Student and Teacher while local views feed Student only, give the global split a visible origin, keep the local-to-Student route separate, and place the Student-to-Teacher update away from both. No loose colored line should appear to create a new input. This is a routing example, not a prescribed architecture.

## Build a family of visual objects

A representation may read better as a small stack of vectors than one isolated strip. Related cells, graph views or token groups can repeat a common silhouette while varying a relevant feature: selected targets, mask marks, front/back layers, or high/low categories supported by the method. Reuse editable groups so proportions and spacing stay coherent.

Consider restrained hue, tint, outline or opacity changes. Lighter rear layers can suggest a collection while a stronger front layer directs attention; a consistent accent can link a selected node to its representation. Keep critical labels and connectors high-contrast. Use outline or shape cues as well when color/opacity alone becomes ambiguous, and inspect the exported figure on its actual background. Do not imply measured expression, confidence, sample counts or probabilities through decorative color, transparency or repetition.

These transformations are often best done with native draw.io objects. For generated illustrations, make a coherent set of simple, formal schematic assets when useful; keep text and scientific arrows separate. An imported bitmap remains a bitmap even when duplicated or made translucent.

## Keep the picture concise

Prefer short noun labels for objects and brief action/operator labels where needed. Place labels close to what they describe; use one compact legend for shared symbols when that saves repetition. Preserve distinctions such as train versus inference, a true fusion operation, or a necessary condition.

Move prose explanations, detailed loss definitions, configuration qualifiers and repeated caveats to the figure caption or companion notes when readers can still interpret the panel correctly. Necessary qualifications can remain as concise labels. Do not reduce font size to fit an entire paragraph into an overview. Aim for visual explanation rather than a page of annotated boxes, without imposing a word-count ceiling.

## Review the visible result

Trace each major path on the render: can a reader identify its start, follow every turn and name its destination without guessing? Check near-parallel segments, crossings, arrowheads, input ports and label clearance at final size. Inspect repeated groups and translucent layers for legibility after export. If the explanation still depends on several sentences inside the panel, consider whether grouping or a clearer visual correspondence would do the work.

A correct adjacency list does not prove that the visible arrows are clear. Recheck the rendered region after rerouting, and do not report existing figures fixed merely because this guidance was updated.
