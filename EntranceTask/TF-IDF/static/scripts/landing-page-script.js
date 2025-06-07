document.addEventListener("DOMContentLoaded", () => {
  const messageBox = document.querySelector(".a_a-success-message");

  if (messageBox) {
    setTimeout(() => {
      messageBox.style.transition = "opacity 0.5s ease, transform 0.5s ease";
      messageBox.style.opacity = "0";
      messageBox.style.transform = "translateY(-10px)";

      setTimeout(() => {
        messageBox.remove();
      }, 500);
    }, 10000); // 10 seconds
  }
});
