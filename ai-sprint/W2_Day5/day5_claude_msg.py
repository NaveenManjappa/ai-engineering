import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024,
    system="""
    You are an expert explainer of concepts. Always try to simply and explain in under 50 words.
    """,
    messages=[
        {"role": "user", "content": "Hello, Claude"},
        {"role": "assistant", "content": "Hello!"},
        {"role": "user", "content": "Can you describe llms to me?"},
    ],
)

print(message.content[0].text)
# for block in message.content:
#     if block.type == "text":
#         print(block.text)
