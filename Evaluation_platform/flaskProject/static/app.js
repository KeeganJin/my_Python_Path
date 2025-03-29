let tasks = [];
let currentTaskId = null;

// Save user info and load tasks
function saveUserInfo() {
  const userId = document.getElementById("userId").value.trim();
  const email = document.getElementById("email").value.trim();
  if (!userId || !email) return alert("Please enter your ID and email.");

  localStorage.setItem("userId", userId);
  localStorage.setItem("email", email);
  loadTasks();
}


function showUserInfo() {
  // Show the user info form again
  document.getElementById("task-list").classList.add("hidden");
  document.getElementById("user-info").classList.remove("hidden");

  // Pre-fill existing values from localStorage
  const storedId = localStorage.getItem("userId") || "";
  const storedEmail = localStorage.getItem("email") || "";
  document.getElementById("userId").value = storedId;
  document.getElementById("email").value = storedEmail;
}


// Load task list from backend
function loadTasks() {
  fetch("/tasks")
    .then(res => res.json())
    .then(data => {
      tasks = data;
      showTaskList();
    })
    .catch(() => alert("Failed to load tasks."));
}

// Show task list
function showTaskList() {
  document.getElementById("user-info").classList.add("hidden");
  document.getElementById("task-list").classList.remove("hidden");

  const uploaded = JSON.parse(localStorage.getItem("uploadedTasks") || "[]");
  const taskList = document.getElementById("tasks");
  taskList.innerHTML = "";

  tasks.forEach(task => {
    const li = document.createElement("li");
    li.innerHTML = `
      <span>${task.title}</span>
      ${uploaded.includes(task.id) ? "✅ Uploaded" : ""}
      <button onclick="showTaskDetail('${task.id}')">Open</button>
    `;
    taskList.appendChild(li);
  });
}

// Show task detail
function showTaskDetail(taskId) {
  fetch(`/tasks/${taskId}`)
    .then(res => res.json())
    .then(task => {
      document.getElementById("task-list").classList.add("hidden");
      document.getElementById("task-detail").classList.remove("hidden");

      document.getElementById("taskTitle").innerText = task.title;

      // Shared markdown description
      document.getElementById("descriptionBlock").innerHTML = marked.parse(task.shared_description_md || "");

      // Translation PDF
      const viewer = document.getElementById("translationViewer");
      viewer.src = task.translation_file_url;
      document.getElementById("translationDownload").href = task.translation_file_url;

      // Activity list (markdown)
      document.getElementById("activityListBlock").innerHTML = marked.parse(task.activity_md || "");

      // PNML download link
      document.getElementById("pnmlDownload").href = task.editable_pnml_url;

      currentTaskId = task.id;
      clearStatus();
    });
}

// Go back to task list
function goBack() {
  document.getElementById("task-detail").classList.add("hidden");
  document.getElementById("task-list").classList.remove("hidden");
  clearStatus();
}

// Clear upload + validation messages
function clearStatus() {
  document.getElementById("checkResult").innerText = "";
  document.getElementById("uploadStatus").innerText = "";
  document.getElementById("uploadInput").value = "";
  document.getElementById("override").checked = false;
}

// Drag & drop validation
const dropZone = document.getElementById("dragDrop");

dropZone.addEventListener("dragover", e => {
  e.preventDefault();
  dropZone.classList.add("active");
});

dropZone.addEventListener("dragleave", () => {
  dropZone.classList.remove("active");
});

dropZone.addEventListener("drop", e => {
  e.preventDefault();
  dropZone.classList.remove("active");

  const file = e.dataTransfer.files[0];
  if (!file) return;

  validateFile(file);
});

function validateFile(file) {
  const formData = new FormData();
  formData.append("file", file);

  fetch("/validate", {
    method: "POST",
    body: formData,
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("checkResult").innerText = data.valid
        ? "✅ This is a valid WF-net!"
        : "❌ Not a valid WF-net.";
    })
    .catch(() => {
      document.getElementById("checkResult").innerText = "❌ Error during validation.";
    });
}

// Upload file
function uploadFile() {
  const file = document.getElementById("uploadInput").files[0];
  const override = document.getElementById("override").checked;
  const user_id = localStorage.getItem("userId");
  const email = localStorage.getItem("email");
  if (!file || !currentTaskId) return;

  const formData = new FormData();
  formData.append("file", file);
  formData.append("user_id", user_id);
  formData.append("email", email);
  formData.append("task_id", currentTaskId);
  formData.append("override", override);

  fetch("/upload", { method: "POST", body: formData })
    .then(async res => {
      const data = await res.json();
      if (res.ok) {
        document.getElementById("uploadStatus").innerText = "✅ Uploaded!";
        const uploaded = JSON.parse(localStorage.getItem("uploadedTasks") || "[]");
        if (!uploaded.includes(currentTaskId)) {
          uploaded.push(currentTaskId);
          localStorage.setItem("uploadedTasks", JSON.stringify(uploaded));
        }
      } else {
        document.getElementById("uploadStatus").innerText = "❌ " + (data.message || "Upload failed.");
      }
    })
    .catch(() => {
      document.getElementById("uploadStatus").innerText = "❌ Upload error.";
    });
}

// --- Drag-and-Drop for Upload Section ---
const uploadDropZone = document.getElementById("uploadDropZone");

uploadDropZone.addEventListener("dragover", e => {
  e.preventDefault();
  uploadDropZone.classList.add("active");
});

uploadDropZone.addEventListener("dragleave", () => {
  uploadDropZone.classList.remove("active");
});

uploadDropZone.addEventListener("drop", e => {
  e.preventDefault();
  uploadDropZone.classList.remove("active");

  const file = e.dataTransfer.files[0];
  if (!file) return;

  // Place dropped file into the upload input for reusability
  const uploadInput = document.getElementById("uploadInput");
  const dataTransfer = new DataTransfer();
  dataTransfer.items.add(file);
  uploadInput.files = dataTransfer.files;

  // Optionally auto-upload here:
  // uploadFile();
});

