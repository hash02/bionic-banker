/* Bionic Banker — Shared Navigation + Mobile Hamburger */
(function() {
  var nav = document.querySelector('nav');
  if (!nav) return;

  /* ── Desktop nav ── */
  nav.innerHTML =
    '<a href="index.html" class="nav-logo">Bionic <span>Banker</span></a>' +
    '<div class="nav-right">' +
      '<ul class="nav-links">' +
        '<li><a href="articles.html">All Articles</a></li>' +
        '<li><a href="ai.html">AI Intelligence</a></li>' +
        '<li><a href="investigate.html">Investigate</a></li>' +
        '<li><a href="index.html#about">About</a></li>' +
      '</ul>' +
      '<a href="https://t.me/BionicBanker" class="nav-cta" target="_blank" rel="noopener">Join Telegram</a>' +
    '</div>' +
    '<button id="bb-hamburger" aria-label="Menu">&#9776;</button>';

  /* ── Inject mobile styles (zero CSS file dependency) ── */
  var style = document.createElement('style');
  style.textContent =
    '#bb-hamburger{display:none;background:none;border:none;color:#e4e4ec;font-size:1.5rem;cursor:pointer;padding:0.25rem;z-index:101;position:relative;}' +
    '@media(max-width:640px){' +
      '.nav-right{display:none !important;}' +
      '#bb-hamburger{display:block;}' +
    '}' +
    '#bb-overlay{position:fixed;inset:0;background:rgba(0,0,0,0.6);z-index:9998;opacity:0;transition:opacity 0.25s ease;pointer-events:none;}' +
    '#bb-overlay.open{opacity:1;pointer-events:auto;}' +
    '#bb-panel{position:fixed;top:0;right:0;bottom:0;width:280px;max-width:85vw;background:#0c0c14;z-index:9999;transform:translateX(100%);transition:transform 0.3s ease;display:flex;flex-direction:column;padding:1.5rem;box-shadow:-4px 0 24px rgba(0,0,0,0.5);}' +
    '#bb-panel.open{transform:translateX(0);}' +
    '#bb-panel-close{align-self:flex-end;background:none;border:none;color:#e4e4ec;font-size:1.5rem;cursor:pointer;padding:0.25rem 0.5rem;margin-bottom:1rem;}' +
    '#bb-panel a{display:block;color:#e4e4ec;font-family:"Plus Jakarta Sans",sans-serif;font-size:1rem;font-weight:500;padding:0.75rem 0;border-bottom:1px solid rgba(255,255,255,0.06);text-decoration:none;pointer-events:auto;}' +
    '#bb-panel a:hover,#bb-panel a:active{color:#1fa068;}' +
    '#bb-panel .bb-panel-cta{display:inline-block;color:#1fa068;border:1px solid rgba(31,160,104,0.4);border-radius:6px;padding:0.6rem 1.2rem;margin-top:1rem;text-align:center;font-size:0.85rem;font-weight:600;}';
  document.head.appendChild(style);

  /* ── Create overlay + panel on document.body ── */
  var overlay = document.createElement('div');
  overlay.id = 'bb-overlay';
  document.body.appendChild(overlay);

  var panel = document.createElement('div');
  panel.id = 'bb-panel';
  panel.innerHTML =
    '<button id="bb-panel-close" aria-label="Close menu">&times;</button>' +
    '<a href="articles.html">All Articles</a>' +
    '<a href="ai.html">AI Intelligence</a>' +
    '<a href="investigate.html">Investigate</a>' +
    '<a href="index.html#about">About</a>' +
    '<a href="https://t.me/BionicBanker" class="bb-panel-cta" target="_blank" rel="noopener">Join Telegram</a>';
  document.body.appendChild(panel);

  /* ── Toggle logic ── */
  function openMenu() {
    panel.classList.add('open');
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function closeMenu() {
    panel.classList.remove('open');
    overlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  document.getElementById('bb-hamburger').addEventListener('click', openMenu);
  document.getElementById('bb-panel-close').addEventListener('click', closeMenu);
  overlay.addEventListener('click', closeMenu);

  /* Close on link tap */
  var panelLinks = panel.querySelectorAll('a');
  for (var i = 0; i < panelLinks.length; i++) {
    panelLinks[i].addEventListener('click', closeMenu);
  }
})();
