/* ═══ Bionic Banker — Self-Contained Navigation ═══
   This file controls nav on ALL pages.
   It injects its own mobile styles — ZERO dependency on styles.css for mobile nav.
   Edit this ONE file to change nav everywhere.
*/
(function() {
  var page = (window.location.pathname.split('/').pop() || 'index.html').toLowerCase();

  /* ── Inject mobile nav styles directly (no CSS file dependency) ── */
  var style = document.createElement('style');
  style.textContent = [
    /* Hide hamburger on desktop */
    '.bb-toggle { display:none; background:none; border:none; cursor:pointer; padding:10px; z-index:10001; position:relative; }',
    '.bb-toggle span { display:block; width:22px; height:2px; background:#e4e4ec; margin:4px 0; border-radius:2px; transition:transform 0.3s, opacity 0.3s; }',

    /* Mobile overlay */
    '.bb-overlay { display:none; position:fixed; top:0; left:0; right:0; bottom:0; background:rgba(0,0,0,0.65); z-index:9998; }',
    '.bb-overlay.active { display:block; }',

    /* Mobile slide-in panel */
    '.bb-mobile-nav { position:fixed; top:0; right:0; width:270px; height:100vh; height:100dvh; background:#08080e; border-left:1px solid rgba(31,160,104,0.2); z-index:9999; transform:translateX(100%); transition:transform 0.3s ease; display:flex; flex-direction:column; padding:3.5rem 1.5rem 2rem; gap:0.5rem; }',
    '.bb-mobile-nav.open { transform:translateX(0); }',

    /* Mobile nav links */
    '.bb-mobile-nav a { display:block; padding:0.75rem 0.25rem; font-family:"Plus Jakarta Sans",sans-serif; font-size:1.05rem; font-weight:500; color:#e4e4ec; text-decoration:none; border-bottom:1px solid rgba(255,255,255,0.06); transition:color 0.2s; }',
    '.bb-mobile-nav a:last-child { border-bottom:none; }',
    '.bb-mobile-nav a:active, .bb-mobile-nav a:hover { color:#1fa068; }',
    '.bb-mobile-nav a.bb-active { color:#1fa068; }',

    /* Mobile CTA button */
    '.bb-mobile-cta { display:inline-block; margin-top:1rem; padding:0.7rem 1.4rem; font-family:"Plus Jakarta Sans",sans-serif; font-size:0.85rem; font-weight:600; color:#1fa068; border:1px solid #1fa068; border-radius:6px; text-decoration:none; text-align:center; letter-spacing:0.03em; transition:background 0.2s, color 0.2s; }',
    '.bb-mobile-cta:active { background:#1fa068; color:#08080e; }',

    /* Show hamburger on mobile only */
    '@media(max-width:640px) { .bb-toggle { display:block; } }'
  ].join('\n');
  document.head.appendChild(style);

  /* ── Build desktop nav (inside <nav>) ── */
  var nav = document.querySelector('nav');
  if (!nav) return;

  nav.innerHTML = '' +
    '<a href="index.html" class="nav-logo">Bionic <span>Banker</span></a>' +
    '<button class="bb-toggle" id="bbToggle" aria-label="Menu"><span></span><span></span><span></span></button>' +
    '<div class="nav-right">' +
      '<ul class="nav-links">' +
        '<li><a href="articles.html">All Articles</a></li>' +
        '<li><a href="ai.html">AI Intelligence</a></li>' +
        '<li><a href="investigate.html">Investigate</a></li>' +
        '<li><a href="index.html#about">About</a></li>' +
      '</ul>' +
      '<a href="https://t.me/BionicBanker" class="nav-cta" target="_blank" rel="noopener">Join Telegram</a>' +
    '</div>';

  /* ── Build mobile panel + overlay (OUTSIDE nav — no stacking trap) ── */
  var overlay = document.createElement('div');
  overlay.className = 'bb-overlay';
  overlay.id = 'bbOverlay';
  document.body.appendChild(overlay);

  var panel = document.createElement('div');
  panel.className = 'bb-mobile-nav';
  panel.id = 'bbPanel';

  var links = [
    { href: 'articles.html', text: 'All Articles' },
    { href: 'ai.html', text: 'AI Intelligence' },
    { href: 'investigate.html', text: 'Investigate' },
    { href: 'index.html#about', text: 'About' }
  ];

  links.forEach(function(l) {
    var a = document.createElement('a');
    a.href = l.href;
    a.textContent = l.text;
    if (page === l.href.split('#')[0].toLowerCase()) a.className = 'bb-active';
    panel.appendChild(a);
  });

  var cta = document.createElement('a');
  cta.href = 'https://t.me/BionicBanker';
  cta.target = '_blank';
  cta.rel = 'noopener';
  cta.className = 'bb-mobile-cta';
  cta.textContent = 'Join Telegram';
  panel.appendChild(cta);

  document.body.appendChild(panel);

  /* ── Toggle logic ── */
  function openNav() { panel.classList.add('open'); overlay.classList.add('active'); }
  function closeNav() { panel.classList.remove('open'); overlay.classList.remove('active'); }

  document.getElementById('bbToggle').addEventListener('click', function(e) {
    e.stopPropagation();
    if (panel.classList.contains('open')) { closeNav(); } else { openNav(); }
  });

  overlay.addEventListener('click', closeNav);

  /* Links close the menu on tap */
  panel.querySelectorAll('a').forEach(function(a) {
    a.addEventListener('click', function() { closeNav(); });
  });
})();
