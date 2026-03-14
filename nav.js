/* ═══ Bionic Banker — Shared Navigation ═══
   ONE file controls nav on ALL pages.
   Change this = every page updates instantly.
   No more editing 28 HTML files for a link change.
*/

(function() {
  // Current page for active highlighting
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';

  // Build nav HTML
  const navHTML = `
    <a href="index.html" class="nav-logo">Bionic <span>Banker</span></a>
    <button class="nav-toggle" id="navToggle" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
    <div class="nav-right" id="navRight">
      <ul class="nav-links">
        <li><a href="articles.html"${currentPage === 'articles.html' ? ' class="active"' : ''}>All Articles</a></li>
        <li><a href="ai.html"${currentPage === 'ai.html' ? ' class="active"' : ''}>AI Intelligence</a></li>
        <li><a href="investigate.html"${currentPage === 'investigate.html' ? ' class="active"' : ''}>Investigate</a></li>
        <li><a href="index.html#about"${currentPage === 'index.html' ? ' class="active"' : ''}>About</a></li>
      </ul>
      <a href="https://t.me/BionicBanker" class="nav-cta" target="_blank" rel="noopener">Join Telegram</a>
    </div>
  `;

  // Find nav element and inject
  const nav = document.querySelector('nav');
  if (nav) {
    nav.innerHTML = navHTML;
  }

  // Create overlay (outside nav to avoid stacking context issues)
  let overlay = document.getElementById('navOverlay');
  if (!overlay) {
    overlay = document.createElement('div');
    overlay.id = 'navOverlay';
    overlay.className = 'nav-overlay';
    // Insert AFTER nav, not inside it
    nav.parentNode.insertBefore(overlay, nav.nextSibling);
  }

  // Toggle function
  function toggleNav() {
    const navRight = document.getElementById('navRight');
    navRight.classList.toggle('open');
    overlay.classList.toggle('active');
  }

  // Close function
  function closeNav() {
    const navRight = document.getElementById('navRight');
    navRight.classList.remove('open');
    overlay.classList.remove('active');
  }

  // Wire up hamburger button
  document.getElementById('navToggle').addEventListener('click', toggleNav);

  // Close on overlay tap
  overlay.addEventListener('click', closeNav);

  // Close on any link tap
  document.querySelectorAll('#navRight a').forEach(function(link) {
    link.addEventListener('click', closeNav);
  });
})();
