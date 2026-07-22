from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "I have two dogs at home"}],
    }
]

interaction1 = client.interactions.create(
    model="gemini-3.1-flash-lite", store=False, input=history
)

print("Response 1",interaction1.steps[-1].content[0].text)

for step in interaction1.steps:
  history.append(step.model_dump())

#print(history)

history.append({
  "type":"user_input",
  "content":[{"type":"text","text":"How many paws are there in my house?"}]
})

interaction2 = client.interactions.create(
  model="gemini-3.1-flash-lite",store=False,input=history
)

print("Response 2",interaction2.steps[-1].content[0].text)