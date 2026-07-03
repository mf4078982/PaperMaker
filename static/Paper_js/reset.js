
document.addEventListener("DOMContentLoaded", function() {
  const resetBtn = document.querySelector(".reset-btn");
  const worksheet = document.getElementById("worksheet");

  if (resetBtn && worksheet) {
    resetBtn.addEventListener("click", function() {
      if (confirm("Are you sure you want to reset the paper?")) {
        worksheet.innerHTML = ""; // removes all question blocks
      }
    });
  }
});
