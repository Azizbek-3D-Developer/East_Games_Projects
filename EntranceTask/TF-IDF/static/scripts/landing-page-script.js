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


document.addEventListener("DOMContentLoaded", () => {
  // Select any success message div by class or ID
  const successMessages = document.querySelectorAll(".a_a-success-message");
  
  if (successMessages.length > 0) {
    setTimeout(() => {
      successMessages.forEach(msg => {
        msg.style.transition = "opacity 1s ease";
        msg.style.opacity = "0";
        setTimeout(() => {
          if (msg.parentNode) {
            msg.parentNode.removeChild(msg);
          }
        }, 1000);
      });
    }, 10000); 
  }
});
