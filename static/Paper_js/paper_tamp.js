// Title Edit / Save
const paperTitle = document.getElementById("paperTitle");
const editBtn = document.getElementById("editBtn");
const titleInput = document.getElementById("titleInput");
const saveBtn = document.getElementById("saveBtn");

// ✅ Ensure they start hidden
if (titleInput && saveBtn) {
  titleInput.style.display = "none";
  saveBtn.style.display = "none";
}

if (editBtn && saveBtn && titleInput && paperTitle) {
  editBtn.addEventListener("click", () => {
    titleInput.style.display = "inline-block";
    saveBtn.style.display = "inline-block";
    titleInput.value = paperTitle.textContent;
    paperTitle.style.display = "none";
    editBtn.style.display = "none";
  });

  saveBtn.addEventListener("click", () => {
    paperTitle.textContent = titleInput.value || "Untitled Paper";
    titleInput.style.display = "none";
    saveBtn.style.display = "none";
    paperTitle.style.display = "inline-block";
    editBtn.style.display = "inline-block";
  });
}
