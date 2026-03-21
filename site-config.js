/* Site Config — Single source of truth. Updated by n8n WF-06. */
window.SITE_CONFIG = {
  articleCount: 26,
  lastUpdated: "2026-03-21"
};

/* Auto-apply counts to any element with data-count="articles" */
document.addEventListener("DOMContentLoaded", function() {
  var els = document.querySelectorAll("[data-count=\"articles\"]");
  for (var i = 0; i < els.length; i++) {
    els[i].textContent = window.SITE_CONFIG.articleCount;
  }
});
