from flask import Flask, request, send_from_directory, jsonify
import os
from werkzeug.utils import secure_filename
from check_wfnet import check_wfnet  # You'll create this
from flask import abort


app = Flask(__name__, static_folder="static")
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
TASK_FOLDER = "tasks"


# Serve frontend files
@app.route("/")
@app.route("/<path:path>")
def serve_static(path="index.html"):
    return send_from_directory(app.static_folder, path)


@app.route("/tasks")
def list_tasks():
    tasks = []
    for folder in os.listdir(TASK_FOLDER):
        task_path = os.path.join(TASK_FOLDER, folder)
        if os.path.isdir(task_path):
            tasks.append({
                "id": folder,
                "title": folder.replace("task_id_", "Task ").replace("_", ".")
            })
    return jsonify(tasks)


@app.route("/tasks/<task_id>")
def get_task(task_id):
    task_path = os.path.join(TASK_FOLDER, task_id)
    if not os.path.exists(task_path):
        abort(404)

    # Load shared task description
    shared_description_md = ""
    if os.path.exists("task_description.md"):
        with open("task_description.md", "r", encoding="utf-8") as file:
            shared_description_md = file.read()

    # Load translation PDF filename
    translation_file = ""
    for f in os.listdir(task_path):
        if f.startswith("translation_") and f.endswith(".pdf"):
            translation_file = f
            break
    translation_file_url = f"/tasks/{task_id}/{translation_file}" if translation_file else ""

    # Load activity list markdown
    activity_md = ""
    for f in os.listdir(task_path):
        if f.startswith("activity_list_") and f.endswith(".md"):
            with open(os.path.join(task_path, f), "r", encoding="utf-8") as file:
                activity_md = file.read()
            break

    # Load editable Petri net PNML (shared template)
    editable_pnml = ""
    for f in os.listdir(task_path):
        if f.startswith("user_eval_net_") and f.endswith(".pnml"):
            editable_pnml = f
            break
    editable_pnml_url = f"/tasks/{task_id}/{editable_pnml}" if editable_pnml else ""

    return jsonify({
        "id": task_id,
        "title": task_id.replace("task_id_", "Task ").replace("_", "."),
        "shared_description_md": shared_description_md,
        "translation_file_url": translation_file_url,
        "activity_md": activity_md,
        "editable_pnml_url": editable_pnml_url
    })
@app.route("/tasks/<task_id>/<filename>")
def serve_task_file(task_id, filename):
    return send_from_directory(os.path.join(TASK_FOLDER, task_id), filename)


# Handle upload with optional validation
@app.route("/upload", methods=["POST"])
def upload_file():
    task_id = request.form.get("task_id")
    user_id = request.form.get("user_id")
    email = request.form.get("email")
    override = request.form.get("override", "false").lower() == "true"
    file = request.files.get("file")

    if not all([task_id, user_id, email, file]):
        return jsonify({"error": "Missing required fields"}), 400

    # Sanitize email
    safe_email = email.replace("@", "_at_").replace(".", "_dot_")
    status = "override" if override else "original"
    filename = f"{task_id}_{user_id}_{safe_email}_{status}.pnml"

    # Create task-specific folder
    task_folder = os.path.join("uploads", task_id)
    os.makedirs(task_folder, exist_ok=True)

    # Save temporarily for validation
    temp_path = os.path.join(task_folder, "temp_" + filename)
    file.save(temp_path)

    # Run WF-net validation
    is_valid = check_wfnet(temp_path)
    if not is_valid and not override:
        os.remove(temp_path)
        return jsonify({"valid": False, "message": "File is not a valid WF-net"}), 400

    # Move validated file to final path
    final_path = os.path.join(task_folder, filename)
    os.rename(temp_path, final_path)

    return jsonify({"valid": is_valid, "uploaded": True}), 200



if __name__ == "__main__":
    app.run(debug=True)
