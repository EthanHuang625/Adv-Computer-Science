from flask import Flask, jsonify
import random
import json
import os

app = Flask(__name__)

# Load jokes from JSON file
DATA_PATH = os.path.join(os.path.dirname(__file__), "jokes.json")
try:
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        jokes = json.load(f)
except Exception:
    jokes = [
        {"Apparently you suck at coding. Come on. Lock in"}
    ]


@app.route("/")
def home():
    html_content = """
    <h1>Joke API</h1>
    <p>Welcome! Use the endpoints below to fetch jokes (JSON):</p>
    <ul>
      <li><code>/api/jokes</code> - returns all jokes</li>
      <li><code>/api/jokes/&lt;int:n&gt;</code> - returns n random jokes</li>
    </ul>
    """
    return html_content


@app.route("/api/jokes")
def all_jokes():
    return jsonify(jokes)


@app.route("/api/jokes/<int:n>")
def n_jokes(n: int):
    if n <= 0:
        return jsonify({"error": "n must be a positive integer"}), 400
    elif n > 10:
        return jsonify({"error": "n is too large; maximum is 10"}), 400
    selected = [random.choice(jokes) for i in range(n)]
    return jsonify(selected)

if __name__ == "__main__":
    app.run()