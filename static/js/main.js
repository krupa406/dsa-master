document.addEventListener('DOMContentLoaded', () => {
  // Highlight active nav module icon
  const path = window.location.pathname;
  document.querySelectorAll('.nav-link').forEach(link => {
    if (link.getAttribute('href') === path) link.classList.add('active');
  });

  // Prism.js handles all <code class="language-python"> blocks automatically.
  // Re-highlight any blocks that were injected after initial load.
  if (window.Prism) Prism.highlightAll();
});
