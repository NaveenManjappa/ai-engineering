from openai import OpenAI
client = OpenAI()

def get_weather(city):
  return f"Weather in {city} today is 23c"
  
tools = [
  {
    "type":"function",
    "name":"get_weather",
    "description":"Get current temperature for a given location",
    "parameters":{
      "type":"object",
      "properties":{
        "location":{
          "type":"string",
          "description":"City and country e.g. Bogota,Columbia"
        }
      },
      "required":["location"],
      "additionalProperties":False,
    },
    "strict":True,
  },
]

response = client.responses.create(
  model="gpt-5-nano",
  input = [
    {"role":"user","content":"What is the weather like in Paris in today?"}
  ],
  tools=tools
)
print(response.output[0].to_json())