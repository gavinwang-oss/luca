# Luca Healthcare — Website explorations

Design iterations for the Luca Healthcare homepage. Each version is a
self-contained, dependency-free static site (HTML + CSS + JS) — no build step.

## Drafts

| Folder | Description |
|--------|-------------|
| `draft-1/` | **Dark theme** — Owkin-structure redesign on Luca's navy + cyan, with an iridescent orb hero. |
| `draft-2/` | **Light theme** — warm cream, editorial hero, AI-forward narrative. Centerpiece is a photorealistic **AI-generated 3D lung image** + an animated SVG node overlay. |
| `draft-3/` | **Light theme** — identical layout to draft-2, but the centerpiece is a **fully custom Canvas animation**: procedural bronchial tree, airflow particles flowing through the airways, a drifting particle field, a pulsing node network, and breathing — all hand-coded and live. |

> **draft-2 vs draft-3** are the same page; only the hero centerpiece differs.
> draft-2 = photoreal-but-static image; draft-3 = stylized-but-truly-animated canvas.

## Run any draft locally

```bash
cd draft-3          # or draft-1 / draft-2
python3 -m http.server 8088   # then open http://localhost:8088
# or just double-click index.html
```

## Notes

- These are design passes — buttons/links are visual (in-page anchors), not wired
  to real endpoints.
- Fonts loaded from Google Fonts. Fully responsive; respects `prefers-reduced-motion`
  (draft-3's animation falls back to a single static frame).
