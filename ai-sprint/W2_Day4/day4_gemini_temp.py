from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

response = client.interactions.create(
    model="gemini-3.1-flash-lite",
    input="Explain how AI works in under 80 words",
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 500
                },
)
print(response.output_text)
#print(response)
