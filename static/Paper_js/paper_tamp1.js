document.addEventListener("DOMContentLoaded", function () {
  const openBtn = document.getElementById("openFormBtn");
  const closeBtn = document.getElementById("closeFormBtn");
  const formPopup = document.getElementById("formPopup");
  const openTriggers = document.querySelectorAll("[data-open-form]");

  function openFormPopup() {
    if (formPopup) {
      formPopup.style.display = "flex";
    }
  }

  function closeFormPopup() {
    if (formPopup) {
      formPopup.style.display = "none";
    }
  }

  if (openBtn && formPopup) {
    openBtn.addEventListener("click", openFormPopup);
  }

  openTriggers.forEach((trigger) => {
    trigger.addEventListener("click", openFormPopup);
  });

  // Popup toggle - sirf popup open/close ka code
  if (closeBtn && formPopup) {
    closeBtn.addEventListener("click", () => {
      closeFormPopup();
    });

    formPopup.addEventListener("click", (event) => {
      if (event.target === formPopup) {
        closeFormPopup();
      }
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        closeFormPopup();
      }
    });
  }
});

