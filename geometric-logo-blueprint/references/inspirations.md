# Inspirations and references


Reading notes that shaped this skill. Primary inspiration: James Barnard, "A Blueprint for a Logo". Paraphrased; brand names are used for commentary only.
URL: https://barnard.co/read-me-blog/a-blueprint-for-a-logo
Format: short essay; each reconstruction is a Vimeo video (e.g. vimeo.com/533514611 NatWest/Mitsubishi, vimeo.com/533423478 McDonald's). The videos hold the actual construction steps; the text holds the principles. Paraphrased below; quotes kept short.

## Thesis
A logo blueprint = a schematic (brand-guideline style) from which, with simple instructions, someone can rebuild the exact logo. The test: "Can you recreate the logo, exactly, from scratch without the ability to measure, or trace over your old design?"

## Examples
| Logo | Base | Result |
| --- | --- | --- |
| NatWest | equilateral triangle only | supremely accurate |
| Mitsubishi | equilateral triangle only (HSBC, Google Drive similar) | accurate |
| McDonald's | square grid ("design system" found online) + four ellipses for the varying stroke widths at the top of the M | accurate |
| Adidas | equilateral triangle; 13 triangles to govern bar ratio/spacing | didn't quite work; bar heights unresolved (author's version in pink) |
| Google G | apparently a circle; it isn't — tail thinner than the other side (Gestalt correction) | author couldn't |
| US Bicentennial (Bruce Blackburn, 1976; also co-designed NASA "worm") | star + rounded corners | author's rebuild from an online copy didn't match original plans (CG&H): corner radius starts just past the star's point |
| Nike, Apple | golden-ratio circle overlays (Apple: 1987 Identity Guidelines via arun.is) | fail — look aligned, need optical adjustment, no reference points |
| N64 | diamonds; colours = controller buttons | needs measurements to start |
| TikTok | circles | needs a specific measurement and complicated ratios |
| Nakatomi Plaza (Die Hard) | rebuilt for fun | real one is less uniform |

## Principles
- Blueprints only work for certain designs; grids can hamstring design and stifle creativity.
- Don't retrofit or apply imaginary lines after the fact; if the logo works without a grid, leave it.
- Grid = tidy-up in the last 10% (credited quote, Joshua Ariza). "There's such a thing as going too far."
- "It takes effort to appear effortless."
- Schematics show geometric harmony, prove accuracy and visual consistency, justify the fee.
- Optical adjustments that break geometry defeat the blueprint; yet the eye perceives a modified circle as more circular than a geometric one.
- Verify against original source material.
- Too bespoke for a grid: e.g. Coca-Cola.

## Cited resources
- CG&H, U.S. Bicentennial: https://www.cghnyc.com/work/project/u-s-bicentennial
- The Logo Creative, 20 famous logos in grid systems: grids optional; benefits organisation, balance/consistency, open margins ("Think Clean!"), scalability; some overlays stretched to fit golden ratio; optical adjustments beyond the grid sometimes necessary; grid studies by Florian Popescu — the more important the logo, the less random each pixel. Tools: Illustrator, Sketch, Figma.
- The Logo Smith, grids & pretty circles (2011)
- 99designs, do's and don'ts of logo grids
- The Logo Smith, Apple identity guidelines notebook (2018)

---

# Version 2 references

Three open projects shaped version 2. The notes below are paraphrased. Nothing is copied from them, and no logos from them are included here.

## logo-design skill, by Kaan Kızıltuğ (MIT)
https://github.com/kaankiziltug/logo-design-skill
- A logo identifies; it doesn't explain. One idea that you can say in one sentence.
- Explore across mark types. Write many one-line concepts, build only the strongest three, and pause at a checkpoint before building the full kit.
- List the category's clichés before drawing, and give any cliché you use a fresh form.
- Craft pass:
  - the letter test (does each letter still read as itself?);
  - junction checks;
  - a peer test against well-made marks;
  - a literalness check.
- Optical corrections with ranges:
  - overshoot of 1 to 3% for curves and more for points;
  - the bone effect on capsules;
  - irradiation (thin the reversed file 2 to 5%);
  - thinner horizontals;
  - the optical centre.
- Testing battery:
  - size ladder and 16px pixel test;
  - backgrounds, one-colour and greyscale;
  - squint, mirror and 180° rotation, which catch unintended readings;
  - realistic contexts;
  - a shelf test against competitors;
  - the familiarity test.
- Production: no live text, rasters or filters in masters; few anchors; arcs for circular geometry; expand strokes before delivery.
- Honesty: you can't give trademark clearance, so recommend a search, and don't claim tests you didn't run.

## Simple Icons
https://github.com/simple-icons/simple-icons (CONTRIBUTING.md)
- The icon convention: 24×24 viewBox, one monochrome path, no extra elements or attributes.
- The icon touches at least two sides of the box and is centred.
- Optimise to about 3-decimal precision, then check that nothing changed.
- Where colour separation is lost in mono, add gaps of about 0.5 on the 24 grid.
- Record the brand colour as a 6-digit hex, and prefer official sources.

## Inkloom
https://github.com/Inkloom-art/inkloom (source published for reading; all rights reserved)
- Turn the brand description into concrete constraints before drawing: stroke weight, width, geometry, counter shape, and which symbol families fit.
- Compose primitives under construction rules: shared radii, tangent junctions, consistent terminals.
- Use optical alignment rather than mathematical centring. Take clear-space ratios from the mark itself, and deliver the lockups a brand needs (horizontal, stacked, symbol alone).
- The output should be a specification you can describe and reproduce, not a bitmap.
- Don't claim a capability before it exists.
