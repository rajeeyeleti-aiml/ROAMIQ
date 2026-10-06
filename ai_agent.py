import requests
import base64

OLLAMA_URL = "http://localhost:11434/api/generate"

TEXT_MODEL = "llama3.2"
VISION_MODEL = "llama3.2-vision"


def generate_challenge(activity="walking"):

    prompt = f"""
You are ROAMIQ, a voice-first outdoor AI companion.

The user is currently {activity}.

Create ONE simple and safe outdoor challenge.

The challenge should:
- encourage the user to look away from the screen
- involve walking, observing, finding, or interacting with surroundings
- take less than 5 minutes
- be easy to understand
- avoid dangerous activities

Return only the challenge sentence.
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": TEXT_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )

        response.raise_for_status()

        return response.json()["response"].strip()

    except Exception:
        return "Walk for two minutes and find something interesting around you."


def verify_photo(image_path, challenge):

    try:

        with open(image_path, "rb") as image_file:
            image_data = base64.b64encode(
                image_file.read()
            ).decode("utf-8")

        prompt = f"""
You are the vision verification system for ROAMIQ.

Outdoor challenge:
{challenge}

Look at the provided image.

Decide whether the image reasonably shows that the user completed
the challenge.

Return ONLY one of these:

YES - followed by a short reason

or

NO - followed by a short reason
"""

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": VISION_MODEL,
                "prompt": prompt,
                "images": [image_data],
                "stream": False
            },
            timeout=60
        )

        response.raise_for_status()

        return response.json()["response"].strip()

    except Exception:
        return "NO - Vision AI is not available yet."


if __name__ == "__main__":

    challenge = generate_challenge("walking")

    print("Challenge:")
    print(challenge)
