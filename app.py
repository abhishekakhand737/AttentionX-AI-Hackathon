# ==========================
# Flask App Starter
# ==========================

from flask import Flask, request, jsonify

app = Flask(__name__)

# ==========================
# Routes
# ==========================

@app.route("/")
def home():
    return "Attention-X AI Backend Running 🚀"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    content = data.get("content", "")

    # TODO: Add AI logic here
    result = {
        "attention_score": 50,
        "wisdom_score": 50,
        "classification": "Neutral"
    }

    return jsonify(result)

# ==========================
# Run Server
# ==========================

if __name__ == "__main__":
    app.run(debug=True)
    