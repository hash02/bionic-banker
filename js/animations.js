/* ============================================
   BIONIC BANKER — ANIMATION ENGINE
   Magnetic 3D Cards + Counters + Scroll FX
   ============================================ */

(function() {
  "use strict";

  // ===== AOS INIT =====
  if (typeof AOS !== "undefined") {
    AOS.init({
      duration: 700,
      easing: "ease-out-cubic",
      once: true,
      offset: 60,
    });
  }

  // ===== MAGNETIC 3D CARD TILT =====
  var magneticCards = document.querySelectorAll(
    ".article-card, .article-card-featured, .hero-article-card, .thoughts-card, .intel-card, .writing-card"
  );

  var isTouchDevice = "ontouchstart" in window || navigator.maxTouchPoints > 0;

  if (!isTouchDevice) {
    magneticCards.forEach(function(card) {
      card.addEventListener("mousemove", function(e) {
        var rect = card.getBoundingClientRect();
        var x = e.clientX - rect.left;
        var y = e.clientY - rect.top;
        var centerX = rect.width / 2;
        var centerY = rect.height / 2;
        var deltaX = (x - centerX) / centerX;
        var deltaY = (y - centerY) / centerY;

        // 3D perspective tilt — card tilts toward cursor
        var tiltX = -deltaY * 5; // vertical tilt
        var tiltY = deltaX * 5;  // horizontal tilt

        card.style.transform =
          "translateY(-6px) perspective(800px) rotateX(" + tiltX + "deg) rotateY(" + tiltY + "deg) scale(1.01)";

        // Dynamic shadow — shifts opposite to tilt
        var shadowX = -deltaX * 15;
        var shadowY = -deltaY * 15 + 20;
        card.style.boxShadow =
          shadowX + "px " + shadowY + "px 60px rgba(0,0,0,0.45), 0 0 40px rgba(31,160,104,0.06)";

        // Cursor glow position
        card.style.setProperty("--glow-x", x + "px");
        card.style.setProperty("--glow-y", y + "px");
        card.style.setProperty("--glow-opacity", "1");
      });

      card.addEventListener("mouseleave", function() {
        card.style.transform = "";
        card.style.boxShadow = "";
        card.style.setProperty("--glow-opacity", "0");
      });
    });
  }

  // ===== STAT COUNTER ANIMATION =====
  var counterDone = false;
  function animateCounters() {
    if (counterDone) return;
    counterDone = true;

    var statEls = document.querySelectorAll(".hstat-n");
    statEls.forEach(function(el) {
      var text = el.textContent.trim();
      var match = text.match(/^(\d+)/);
      if (!match) return;

      var target = parseInt(match[1]);
      var suffix = text.replace(/^\d+/, ""); // captures "+" etc
      var duration = 1500;
      var startTime = null;

      function step(ts) {
        if (!startTime) startTime = ts;
        var progress = Math.min((ts - startTime) / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
        el.textContent = Math.floor(eased * target) + suffix;
        if (progress < 1) requestAnimationFrame(step);
        else el.textContent = target + suffix;
      }

      el.textContent = "0" + suffix;
      requestAnimationFrame(step);
    });
  }

  // Trigger counters on scroll into view
  var statsRow = document.querySelector(".hero-stats-row");
  if (statsRow) {
    var counterObs = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          animateCounters();
          counterObs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.3 });
    counterObs.observe(statsRow);
  }

  // ===== SECTION TITLE UNDERLINE ANIMATION =====
  var titles = document.querySelectorAll(".section-title-text");
  if (titles.length) {
    var titleObs = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("line-animate");
          titleObs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    titles.forEach(function(t) { titleObs.observe(t); });
  }

  // ===== SECTION DIVIDER ANIMATION =====
  var dividers = document.querySelectorAll(".section-divider-line");
  if (dividers.length) {
    var divObs = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("divider-animate");
          divObs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.2 });
    dividers.forEach(function(d) { divObs.observe(d); });
  }

  // ===== READING PROGRESS BAR (homepage scroll) =====
  var progressBar = document.getElementById("bb-progress-bar");
  if (progressBar) {
    window.addEventListener("scroll", function() {
      var h = document.documentElement;
      var pct = (h.scrollTop / (h.scrollHeight - h.clientHeight)) * 100;
      progressBar.style.width = pct + "%";
    }, { passive: true });
  }

})();

// ===== MOBILE: KILL PARTICLE CANVAS =====
// Particles are CPU-heavy and have no interaction on touch
(function() {
  var isMobile = window.innerWidth <= 768 || ("ontouchstart" in window);
  if (isMobile) {
    var canvas = document.getElementById("particle-canvas");
    if (canvas) {
      canvas.style.display = "none";
      // Clear any running animation frame
      var ctx = canvas.getContext("2d");
      if (ctx) ctx.clearRect(0, 0, canvas.width, canvas.height);
    }
  }
})();
