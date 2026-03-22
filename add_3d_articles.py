#!/usr/bin/env python3
"""Add Vanta.js NET + GSAP ScrollTrigger to articles page."""
import re

filepath = '/home/vic1hash/bionic-banker/articles/index.html'

with open(filepath, 'r') as f:
    content = f.read()

# 1. Add CDN scripts before </head>
cdn_scripts = '''<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vanta@0.5.24/dist/vanta.net.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<link rel="stylesheet" href="/styles/animations.css?vdaa5e4d">
'''

content = content.replace('</head>', cdn_scripts + '</head>')

# 2. Add Vanta init on the page-header and GSAP card animations before </body>
init_script = '''<script>
window.addEventListener('load', function() {
  // Vanta NET on page header (desktop only)
  if (window.innerWidth > 768 && typeof VANTA !== 'undefined') {
    var ph = document.querySelector('.page-header');
    if (ph) {
      ph.style.position = 'relative';
      ph.style.overflow = 'hidden';
      window._vantaArticles = VANTA.NET({
        el: ph,
        mouseControls: true,
        touchControls: false,
        gyroControls: false,
        minHeight: 200,
        minWidth: 200,
        scale: 1.0,
        scaleMobile: 1.0,
        color: 0x1fa068,
        backgroundColor: 0x020204,
        points: 8,
        maxDistance: 22,
        spacing: 18,
        showDots: true
      });
    }
  }

  // GSAP ScrollTrigger — staggered card entrances
  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);

    gsap.utils.toArray('.article-card').forEach(function(card, i) {
      gsap.from(card, {
        scrollTrigger: {
          trigger: card,
          start: 'top 90%',
          toggleActions: 'play none none none'
        },
        y: 40,
        opacity: 0,
        duration: 0.6,
        delay: (i % 3) * 0.1,
        ease: 'power2.out'
      });
    });

    // Page title entrance
    gsap.from('.page-title', {
      y: 30, opacity: 0, duration: 0.8, ease: 'power2.out'
    });
    gsap.from('.page-sub', {
      y: 20, opacity: 0, duration: 0.8, delay: 0.2, ease: 'power2.out'
    });
    gsap.from('.filter-bar', {
      y: 20, opacity: 0, duration: 0.6, delay: 0.4, ease: 'power2.out'
    });
  }
});
</script>
'''

content = content.replace('</body>', init_script + '</body>')

with open(filepath, 'w') as f:
    f.write(content)

print("Added Vanta + GSAP to articles/index.html")
