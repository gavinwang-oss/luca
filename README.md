# Luca Healthcare — Website explorations

Design iterations for the Luca Healthcare homepage. Each version is a
self-contained, dependency-free static site (HTML + CSS + JS) — no build step.

## Drafts

| Folder | Description |
|--------|-------------|
| `draft-1/` | **Dark theme** — Owkin-structure redesign on Luca's navy + cyan, with an iridescent orb hero. |
| `draft-2/` | **Light theme** (current) — warm cream, editorial hero, AI-forward narrative, and a custom animated **lung** centerpiece (breathing motion + bronchial airflow + AI scan nodes). |

## Run any draft locally

```bash
cd draft-2          # or draft-1
python3 -m http.server 8088   # then open http://localhost:8088
# or just double-click index.html
```

## Notes

- These are design passes — buttons/links are visual (in-page anchors), not wired
  to real endpoints.
- Fonts loaded from Google Fonts. Fully responsive; respects `prefers-reduced-motion`.
