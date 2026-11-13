---
name: geometric-logo-blueprint
description: Design, revise, or audit a logo mark on a geometric blueprint (construction grid, circles, triangles, halved angles) that anyone can rebuild without measuring. Use when asked to create a logo, revise a logomark, build a logo construction or grid diagram, make a mark crop-safe for avatars or app icons, produce positive and reversed colourways, score logo options for scalability down to favicon size, or check whether a logo can be redrawn from scratch. Triggers - "logo blueprint", "logo grid", "construction lines", "geometric mark", "rebuild this logo", "avatar crop", "favicon test", "reverse the logo colours".
---

# Geometric Logo Blueprint

A blueprint is a short list of instructions that rebuilds a logo exactly, from a blank canvas, without measuring or tracing the old file. If you can't write that list, you have decoration, not a system.

Inspired by logo designers who build marks from simple geometry: James Barnard's writing on logo blueprints, and the constructed identities of Chermayeff & Geismar & Haviv and Bruce Blackburn. Notes in `references/inspirations.md`.

## Ten rules

1. **Concept first, geometry last.** Know what each element means before you draw a circle. The grid tidies the design in the last 10% of the work.
2. **The rebuild test defines a blueprint.** Can someone recreate the mark exactly from the diagram and a few plain instructions?
3. **Few primitives.** One base shape family: a circle, an equilateral triangle, or a square grid. Add only what the mark needs.
4. **Not every mark suits a blueprint.** Calligraphic or heavily optical marks don't reduce to clean geometry. Don't force them.
5. **Never retrofit.** Golden-ratio circles drawn over a finished logo look aligned and prove nothing.
6. **Optical correction is a choice, not a nudge.** The eye reads a slightly modified circle as rounder than a true one. If you correct, write the correction into the system as a number. Otherwise make an optical mark and make no blueprint claim.
7. **Stop early.** A grid can strangle a design. Stop adding construction once the mark is reproducible.
8. **Simple takes the most effort.** Expect many rounds.
9. **Ship the diagram.** A schematic proves accuracy and consistency.
10. **Check against the source.** Copies of famous logo diagrams online often differ from the originals.

If a construction needs many measurements, it isn't simple enough. Simplify the mark or the system.

## Procedure

**1. Read the concept.** List what each element means. If a previous version exists, inspect the real file data (sizes, stroke widths, arc angles, centres) and reverse-engineer its system first. In Figma, use the MCP (`get_metadata`) or a CLI that can run plugin code. Fit circle centres and radii from path endpoints. Note what is arbitrary: off-module sizes, uneven gaps, mass that is off-centre.

**2. Fix the frame and its crops.**
- Canvas size (for example 512) and every crop the mark must survive: circle avatar (inscribed circle, r = S/2), rounded app icon, square favicon.
- **Safe circle** at 7/8 of the crop radius (224 on 512). All ink stays inside it. Centre the construction on the crop centre, not on the old bounding box.
- If a brief mentions the mark being cut by a crop, decide out loud: *crop-safe* (nothing clipped, the default) or *deliberate bleed* (one element intentionally runs off the edge at a documented point).

**3. Pick a module and one primitive.**
- Unit `u` that divides the canvas (8px on 512). Stroke weight a clean multiple (48 = 6u). Grid every 4u.
- Prefer relations a person can rebuild with compass and ruler: Pythagorean triples (3:4:5), radius equals half the canvas, height equals the radius.
- Angles by halving only (90°, 45°, 22.5°) or by hexagon (60°, 30°).

**4. Place every element by a rule.** Each one gets a one-line instruction. Example: "the stem stands on the circle's west point and rises until its cap touches the safe circle: a 3:4:5 triangle." Use one stroke weight, one cap style and one gap rule throughout. Make dot diameter equal the stroke weight.

**5. Check mass and optics.** Compare geometric centre and centroid numerically. Keep intentional weight contrasts and write them down. Any correction lives in the system as a number, never as a nudge.

**6. Run the rebuild test.** Write the instruction list in 8 lines or fewer. Rebuild the mark from the list alone, ideally in code (SVG or Figma plugin script), and diff it against the drawing. Anything you had to measure needs a better rule.

**7. Produce colourways.**
- A reversal swaps background and foreground exactly. Keep the geometry identical. Light on dark reads slightly heavier. If you compensate, ship it as a named small-size variant and leave the master alone.
- Check the contrast of the pair (aim for 4.5:1 or more).
- One flat colour per version. No gradients in the master.

**8. Score for scalability.** See the next section. Every candidate looks fine at 512.

**9. Deliver.**
- The master in positive and reversed.
- The blueprint diagram.
- The crop test and the favicon crop.
- The instruction list.
- The scorecard.
- A short rationale saying what changed and why.

In Figma, add new frames beside the original and never overwrite it.

## Scalability scorecard

Export every candidate at 64, 32 and 16px from the real renderer (Figma `exportAsync`, or the browser). Don't judge from a downscaled screenshot.

Measure:
- **Shapes kept:** threshold each render at 50% between background and ink, then count connected shapes. Compare with the count at 512. More shapes means fragments; fewer means gaps closed.
- **Smallest gap at 16px:** visual gap in px at 512 × 16 / 512. Below about 1.3px, gaps close.
- **Crop:** the farthest ink from the centre must sit at or inside the safe circle.

Score each criterion out of 5, weight it, and show your working:

| Criterion | Weight |
| --- | --- |
| Favicon read: does the silhouette still say what it means at 16px? | ×3 |
| Shapes and gaps survive at 32 and 16px | ×2 |
| Crop safety | ×2 |
| Brief fit: keeps the elements that carry meaning | ×2 |
| Rebuild: short, measurement-free instructions | ×1 |

The highest scalability total isn't automatically the pick. A version that wins on size by dropping the elements that carry the brand's meaning has not survived. Say so in the recommendation.

**Favicon crop.** The safe circle exists for circular crops. A square favicon can drop it: re-crop the viewBox to the ink bounds plus a small margin, so the mark draws larger in the same 16px.

**Breaks and gaps.** Put a break where it doesn't change which letter or shape you read. A gap in the wrong place can turn one letterform into another.

## Blueprint diagram conventions

- Mark at 25 to 30% opacity under the construction.
- One accent colour for construction lines. Grid in a muted tint at about 18% opacity.
- Draw:
  - the crop circle (solid) and the safe circle (dashed);
  - each primitive circle, with a solid centreline and dashed stroke edges;
  - the compass rays you used;
  - the key triangle or ratio, with numeric labels;
  - guides for glyph extents.
- Label ratios and rules, not every dimension.

## Motion explainer (optional)

To show the process, animate it in this order, one step at a time:

1. Frame (crop and safe circle)
2. Grid
3. Primitive
4. Angles
5. Rule triangle
6. Elements
7. Scaffolding removed
8. Crop test
9. Scale test

Build each frame as SVG with partial geometry: arcs grow by angle and lines by length. Avoid dash tricks, which some renderers ignore. Render the frames, then assemble a GIF with a hold on each step's last frame.

## Anti-patterns

- Retrofitted golden-ratio circles.
- A construction that needs a ruler to read.
- Uneven gaps with no rule behind them.
- Mass centred on the bounding box while the crop is centred somewhere else.
- Elements touching the crop edge by accident.
- Undocumented optical tweaks.
- Editing the original master in place.
- Judging scalability at 512px.
