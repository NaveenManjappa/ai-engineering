from google import genai
from dotenv import load_dotenv
import time

load_dotenv()
client = genai.Client()


def stream_response(prompt):
    full_response = ""

    try:
        interactions = client.interactions.create(
            model="gemini-3.1-flash-lite", input=prompt, stream=True
        )
        print("called llm")

        for event in interactions:
            if event.event_type == "step.delta" and event.delta.type == "text":
                text_chunk = event.delta.text
                full_response += text_chunk
                print(text_chunk, end="", flush=True)
                time.sleep(2)
    except KeyboardInterrupt:
        print("\n Stream manually stopped")
    except Exception as e:
        print("Stream interrupted")

    return full_response


result = stream_response("Explain AI in two sentences")
print(result)
