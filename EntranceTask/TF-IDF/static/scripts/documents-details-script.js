const toggles = document.querySelectorAll('.collapsible-toggle');
  toggles.forEach(btn => {
    btn.addEventListener('click', () => {
      btn.classList.toggle('active');
      const content = btn.nextElementSibling;
      content.style.display = content.style.display === 'block' ? 'none' : 'block';
    });
  });
  
document.addEventListener("DOMContentLoaded", () => {
  const toggles = document.querySelectorAll(".collapsible-header");

  toggles.forEach(header => {
    header.addEventListener("click", () => {
      const content = header.nextElementSibling;
      const icon = header.querySelector(".toggle-icon");

      content.classList.toggle("open");
      icon.style.transform = content.classList.contains("open") ? "rotate(180deg)" : "rotate(0deg)";
    });
  });
});