from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

@app.route("/tasks", methods=["GET", "POST"])
def tasks_api():
    if request.method == "POST":
        task = request.json.get("task")
        tasks.append(task)
        return {"message": "Task added"}, 201
    return jsonify(tasks)

app.run(host="0.0.0.0", port=5000)
