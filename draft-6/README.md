# Luca Healthcare — Website (draft-6)

A self-contained, **static** marketing website for Luca Healthcare. No build
step, no framework, no dependencies — just HTML, CSS, and a little vanilla JS.

---

## Quick start

Open `index.html` in a browser — that's it. Or, to preview with correct
relative paths (recommended, so the news/ and privacy pages resolve):

```bash
cd draft-6
python3 -m http.server 8080
# then open http://localhost:8080
```

To put it live, upload the **contents of this folder** to any static host

---

## Pages

| File | Purpose |
|------|---------|
| `index.html` | Homepage — hero, mission, intelligence platform, proof-at-scale stats, what we offer, patient-generated RWD, partners marquee, **Resources** (news), contact CTA |
| `contact.html` | Contact page — two-column layout with the enquiry form |
| `privacy-policy.html` | Full privacy policy |
| `resources.html` | Standalone news listing (legacy — the homepage `#resources` section is the primary one; this page is no longer linked from nav) |
| `news/*.html` | 12 individual news / press-release article pages |

All internal links are relative, so the site works from any sub-path or domain.

---

## Folder structure

```
draft-6/
├── index.html
├── contact.html
├── privacy-policy.html
├── resources.html
├── news/                     # 12 article pages
├── assets/
│   ├── css/main.css          # all styles (single file)
│   ├── js/
│   │   ├── main.js           # nav, scroll-reveal, carousel, form stub, i18n engine
│   │   └── i18n-dict.js      # EN→中文 translation dictionary
│   └── img/                  # logos, lung visuals, favicons, news/ thumbnails, partners/ logos
├── build_news.py             # regenerates news/*.html from article data (optional, dev tool)
└── build_privacy.py          # regenerates privacy-policy.html (optional, dev tool)
```

> `build_news.py` / `build_privacy.py` are convenience generators used to
> author the article pages. You do **not** need them to run or deploy the site —
> the generated `.html` files are committed. Edit them only if you'd rather
> regenerate pages from structured data than hand-edit HTML.

---

## Language toggle (EN / 中文)

The footer has an **EN / 中文** switch. English is the source text in the HTML;
Chinese is applied as an overlay from `assets/js/i18n-dict.js`, and the choice
is saved in `localStorage` so it persists across pages.

- The homepage, nav, footer, and contact form **are** translated.
- The **news articles and privacy policy are English-only** for now. To add
  Chinese for any string, add a `"English": "中文"` entry to `i18n-dict.js`.

---

## ⚠️ Contact form — needs a backend

The enquiry form on `contact.html` is **fully built** (fields, labels,
validation) but is **not yet connected to anything**. On submit it currently
just shows a "design preview" notice (see the handler in `assets/js/main.js`,
the `#contactForm` block).

To make it send, pick one:

**A. Form service (no backend code) — easiest**
Point the form at a service like Web3Forms / Formspree / Netlify Forms.
1. In `contact.html`, give the `<form id="contactForm">` an `action="<endpoint>"`
   and `method="POST"`.
2. In `assets/js/main.js`, replace the design-preview stub so it either lets the
   native POST through, or does a `fetch()` POST and shows a success message.

**B. Your own backend**
POST the form fields to your own endpoint and handle storage/email there.

Form fields (names): `name`, `email`, `company`, `title`, `country`,
`interest`, `marketing` (checkbox).

> **Security note:** any form-service *public* key placed in the HTML is visible
> to anyone (View Source) — that's expected and safe for those services. Never
> put a **private/secret** API key in front-end code; it must live server-side.

---


## Notes

- Fonts: **Inter** (variable, latin subset) is **self-hosted** in
  `assets/fonts/inter-latin.woff2` and loaded via `@font-face` in `main.css` —
  no external CDN, so the site loads reliably in mainland China where Google
  Fonts is blocked. The site has **zero external resource dependencies**.
- Brand: single cyan accent `#009EDF`, warm cream background, Heroicons inline
  SVG icons. Design language documented implicitly in `assets/css/main.css`
  (CSS custom properties at the top of the file).
- No analytics or third-party trackers are included.
- Fully responsive; respects `prefers-reduced-motion`.
