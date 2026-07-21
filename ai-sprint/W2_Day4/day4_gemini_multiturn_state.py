from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

# Server side state
interaction1 = client.interactions.create(
  model="gemini-3.5-flash",
  input="I have two dogs in my house named Jee and Juu"
)

print("Response 1:",interaction1.output_text)

interaction2 = client.interactions.create(
  model="gemini-3.5-flash",
  input="What are the names of my dogs?",
  previous_interaction_id=interaction1.id
)


print("Response 2:",interaction2.output_text)