from google import genai
from dotenv import load_dotenv
import json

load_dotenv()

client = genai.Client()

reviews = [
    "The camera quality is amazing but the battery dies way too fast.-Naveen",
    "Loved the fast shipping! Item arrived in perfect condition.",
    "Customer support was unhelpful and rude. Will never buy it again. - Charlie",
    "Decent product for the price. Works as expected.",
    "Screen flickered out of the box.Had to return it immediately. - Dave",
    "",
]


def clean_json_string(text: str) -> str:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[-1]
    if cleaned.endswith("```"):
        cleaned.rsplit("\n", 1)[0]

    return cleaned.strip()


for i, review in enumerate(reviews):
    prompt = f"""
  Extract the following information from this customer review:
  - name (if not mentioned use "Unknown")
  - sentiment (positive,negative or neutral)
  - topics (array of topics mentioned)
  Return ONLY a JSON object with keys: "name","sentiment","topics".
  Review:{review}
  """

    max_retries = 3
    for attempt in range(max_retries):
        interaction = client.interactions.create(
            model="gemini-3.1-flash-lite", input=prompt
        )
        response_text = interaction.output_text
        print("Raw output", response_text)
        cleaned_text = clean_json_string(response_text)
        try:
            response_json = json.loads(cleaned_text)
            print(f"Review {i + 1} JSON:", response_json)
            break
        except json.JSONDecodeError as e:
            print(f"Review {i + 1} Attempt {attempt + 1} JSON decode error {e}")
            continue
