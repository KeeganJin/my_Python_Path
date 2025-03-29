from flask import Flask, request, jsonify, send_from_directory, abort
import os
from werkzeug.utils import secure_filename
from check_wfnet import check_wfnet

app = Flask(__name__, static_folder="static")

UPLOAD_FOLDER = "uploads"
TASK_FOLDER = "tasks"
SHARED_DESCRIPTION_FILE = "task_description.md"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# =========================
# ROUTE: Serve Frontend
# =========================
@app.route("/")
@app.route("/<path:path>")
def serve_static(path="index.html"):
    return send_from_directory(app.static_folder, path)


# =========================
# ROUTE: List all tasks
# =========================
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


# =========================
# ROUTE: Get task details
# =========================
@app.route("/tasks/<task_id>")
def get_task(task_id):
    task_path = os.path.join(TASK_FOLDER, task_id)
    if not os.path.exists(task_path):
        abort(404)

    # Load shared description
    shared_description_md = ""
    if os.path.exists(SHARED_DESCRIPTION_FILE):
        with open(SHARED_DESCRIPTION_FILE, "r", encoding="utf-8") as f:
            shared_description_md = f.read()

    # Translation PDF
    translation_file = ""
    for f in os.listdir(task_path):
        if f.startswith("translation_") and f.endswith(".pdf"):
            translation_file = f
            break
    translation_file_url = f"/tasks/{task_id}/{translation_file}" if translation_file else ""

    # Activity list (markdown)
    activity_md = ""
    for f in os.listdir(task_path):
        if f.startswith("activity_list_") and f.endswith(".md"):
            with open(os.path.join(task_path, f), "r", encoding="utf-8") as f_md:
                activity_md = f_md.read()
            break

    # Editable PNML (template)
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


# =========================
# ROUTE: Serve task files
# =========================
@app.route("/tasks/<task_id>/<filename>")
def serve_task_file(task_id, filename):
    return send_from_directory(os.path.join(TASK_FOLDER, task_id), filename)


# =========================
# ROUTE: WF-net validation only (drag & drop)
# =========================
@app.route("/validate", methods=["POST"])
def validate_wfnet():
    try:
        file = request.files.get("file")
        if not file:
            return jsonify({"error": "No file provided"}), 400

        temp_path = "temp_validate.pnml"
        file.save(temp_path)

        from check_wfnet import check_wfnet
        is_valid = check_wfnet(temp_path)

        os.remove(temp_path)

        return jsonify({"valid": is_valid})
    except Exception as e:
        print("Validation error:", e)
        return jsonify({"error": "Internal validation error"}), 500
# =========================
# ROUTE: Upload + validate (with override)
# =========================
@app.route("/upload", methods=["POST"])
def upload_file():
    task_id = request.form.get("task_id")
    user_id = request.form.get("user_id")
    email = request.form.get("email")
    override = request.form.get("override", "false").lower() == "true"
    file = request.files.get("file")

    if not all([task_id, user_id, email, file]):
        return jsonify({"error": "Missing required fields"}), 400

    # Prepare filename
    safe_email = email.replace("@", "_at_").replace(".", "_dot_")
    status = "override" if override else "original"
    filename = f"{task_id}_{user_id}_{safe_email}_{status}.pnml"

    # Save under task-specific folder
    task_upload_folder = os.path.join(UPLOAD_FOLDER, task_id)
    os.makedirs(task_upload_folder, exist_ok=True)

    temp_path = os.path.join(task_upload_folder, "temp_" + secure_filename(filename))
    file.save(temp_path)

    is_valid = check_wfnet(temp_path)
    if not is_valid and not override:
        os.remove(temp_path)
        return jsonify({"valid": False, "message": "File is not a valid WF-net"}), 400

    final_path = os.path.join(task_upload_folder, secure_filename(filename))
    os.rename(temp_path, final_path)

    return jsonify({"valid": is_valid, "uploaded": True})


# =========================
# Run the app (for local dev)
# =========================
if __name__ == "__main__":
    app.run(debug=True)
