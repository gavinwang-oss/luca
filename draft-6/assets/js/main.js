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

  /* Contact form (design preview — not wired to a live endpoint) */
  const cf = document.getElementById('contactForm');
  if (cf) {
    cf.addEventListener('submit', (e) => {
      e.preventDefault();
      if (!cf.checkValidity()) { cf.reportValidity(); return; }
      const note = document.getElementById('cfNote');
      if (note) note.hidden = false;
      const btn = cf.querySelector('.cf-submit');
      if (btn) { btn.disabled = true; btn.style.opacity = '0.6'; }
    });
  }
})();
