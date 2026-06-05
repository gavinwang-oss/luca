/* =============================================================
   Luca Healthcare — interactions
   ============================================================= */
(function () {
  'use strict';

  /* ---- Sticky header state ---- */
  const header = document.getElementById('header');
  const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 24);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ---- Mobile menu ---- */
  const menu = document.getElementById('mobileMenu');
  const open = document.getElementById('navOpen');
  const close = document.getElementById('navClose');
  const setMenu = (state) => {
    menu.classList.toggle('open', state);
    document.body.style.overflow = state ? 'hidden' : '';
  };
  open && open.addEventListener('click', () => setMenu(true));
  close && close.addEventListener('click', () => setMenu(false));
  menu && menu.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => setMenu(false)));

  /* ---- Scroll reveal ---- */
  const reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add('in'));
  }

  /* ---- Hero typewriter (cycles the gradient phrase) ---- */
  const typed = document.getElementById('typed');
  if (typed && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const words = ['Digital Health', 'Biomarker', 'Bio-Intelligence', 'Clinical'];
    let wi = 0, ci = 0, deleting = false;
    const tick = () => {
      const word = words[wi];
      typed.textContent = deleting ? word.slice(0, --ci) : word.slice(0, ++ci);
      let delay = deleting ? 55 : 110;
      if (!deleting && ci === word.length) { delay = 1900; deleting = true; }
      else if (deleting && ci === 0) { deleting = false; wi = (wi + 1) % words.length; delay = 450; }
      setTimeout(tick, delay);
    };
    setTimeout(tick, 1600);
  }

  /* ---- Solution card spotlight (follows pointer) ---- */
  document.querySelectorAll('.sol-card').forEach((card) => {
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      card.style.setProperty('--mx', ((e.clientX - r.left) / r.width) * 100 + '%');
      card.style.setProperty('--my', ((e.clientY - r.top) / r.height) * 100 + '%');
    });
  });

  /* ---- Smooth-scroll for in-page anchors ---- */
  document.querySelectorAll('a[href^="#"]').forEach((a) => {
    a.addEventListener('click', (e) => {
      const id = a.getAttribute('href');
      if (id.length < 2) return;
      const target = document.querySelector(id);
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    });
  });

  /* ---- Contact form (graceful demo handler — preserves real action) ---- */
  const form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', (e) => {
      // No backend wired in this static build — prevent navigation and confirm.
      // Wire `action="/contactus/"` to the real endpoint to enable live submission.
      e.preventDefault();
      const btn = form.querySelector('button[type="submit"]');
      const original = btn.innerHTML;
      btn.innerHTML = 'Thank you — we\u2019ll be in touch';
      btn.style.background = '#2BE0C8';
      form.reset();
      setTimeout(() => { btn.innerHTML = original; btn.style.background = ''; }, 3200);
    });
  }
})();
