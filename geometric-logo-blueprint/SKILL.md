---
name: geometric-logo-blueprint
description: Design, revise, or audit a logo mark on a geometric blueprint (construction grid, circles, triangles, halved angles) that anyone can rebuild without measuring, then prove it with measured tests and a variation tournament. Use when asked to create a logo, revise a logomark, explore logo variations, build a logo construction or grid diagram, make a mark crop-safe for avatars or app icons, produce positive and reversed colourways, score logo options for scalability down to favicon size, export a single-path 24px icon, or check whether a logo can be redrawn from scratch. Triggers - "logo blueprint", "logo grid", "construction lines", "geometric mark", "rebuild this logo", "logo variations", "avatar crop", "favicon test", "reverse the logo colours", "simple icon".
---

# Geometric Logo Blueprint

A blueprint is a short list of instructions that rebuilds a logo exactly, from a blank canvas, without measuring or tracing the old file. If you can't write that list, you have decoration, not a system. The deliverable is a specification you can describe, defend and reproduce, not a picture.

Inspired by logo designers who build marks from simple geometry: James Barnard's writing on logo blueprints, and the constructed identities of Chermayeff & Geismar & Haviv and Bruce Blackburn. Version 2 adds practice from three open projects:
- Kaan Kızıltuğ's open-source logo-design skill (testing battery, optical corrections, critique);
- the Simple Icons project's icon conventions (single-path monochrome export);
- Inkloom's published account of building marks under construction rules.

Notes in `references/inspirations.md`.

## Ten rules

1. **Concept first, geometry last.** Know what each element means before you draw a circle. The grid tidies the design in the last 10% of the work.
2. **The rebuild test defines a blueprint.** Can someone recreate the mark exactly from the diagram and a few plain instructions?
3. **Few primitives, shared.** One base shape family, with shared radii, tangent junctions and one terminal style.
4. **Not every mark suits a blueprint.** Calligraphic or heavily optical marks don't reduce to clean geometry. Don't force them.
5. **Never retrofit.** Golden-ratio circles drawn over a finished logo look aligned and prove nothing.
6. **Optical correction is a number, not a nudge.** Write every correction into the rules (see step 5).
7. **Stop early.** Stop adding construction once the mark is reproducible.
8. **Explore wide, then narrow.** Many cheap one-line concepts, a few builds, one final. Keep every iteration.
9. **Measure, don't admire.** Every candidate looks fine at 512. Judge at 16px from real renders.
10. **Ship the specification.** The rule list, the diagram and the test results.

If a construction needs many measurements, it isn't simple enough. Simplify the mark or the system.

## Procedure

**1. Brief to constraints.** List what each element means. Turn the brief's adjectives, audience and competitors into concrete parameters before drawing:
- stroke weight;
- width and proportion;
- geometry family;
- counter shape;
- terminal style (round or flat);
- which mark types fit.

Then list the category's clichés (for a dev tool: brackets, chevrons, terminal windows, cursors). Use a cliché only with a fresh form.

If a previous version exists, inspect the real file data (sizes, stroke widths, arc angles, centres) and reverse-engineer its system first. Note what is arbitrary: off-module sizes, uneven gaps, mass that sits off-centre.

**2. Fix the frame and its crops.**
- Canvas size (512) and every crop the mark must survive: circle avatar (r = S/2), rounded app icon, square favicon.
- **Safe circle** at 7/8 of the crop radius (224 on 512). All ink stays inside it.
- **What sits on the crop centre.** If the mark is built on a circle, put that circle's centre on the crop centre. Two near-concentric circles that miss by a few pixels read as a mistake, and the eye forgives uneven weight sooner. Centre on the area centroid only when nothing in the mark echoes the crop.
- If a brief mentions the mark being cut by a crop, decide out loud: *crop-safe* (the default) or *deliberate bleed* (one element runs off the edge at a documented point).

**3. Pick a module and one primitive.**
- Unit `u` that divides the canvas (8 on 512). Stroke weight a clean multiple (48 = 6u).
- Prefer relations a person can rebuild with compass and ruler: Pythagorean triples (3:4:5), radius equals half the canvas.
- Angles by halving (90°, 45°, 22.5°) or by hexagon (60°, 30°). No near-miss angles.

**4. Place every element by a rule.** Each one gets a one-line instruction, for example: "the stem stands on the circle's west point and rises until its cap touches the safe circle."
- One stroke weight, **measured square to the stroke**. A 45° arm cut 48 wide horizontally is only 34 thick.
- One cap and join style for every element. Sharp corners beside round caps read as two systems.
- One gap rule, for example "every gap equals one stroke", or for a broken ring "divide it into equal sectors and ink alternate ones".
- Dot diameter equals the stroke.

**5. Optics, as numbers.**
- **Mass:** for marks with no circle echoing the crop, put the area centroid on the optical centre (about 1% above the geometric centre), not the bounding box. For ring-based marks see step 2: the ring wins, and open space on the light side balances the weight.
- **Overshoot:** round forms 1 to 3% of height; points 3 to 6%. A round dot beside straight strokes needs about +4% diameter.
- **Irradiation:** light-on-dark reads heavier. Thin the reversed file 2 to 5% and name it as its own file.
- **Lettering:** horizontals 5 to 10% thinner than verticals.

Write each correction into the rule list.

**6. Run the rebuild test.** Write the rules in 8 lines or fewer. Rebuild the mark from the list alone, in code, and diff it against the drawing. Anything you had to measure needs a better rule.

**7. Explore, then run a tournament.**
- Write 12 to 15 one-sentence concepts across at least three mark types. A good spread:
  - refinements of the current mark;
  - hybrids that reinterpret one element;
  - fresh directions (letterform, ligature, container, negative space, bitmap).
- Build them all from rules.
- Apply the **gates**, then score the survivors (see the scorecard).
- Shortlist **three finalists from different directions**, not the top three of one family.
- Reiterate each finalist to fix what its tests exposed, then reiterate the winner once more into the final.
- Keep every round's files. A reiteration can make a mark worse. Say so and keep the earlier version.
- **Show every round where the decision-maker works** (a Figma page, a shared board), one labelled frame per version with its score, before asking anyone to choose. Scores computed out of sight feel unverifiable.
- Let the person pick a shortlist by eye, then revise each pick with its blueprint. Scores inform the choice. They don't make it.

**8. Test battery.** Use real renders, never a downscaled screenshot.
- **Size:** 16, 20, 24, 32, 48, 64, 128, 256px.
- **Shape count:** threshold at 50% and count ink shapes and enclosed holes at 512, 32 and 16px. If the 16px count differs from the 512px count, gaps have closed or the mark has fragmented.
- **Smallest gap:** at least 1/32 of the mark's width. At 16px, below about 1.3px, gaps close.
- **Letter test:** every letter still reads as itself at first glance. Re-run it after any change to weight, ring size or breaks. A heavier stroke can drown an ascender, and a new break can turn a b into a play button.
- **Unintended readings:** mirror, rotate 180°, view tiny, blur (squint).
- **Colour:** one-colour black and white, reversed, brand colour, a photo, a pattern.
- **Shelf and familiarity:** put the mark beside 4 to 6 marks from its category that use the same device. If it feels familiar and isn't yours, it's someone else's.
- **Junctions:** zoom into every place strokes meet. Look for notches, slivers and lumps.
- **Context composites:** put the mark in the real places it will live, using a screenshot of the person's own Dock, home screen or tab bar at native resolution, and compare it with its neighbours.
- **Measure honestly:** sample pixel centres when rasterising. Polygon fills that include edge pixels add a false grey border and inflate blur numbers.

**9. Colourways.** A reversal swaps background and foreground and keeps the geometry, apart from the thinned reversed file. Check contrast (aim for 4.5:1 or more). One flat colour per version, no gradients in the master.
- **One accent, one meaning.** If a second colour is used, give it to the single element that carries a meaning (for example, the cursor or prompt that says "code"). A graphic accent needs at least 3:1 against its background, so use it only on grounds where it reaches that.

**10. Production files.**
- Outlines, not strokes. One `<path>`, a `<title>`, coordinates to 2 decimals.
- Arcs written as arcs. A mark built from primitives needs tens of anchors, not hundreds.
- Overlapping subpaths with the same winding render as a union (nonzero fill). That is fine for screen and print. Unite them in a vector editor for cutters and embroidery.
- **24px icon export (Simple Icons convention):**
  - 24×24 viewBox, monochrome, one path;
  - touches at least two sides and is centred;
  - 3-decimal precision;
  - no fill, width or height attributes;
  - the brand colour recorded as a 6-digit hex.
  - Where a mono version needs separated segments, use gaps of about 0.5 on 24 (1/48).
- **Small-size cut:** if the master's details merge at 16px, draw a separate 16px version. Drop the smallest element and thicken the stroke, then use it only at that size. Don't weaken the master to fit.
- **Pixel-grid construction** for marks that must be razor-sharp: use cells of canvas/16 (32 on 512), so one cell is exactly 1px at 16px and 2px at 32px. Place on whole cells only. Snap the vertical stems of curved marks to a 16-unit grid so they stay crisp at 32 and 64px.
- **Favicon crop:** square favicons don't need the safe circle. Re-crop the viewBox to the ink bounds plus a 6% margin so the mark draws larger.
- **Clear space** comes from the mark's own geometry (for example, one stroke or one dot diameter), not a fixed number.

**11. Checkpoint before the kit.** Show the concept sheet and your recommendation, then wait. Build lockups, icon sets and guidelines only for the direction the person picks.

**12. Deliver.**
- The master in positive, reversed (thinned) and one-colour versions.
- The blueprint diagram.
- The crop test and the favicon crop.
- The 24px single-path icon.
- The rule list.
- The scorecard with measurements.
- A short rationale that says what changed and why.

In Figma, add new frames beside the original and never overwrite it.

## Scorecard

**Gates first.** Failing either one rules a candidate out, whatever its total:
- **Crop:** the farthest ink sits at or inside the safe circle.
- **Letter test:** the intended letters still read.

**Then score out of 5, weight it, and show your working (total /50):**

| Criterion | Weight |
| --- | --- |
| Favicon read: does the silhouette still say what it means at 16px? | ×3 |
| Shapes and gaps: measured shape counts hold at 32 and 16px; smallest gap | ×2 |
| Brief fit: keeps the elements that carry meaning | ×2 |
| Distinction: shelf and familiarity tests | ×2 |
| Craft and rebuild: one weight, one terminal, optics as numbers, short rules | ×1 |

The highest total isn't automatically the pick. A version that wins on size by dropping the elements that carry the brand's meaning has not survived. Say so, and name it as the runner-up.

**Breaks and gaps.** Put a break where it doesn't change which letter or shape you read. Test every new break with the letter test and the unintended-readings test.

## Tools

`scripts/blueprint_kit.py` (needs `shapely`, `numpy` and `pillow`) covers:
- primitives: round-capped arcs, lines and dots;
- placement: mass centring and safe-circle fit;
- SVG output: master and favicon crop, plus the 24px Simple Icons export;
- measurement: an area-coverage rasteriser and the shape and hole count at any size.

Run `python3 scripts/blueprint_kit.py --demo out/` to see it on a demo mark.

## Blueprint diagram conventions

- Mark at 25 to 30% opacity under the construction.
- One accent colour for construction lines. Grid in a muted tint at about 18% opacity.
- Draw:
  - the crop circle (solid) and the safe circle (dashed);
  - each primitive circle, with a solid centreline and dashed stroke edges;
  - the compass rays you used;
  - the key triangle or ratio, with numeric labels.
- Label ratios and rules, not every dimension.

## Motion explainer (optional)

Animate one step at a time:

1. Frame (crop and safe circle)
2. Grid
3. Primitive
4. Angles
5. Rule triangle
6. Elements
7. Scaffolding removed
8. Crop test
9. Scale test

Build each frame as SVG with partial geometry: arcs grow by angle and lines by length. Avoid dash tricks, which some renderers ignore. Assemble a GIF with a hold on each step's last frame.

## Anti-patterns

- Retrofitted golden-ratio circles.
- Diagonal strokes cut to the horizontal width, so they read thinner.
- Sharp corners mixed with round caps.
- Uneven gaps with no rule behind them.
- Mass centred on the bounding box while the crop is centred somewhere else.
- Elements touching the crop edge by accident.
- Undocumented optical tweaks.
- Hundreds of anchors in a mark made of circles and lines.
- A ring that almost, but not quite, shares the crop's centre.
- Scoring versions the decision-maker can't see.
- Shortlisting three versions of the same idea.
- Overwriting iterations, or editing the original master in place.
- Judging scalability at 512px.
- Claiming a test you didn't run, or trademark clearance you can't give. Recommend a professional search.
