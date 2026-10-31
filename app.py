from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "application": "Flask Backend",
        "status": "running",
        "message": "Flask application deployed successfully through Jenkins CI/CD"
    })

@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "flask-backend"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)