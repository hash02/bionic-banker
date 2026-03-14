/* Bionic Banker — Shared Navigation (simple, stable) */
(function() {
  var nav = document.querySelector('nav');
  if (!nav) return;

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
    '</div>';
})();
