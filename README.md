# Luca Healthcare — Website

A premium, Owkin-inspired redesign of the Luca Healthcare homepage. Built as a
clean, dependency-free static site (HTML + CSS + JS) — no build step required.

## Run locally

```bash
# Option A: any static server
python3 -m http.server 8088
# then open http://localhost:8088

# Option B: just open index.html in a browser
```

## Structure

```
index.html              # Full homepage (all sections + inline icon sprite)
assets/css/main.css     # Design system + all component styles
assets/js/main.js       # Scroll reveal, sticky nav, mobile menu, typewriter,
                        # card spotlight, smooth scroll, form handler
```

## Design system

Defined as CSS custom properties at the top of `main.css` (`:root`). Reinterprets
Luca's real brand colors — navy `#1D243C` + cyan `#009EDF` (brightened to `#19B6F0`)
— into a dark, cinematic palette with soft glows and gradients. Tokens cover
primary / secondary / background / surface / border / muted text / accent / CTA.

## Sections

Header/nav · Hero (orb + typewriter) · Trust strip · Platform overview ·
Three solution cards (Life Science / Wellness / Remote Care) · Impact (cream block) ·
News & Resources · Contact CTA + form · Footer.

## Notes

- All real Luca routes are preserved (`/lifescience/`, `/wellness/`, `/remotecare/`,
  `/our-platform/`, `/company/`, `/resources/`, `/contactus/`, `/privacy-policy/`,
  and the LucaPlex login at `saas.lucahealthcare.cn`).
- The contact form has a graceful client-side demo handler. Wire `action="/contactus/"`
  in `index.html` to a real endpoint to enable live submission.
- Fonts: Fraunces (display serif) + Inter (sans), loaded from Google Fonts.
- Fully responsive; respects `prefers-reduced-motion`.
