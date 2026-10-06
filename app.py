from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Outdoor challenges for ROAMIQ
challenges = [
    "Walk for 3 minutes and find something yellow around you.",
    "Find a green leaf and observe its shape.",
    "Walk for 2 minutes and look for a red object in nature.",
    "Find a tree and observe its bark carefully.",
    "Walk 200 steps and look for a bird.",
    "Find something that can be recycled.",
    "Walk to a shaded area and spend one quiet minute observing nature.",
    "Find two different types of leaves around you."
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/challenge")
def get_challenge():
    challenge = random.choice(challenges)

    return jsonify({
        "challenge": challenge
    })


if __name__ == "__main__":
    app.run(debug=True)
