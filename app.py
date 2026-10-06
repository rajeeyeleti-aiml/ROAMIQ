
from flask import Flask, render_template, jsonify
from ai_agent import generate_challenge

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/challenge")
def get_challenge():
    challenge = generate_challenge("walking")

    return jsonify({
        "challenge": challenge
    })


if __name__ == "__main__":
    app.run(debug=True)
