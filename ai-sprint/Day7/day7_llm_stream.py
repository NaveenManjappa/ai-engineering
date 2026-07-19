import time
import random

def fake_llm_stream(text,stop_word=None):
    words = text.split()
    for word in words:
        time.sleep(random.uniform(0.1,0.8))
        if word == stop_word:
            break
        yield word


text = "This is the best day ever"

generator_object = fake_llm_stream(text)
for item in generator_object:
    print(item, end=" ", flush=True)
