# Luca Healthcare — Website (v2, light)

A light, editorial homepage for Luca Healthcare, inspired by the clean
cream-toned layout of owkin.com. Built as a dependency-free static site
(HTML + CSS + JS) — no build step.

The hero centerpiece is a custom **animated lung** (breathing motion, bronchial
airflow, AI scan nodes) — fitting Luca's respiratory / acoustic-AI work — in
place of a generic orb.

> The previous dark-themed version is preserved in `draft-1/`.

## Run locally

```bash
python3 -m http.server 8088   # then open http://localhost:8088
# or just double-click index.html
```

## Structure

```
index.html              # Full homepage + inline icon sprite + lung SVG
assets/css/main.css     # Light design system + all component styles
assets/js/main.js       # Sticky nav, mobile menu, scroll reveal, smooth scroll
draft-1/                # Earlier dark-themed version (reference)
```

## Notes

- This is a **bare design pass** — buttons/links are visual (in-page anchors),
  not wired to real endpoints yet.
- Light, warm palette; Luca cyan (`#009EDF`) as the single brand accent.
- Fonts: Inter (Google Fonts). Fully responsive; respects `prefers-reduced-motion`.
