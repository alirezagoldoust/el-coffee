document.addEventListener('DOMContentLoaded', () => {
  const tabs = document.querySelectorAll('.cat-tab');
  const sections = document.querySelectorAll('.menu-section');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      const filter = tab.dataset.filter;

      sections.forEach(section => {
        if (filter === 'all' || section.dataset.category === filter) {
          section.classList.remove('hidden');
          section.style.animationName = 'none';
          section.offsetHeight; // reflow
          section.style.animationName = '';
        } else {
          section.classList.add('hidden');
        }
      });

      if (filter !== 'all') {
        const target = document.getElementById(filter);
        if (target) {
          setTimeout(() => target.scrollIntoView({ behavior: 'smooth', block: 'start' }), 50);
        }
      }
    });
  });

  // Stagger card entrance animations via IntersectionObserver
  const cards = document.querySelectorAll('.menu-card');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  cards.forEach((card, i) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(24px)';
    card.style.transition = `opacity 0.5s ease ${i * 0.06}s, transform 0.5s ease ${i * 0.06}s, box-shadow 0.35s, border-color 0.35s`;
    observer.observe(card);
  });
});
