"""Blueprint kit: build a logo mark from rules, then measure it.

Part of the geometric-logo-blueprint skill. Needs shapely, numpy and pillow.

Canvas 512, crop circle r256, safe circle r224 (7/8) at (256,256). Angles in screen degrees:
0 = east, 90 = south, 180 = west, 270 = north.

    python3 blueprint_kit.py --demo out/      # demo mark: master, favicon, 24px icon, measured contact sheet
"""
import math
from collections import deque

import numpy as np
from PIL import Image, ImageDraw
from shapely import affinity
from shapely.geometry import LineString, MultiPolygon, Point, Polygon, box
from shapely.ops import unary_union

C = 256.0
SAFE = 224.0
INK = "#1D2B3A"
PAPER = "#F4EFE6"


def P(r, a, cx=C, cy=C):
    t = math.radians(a)
    return (cx + r * math.cos(t), cy + r * math.sin(t))


def arc_pts(cx, cy, r, a0, a1, step=0.5):
    n = max(2, int(abs(a1 - a0) / step) + 1)
    return [P(r, a0 + (a1 - a0) * i / (n - 1), cx, cy) for i in range(n)]


def arc(cx, cy, r, a0, a1, w, cap="round"):
    cs = {"round": "round", "flat": "flat"}[cap]
    return LineString(arc_pts(cx, cy, r, a0, a1)).buffer(w / 2, cap_style=cs, join_style="round", quad_segs=32)


def line(pts, w, cap="round", join="round"):
    return LineString(pts).buffer(w / 2, cap_style=cap, join_style=join, quad_segs=32, mitre_limit=10)


def dot(x, y, r):
    return Point(x, y).buffer(r, quad_segs=64)


def rrect(x0, y0, x1, y1, r):
    return box(x0 + r, y0 + r, x1 - r, y1 - r).buffer(r, quad_segs=32) if r else box(x0, y0, x1, y1)


def union(*g):
    return unary_union([x for x in g if x is not None])


def polys(g):
    if g.is_empty:
        return []
    return list(g.geoms) if isinstance(g, MultiPolygon) else [g]


def max_radius(g):
    return max(math.hypot(x - C, y - C) for p in polys(g) for x, y in p.exterior.coords)


def centre_mass(g, target=(C, C - 4)):
    """Translate so the area centroid sits on the optical centre (4px above geometric centre)."""
    c = g.centroid
    return affinity.translate(g, target[0] - c.x, target[1] - c.y)


def fit_safe(g):
    """Scale about the crop centre so the farthest ink sits on the safe circle (only ever shrinks)."""
    m = max_radius(g)
    if m <= SAFE:
        return g, 1.0
    s = SAFE / m
    return affinity.scale(g, s, s, origin=(C, C)), s


# ---------- SVG ----------

def _ring(coords):
    pts = list(coords)
    if pts[0] == pts[-1]:
        pts = pts[:-1]
    s = "M%.2f %.2f" % pts[0] + "".join("L%.2f %.2f" % p for p in pts[1:]) + "Z"
    return s.replace(".00", "")


def path_d(g, tol=0.04):
    g = g.simplify(tol, preserve_topology=True)
    out = []
    for p in polys(g):
        out.append(_ring(p.exterior.coords))
        out += [_ring(i.coords) for i in p.interiors]
    return "".join(out)


def svg(g, fg="#000000", bg=None, title="Mark", vb=(0, 0, 512, 512), size=None):
    w = size or vb[2]
    h = size or vb[3]
    rect = f'<rect x="{vb[0]}" y="{vb[1]}" width="{vb[2]}" height="{vb[3]}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" role="img" viewBox="{" ".join("%g" % v for v in vb)}" '
            f'width="{w:g}" height="{h:g}"><title>{title}</title>{rect}'
            f'<path fill="{fg}" fill-rule="evenodd" d="{path_d(g)}"/></svg>')


def tight_vb(g, margin=0.06):
    x0, y0, x1, y1 = g.bounds
    s = max(x1 - x0, y1 - y0) * (1 + 2 * margin)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    return (round(cx - s / 2, 2), round(cy - s / 2, 2), round(s, 2), round(s, 2))


def simple_icon(g, title):
    """Simple Icons convention: 24x24 viewBox, one path, touches two sides, centred, no fill attr."""
    x0, y0, x1, y1 = g.bounds
    s = 24 / max(x1 - x0, y1 - y0)
    h = affinity.scale(g, s, s, origin=(0, 0))
    hx0, hy0, hx1, hy1 = h.bounds
    h = affinity.translate(h, (24 - (hx1 - hx0)) / 2 - hx0, (24 - (hy1 - hy0)) / 2 - hy0)
    d = path_d(h, tol=0.004)
    d = "".join(ch for ch in d)
    import re
    d = re.sub(r"(\d+\.\d{3})\d+", r"\1", d)
    return f'<svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>{title}</title><path d="{d}"/></svg>'


# ---------- raster ----------

def raster(g, size, vb=(0, 0, 512, 512), ss=8):
    """Area-coverage render (supersample then box-filter), ink=1.0."""
    S = size * ss
    im = Image.new("L", (S, S), 0)
    dr = ImageDraw.Draw(im)
    k = S / vb[2]

    def tr(coords):
        return [((x - vb[0]) * k, (y - vb[1]) * k) for x, y in coords]

    for p in polys(g):
        dr.polygon(tr(p.exterior.coords), fill=255)
        for i in p.interiors:
            dr.polygon(tr(i.coords), fill=0)
    return np.asarray(im.resize((size, size), Image.BOX), dtype=np.float32) / 255.0


def _label(mask):
    h, w = mask.shape
    seen = np.zeros_like(mask, dtype=bool)
    n = 0
    for y in range(h):
        for x in range(w):
            if mask[y, x] and not seen[y, x]:
                n += 1
                q = deque([(y, x)])
                seen[y, x] = True
                while q:
                    cy, cx = q.popleft()
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not seen[ny, nx]:
                            seen[ny, nx] = True
                            q.append((ny, nx))
    return n


def topology(a):
    """(ink shapes, enclosed background holes) at a 50% threshold."""
    ink = a >= 0.5
    bg = ~ink
    pad = np.pad(bg, 1, constant_values=True)
    return _label(ink), _label(pad) - 1


def min_gap(g):
    ps = polys(g)
    d = [ps[i].distance(ps[j]) for i in range(len(ps)) for j in range(i + 1, len(ps))]
    return min(d) if d else None


def measure(g):
    fav = tight_vb(g)
    t512 = topology(raster(g, 256, ss=2))
    out = {
        "max_r": round(max_radius(g), 1),
        "crop_ok": max_radius(g) <= SAFE + 0.5,
        "centroid": (round(g.centroid.x, 1), round(g.centroid.y, 1)),
        "ink_pct": round(g.area / (512 * 512) * 100, 1),
        "parts": len(polys(g)),
        "min_gap": None if min_gap(g) is None else round(min_gap(g), 1),
        "topo512": t512,
        "fav_vb": fav,
        "fav_scale": round(512 / fav[2], 2),
    }
    for s in (32, 16):
        out[f"topo{s}"] = topology(raster(g, s))
        out[f"topo{s}_fav"] = topology(raster(g, s, vb=fav))
    return out


def stem_top(x, w, r_safe=SAFE):
    """Highest y where a round-capped vertical stroke at x keeps its cap inside the safe circle."""
    reach = r_safe - w / 2
    return C - math.sqrt(max(reach ** 2 - (x - C) ** 2, 0))


def gap_angle(R, gap, w):
    """Angle between two round-capped arc ends on radius R that leaves a visual gap `gap`."""
    return math.degrees(2 * math.asin((w + gap) / (2 * R)))


# ---------------- demo ----------------

def demo_mark(w=48, R=120, gap_deg=45):
    """A generic demo mark: open ring, centre dot, and a 3:4:5 tail whose cap meets the safe circle."""
    tail0 = P(R, math.degrees(math.atan2(-160, -120)))
    return union(
        arc(C, C, R, 0, 360 - gap_deg, w),
        line([tail0, (136, 96)], w),
        dot(C, C, w / 2),
    )


def _demo(out):
    import os
    os.makedirs(out, exist_ok=True)
    variants = {
        "stroke 48, gap 45": demo_mark(w=48),
        "stroke 64, gap 45": demo_mark(w=64),
        "stroke 48, gap 28": demo_mark(w=48, gap_deg=28),
        "stroke 32, gap 45": demo_mark(w=32),
    }
    tiles = []
    for name, g in variants.items():
        g = centre_mass(g)
        g, _ = fit_safe(g)
        m = measure(g)
        slug = name.replace(", ", "-").replace(" ", "")
        open(f"{out}/{slug}.svg", "w").write(svg(g, INK, PAPER, f"Demo {name}"))
        open(f"{out}/{slug}-favicon.svg", "w").write(svg(g, PAPER, INK, f"Demo {name}", vb=m["fav_vb"]))
        open(f"{out}/{slug}-24.svg", "w").write(simple_icon(g, f"Demo {name}"))
        ok = m["topo16_fav"] == m["topo512"]
        print(f"{name:18s} shapes512={m['topo512']} shapes32={m['topo32_fav']} shapes16={m['topo16_fav']} "
              f"{'holds' if ok else 'CHANGES'}  max_r={m['max_r']} crop_ok={m['crop_ok']}")
        tiles.append((name, g, m, ok))
    W, H = 300, 330
    sheet = Image.new("RGB", (W * len(tiles), H), PAPER)
    d = ImageDraw.Draw(sheet)
    ink = tuple(int(INK[i:i + 2], 16) for i in (1, 3, 5))
    paper = tuple(int(PAPER[i:i + 2], 16) for i in (1, 3, 5))
    for k, (name, g, m, ok) in enumerate(tiles):
        def img(a):
            a = a[..., None]
            return Image.fromarray((np.array(paper) * (1 - a) + np.array(ink) * a).astype(np.uint8))
        sheet.paste(img(raster(g, 200)), (k * W + 50, 20))
        for j, s in enumerate((32, 16)):
            im = img(raster(g, s, vb=m["fav_vb"])).resize((s * (3 if s == 32 else 6),) * 2, Image.NEAREST)
            sheet.paste(im, (k * W + 50 + j * 104, 228))
        d.text((k * W + 50, 4), f"{name}: 16px {'holds' if ok else 'changes'} {m['topo16_fav']}", fill=ink)
    sheet.save(f"{out}/demo-sheet.png")
    print("wrote", out)


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3 and sys.argv[1] == "--demo":
        _demo(sys.argv[2])
    else:
        print(__doc__)
