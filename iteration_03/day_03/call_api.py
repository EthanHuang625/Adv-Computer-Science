from flask import Flask, jsonify
import requests

app = Flask(__name__)
# Use requests package to call your api address http://127.0.0.1:5000/api/joke to display a funny joke

@app.route("/api/joke/3")
def joke():
    url = "http://127.0.0.1:5000/api/joke/3"
    response = requests.get(url)
    data = response.json()

    print(f"Here's a joke for you: {data['setup']}")
    print(f"Punchline: {data['punchline']}")
    return jsonify(data)

app.run()