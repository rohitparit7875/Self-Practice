Rest appear to save the status dotfrom flask import Flask, jsonify

app = Flask(__name__)

@app.route("/status")
def status():
    return jsonify({
        "service": "python-api",
        "status": "running"
    })

app.run(host="0.0.0.0", port=5000)
