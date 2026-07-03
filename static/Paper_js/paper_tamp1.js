document.addEventListener("DOMContentLoaded", function () {
  const openBtn = document.getElementById("openFormBtn");
  const closeBtn = document.getElementById("closeFormBtn");
  const formPopup = document.getElementById("formPopup");

  // Popup toggle - sirf popup open/close ka code
  if (openBtn && closeBtn && formPopup) {
    openBtn.addEventListener("click", () => {
      formPopup.style.display = "flex";
    });

    closeBtn.addEventListener("click", () => {
      formPopup.style.display = "none";
    });
  }
});

