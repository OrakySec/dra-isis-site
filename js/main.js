// ============================================
// DRA. ÍSIS ANDRADE — Main JavaScript
// ============================================

document.addEventListener('DOMContentLoaded', () => {

  // ---- Animate on scroll ----
  const animatedEls = document.querySelectorAll('.animate-on-scroll');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.12,
    rootMargin: '0px 0px -40px 0px'
  });

  animatedEls.forEach(el => observer.observe(el));

  // ---- Procedures tabs ----
  const tabs = document.querySelectorAll('.procedures__tab');
  const panels = document.querySelectorAll('.procedures__panel');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const targetId = tab.getAttribute('aria-controls');

      tabs.forEach(t => {
        t.classList.remove('active');
        t.setAttribute('aria-selected', 'false');
      });
      panels.forEach(p => p.classList.remove('active'));

      tab.classList.add('active');
      tab.setAttribute('aria-selected', 'true');
      const targetPanel = document.getElementById(targetId);
      if (targetPanel) {
        targetPanel.classList.add('active');
      }
    });
  });

  // ---- Smooth scroll for anchor links ----
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // ---- Service cards hover effect (touch devices) ----
  const cards = document.querySelectorAll('.service-card');
  cards.forEach(card => {
    card.addEventListener('touchstart', () => {
      card.style.transform = 'translateY(-4px)';
    }, { passive: true });
    card.addEventListener('touchend', () => {
      setTimeout(() => { card.style.transform = ''; }, 300);
    }, { passive: true });
  });

});
