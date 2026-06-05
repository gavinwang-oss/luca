/* =============================================================
   Luca Healthcare — interactions (light build)
   ============================================================= */
(function () {
  'use strict';

  /* Sticky header */
  const header = document.getElementById('header');
  const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 20);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* Mobile menu */
  const menu = document.getElementById('mobileMenu');
  const open = document.getElementById('navOpen');
  const close = document.getElementById('navClose');
  const setMenu = (s) => { menu.classList.toggle('open', s); document.body.style.overflow = s ? 'hidden' : ''; };
  open && open.addEventListener('click', () => setMenu(true));
  close && close.addEventListener('click', () => setMenu(false));
  menu && menu.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => setMenu(false)));

  /* Scroll reveal */
  const reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add('in'));
  }

  /* Smooth-scroll for in-page anchors */
  document.querySelectorAll('a[href^="#"]').forEach((a) => {
    a.addEventListener('click', (e) => {
      const id = a.getAttribute('href');
      if (id.length < 2) return;
      const t = document.querySelector(id);
      if (t) { e.preventDefault(); t.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    });
  });

  /* =============================================================
     Hero "rolling die" — types a left fragment, rolls, types the
     right fragment, holds, then rolls on to the next sentence.
     ============================================================= */
  (function diceHero() {
    const cube  = document.getElementById('heroCube');
    const left  = document.getElementById('diceLeft');
    const right = document.getElementById('diceRight');
    if (!cube || !left || !right) return;

    // Each sentence: a setup fragment (left) + a payoff fragment (right).
    // `accent: true` wraps the right fragment in the gradient style.
    const SENTENCES = [
      { l: 'Decoding health,',           r: 'one biomarker at a time.',         accent: true  },
      { l: 'From the sound of a breath', r: 'to clinical-grade insight.',        accent: true  },
      { l: 'Everyday signals,',          r: 'turned into early answers.',        accent: true  },
      { l: 'Predictive AI',              r: 'for the future of respiratory care.', accent: true },
    ];

    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Static fallback for reduced-motion users.
    if (reduce) {
      left.textContent = SENTENCES[0].l;
      right.innerHTML  = '<span class="accent">' + SENTENCES[0].r + '</span>';
      return;
    }

    const TYPE_SPD  = 42;    // ms per character
    const HOLD_FULL = 2200;  // ms a complete sentence stays up
    const ROLL_MS   = 900;   // must match CSS transition on .hero-cube
    let yaw = 0;             // accumulated cube Y rotation
    let pitch = 0;           // accumulated cube X rotation (for variety)
    let idx = 0;

    const wait = (ms) => new Promise((res) => setTimeout(res, ms));

    function type(el, text, accent) {
      return new Promise((resolve) => {
        el.classList.add('caret');
        let i = 0;
        const open = accent ? '<span class="accent">' : '';
        const close = accent ? '</span>' : '';
        (function step() {
          el.innerHTML = open + text.slice(0, i) + close;
          if (i++ <= text.length) setTimeout(step, TYPE_SPD);
          else { el.classList.remove('caret'); resolve(); }
        })();
      });
    }

    function roll() {
      // A real die tips over ONE edge at a time — never two axes at once,
      // which is what caused the diagonal wobble. Mostly tumble sideways
      // (matches the left→right text flow); occasionally tip forward/back.
      if (Math.random() < 0.3) {
        pitch += (Math.random() < 0.5 ? 90 : -90);   // pure forward/back tumble
      } else {
        yaw += 90;                                    // pure sideways roll
      }
      cube.style.setProperty('--cube-y', yaw + 'deg');
      cube.style.setProperty('--cube-x', pitch + 'deg');
      return wait(ROLL_MS);
    }

    async function run() {
      // tiny beat so the first frame isn't blank on load
      await wait(300);
      while (true) {
        const s = SENTENCES[idx % SENTENCES.length];

        await type(left, s.l, false);   // type the setup on the left
        await wait(220);
        await roll();                    // die rolls...
        await type(right, s.r, s.accent);// payoff types in on the right
        await wait(HOLD_FULL);           // hold the full sentence

        await roll();                    // roll on — clear for the next
        left.textContent = '';
        right.textContent = '';
        await wait(180);
        idx++;
      }
    }
    run();
  })();
})();
