import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"


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
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )

        response.raise_for_status()

        result = response.json()

        return result["response"].strip()

    except Exception:
        return "Walk for two minutes and find something interesting around you."


if __name__ == "__main__":
    challenge = generate_challenge("walking")
    print(challenge)
