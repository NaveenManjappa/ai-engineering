import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

message = client.messages.create(
  model="claude-haiku-4-5-20251001",
  max_tokens=500,
  messages=[
    {
      "role":"user",
      "content":"Explain me what is a neural network in under 100 words"
    }
  ]
)
#print(message)
for block in message.content:
  if block.type == "text":
    print(block.text)