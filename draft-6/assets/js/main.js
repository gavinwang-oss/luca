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

  /* ===== i18n: EN source <-> ZH overlay, persisted in localStorage ===== */
  (function () {
    var ZH = window.LUCA_ZH;
    if (!ZH) return;
    var KEY = 'luca-lang';

    // Walk text nodes once, cache the node + its original English text.
    var nodes = [];
    var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (!n.nodeValue || !n.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        var p = n.parentNode;
        if (!p) return NodeFilter.FILTER_REJECT;
        var tag = p.nodeName;
        if (tag === 'SCRIPT' || tag === 'STYLE') return NodeFilter.FILTER_REJECT;
        if (p.closest && p.closest('[data-zh-text]')) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    var nd;
    while ((nd = walker.nextNode())) {
      nodes.push({ node: nd, en: nd.nodeValue, key: nd.nodeValue.trim() });
    }

    // Attribute-bearing things: placeholders, <option>, meta description, <title>.
    var ph = [].map.call(document.querySelectorAll('input[placeholder],textarea[placeholder]'), function (el) {
      return { el: el, en: el.getAttribute('placeholder') };
    });
    var opts = [].map.call(document.querySelectorAll('option'), function (el) {
      return { el: el, en: el.textContent, key: el.textContent.trim() };
    });
    var metaDesc = document.querySelector('meta[name="description"]');
    var metaEn = metaDesc ? metaDesc.getAttribute('content') : null;
    var titleEn = document.title;

    function apply(lang) {
      var zh = lang === 'zh';
      // element-level overrides (disambiguate identical EN strings, e.g. nav "Company")
      document.querySelectorAll('[data-zh-text]').forEach(function (el) {
        if (!el.hasAttribute('data-en-text')) el.setAttribute('data-en-text', el.textContent);
        el.textContent = zh ? el.getAttribute('data-zh-text') : el.getAttribute('data-en-text');
      });
      // text nodes — for ZH assign the translation directly (CJK needs no
      // inter-word spaces); for EN restore the exact original node text.
      nodes.forEach(function (o) {
        if (zh) {
          var t = ZH[o.key];
          if (t != null) o.node.nodeValue = t;
        } else {
          o.node.nodeValue = o.en;
        }
      });
      // placeholders
      ph.forEach(function (o) {
        if (!o.en) return;
        var t = zh ? ZH[o.en.trim()] : null;
        o.el.setAttribute('placeholder', zh && t != null ? t : o.en);
      });
      // <option> labels
      opts.forEach(function (o) {
        if (zh) { var t = ZH[o.key]; if (t != null) o.el.textContent = o.en.replace(o.key, t); }
        else o.el.textContent = o.en;
      });
      // meta + title
      if (metaDesc && metaEn) { var md = zh ? ZH[metaEn.trim()] : null; metaDesc.setAttribute('content', zh && md != null ? md : metaEn); }
      var tt = zh ? ZH[titleEn.trim()] : null; document.title = zh && tt != null ? tt : titleEn;
      // <html lang> + active button state
      document.documentElement.setAttribute('lang', zh ? 'zh-CN' : 'en');
      document.querySelectorAll('.lang a[data-lang]').forEach(function (a) {
        a.classList.toggle('active', a.getAttribute('data-lang') === lang);
      });
      try { localStorage.setItem(KEY, lang); } catch (e) {}
    }

    // wire buttons
    document.querySelectorAll('.lang a[data-lang]').forEach(function (a) {
      a.addEventListener('click', function (e) { e.preventDefault(); apply(a.getAttribute('data-lang')); });
    });

    // restore saved choice (default en)
    var saved = 'en';
    try { saved = localStorage.getItem(KEY) || 'en'; } catch (e) {}
    if (saved === 'zh') apply('zh'); else apply('en');
  })();

  /* Resources carousel — paged slide, arrows disable at ends */
  (function () {
    var track = document.getElementById('resTrack');
    var prev = document.getElementById('resPrev');
    var next = document.getElementById('resNext');
    if (!track || !prev || !next) return;
    var cards = [].slice.call(track.children);
    if (!cards.length) return;
    var index = 0; // index of the left-most visible card

    function perView() {
      var w = window.innerWidth;
      if (w <= 560) return 1;
      if (w <= 900) return 2;
      return 4;
    }
    function maxIndex() { return Math.max(0, cards.length - perView()); }
    function step() {
      // card width + gap
      var gap = parseFloat(getComputedStyle(track).columnGap || getComputedStyle(track).gap || '22') || 22;
      return cards[0].getBoundingClientRect().width + gap;
    }
    function update() {
      if (index > maxIndex()) index = maxIndex();
      track.style.transform = 'translateX(' + (-index * step()) + 'px)';
      prev.disabled = index <= 0;
      next.disabled = index >= maxIndex();
    }
    prev.addEventListener('click', function () { index = Math.max(0, index - perView()); update(); });
    next.addEventListener('click', function () { index = Math.min(maxIndex(), index + perView()); update(); });
    var rt;
    window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(update, 150); }, { passive: true });
    update();
  })();

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
