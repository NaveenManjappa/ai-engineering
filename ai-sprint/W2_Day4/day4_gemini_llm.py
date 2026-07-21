from google import genai
from dotenv import load_dotenv
import json
import time

load_dotenv()

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash", input="Explain how AI works in few words", stream=True
)
for event in interaction:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            #time.sleep(5)
            print(event.delta.text, end="", flush=True)

# print(json.dumps(interaction.model_dump(), indent=2))
