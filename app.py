from flask import Flask, render_template, jsonify, request
from ai_agent import generate_challenge, verify_photo
import tempfile
import os

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


@app.route("/verify", methods=["POST"])
def verify():

    if "photo" not in request.files:
        return jsonify({
            "result": "NO - No photo received."
        })

    photo = request.files["photo"]

    if photo.filename == "":
        return jsonify({
            "result": "NO - No photo selected."
        })

    challenge = request.form.get(
        "challenge",
        ""
    )

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    )

    try:

        photo.save(temp_file.name)

        result = verify_photo(
            temp_file.name,
            challenge
        )

        return jsonify({
            "result": result
        })

    finally:

        temp_file.close()

        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)


if __name__ == "__main__":
    app.run(debug=True)

