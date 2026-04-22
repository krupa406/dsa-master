// Inject modules_nav into base template via a global populated by Flask
// (nav icons are rendered server-side; this file handles shared client utilities)

// Highlight active nav link
document.addEventListener('DOMContentLoaded', () => {
  const path = window.location.pathname;
  document.querySelectorAll('.nav-link').forEach(link => {
    if (link.getAttribute('href') === path) link.classList.add('active');
  });

  // Syntax highlight: wrap keywords in code blocks
  document.querySelectorAll('.theory-content pre code').forEach(block => {
    block.innerHTML = highlight(block.innerHTML);
  });
});

function highlight(code) {
  const keywords = ['def','class','return','if','elif','else','for','while',
                    'in','not','and','or','import','from','pass','None',
                    'True','False','lambda','yield','with','as','try','except',
                    'raise','break','continue','global','self'];
  const kwRe = new RegExp(`\\b(${keywords.join('|')})\\b`, 'g');

  return code
    .replace(/(&lt;.*?&gt;)/g, '<span style="color:#f9a8d4">$1</span>')
    .replace(/(#.*?)(\n|$)/g, '<span style="color:#6ee7b7;font-style:italic">$1</span>$2')
    .replace(/("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'|"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*')/g,
             '<span style="color:#fcd34d">$1</span>')
    .replace(/\b(\d+\.?\d*)\b/g, '<span style="color:#fb923c">$1</span>')
    .replace(kwRe, '<span style="color:#a78bfa;font-weight:600">$1</span>');
}
