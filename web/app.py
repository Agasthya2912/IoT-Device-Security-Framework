from flask import Flask, render_template, request, jsonify
from backend.iot_core import handle_request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    status, result = handle_request(data["device_id"], data["message"])
    return jsonify({"status": status, "result": result})

if __name__ == "__main__":
    app.run(debug=True)
