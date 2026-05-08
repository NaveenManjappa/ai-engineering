from openai import OpenAI
client = OpenAI()

response = client.responses.create(
  model="gpt-5-nano",
  tools = [{"type":"web_search"}],
  input="Who won the IPL match yesterday? Just give me the details in 2 sentences"
)

print(response.output_text)