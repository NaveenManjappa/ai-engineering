import json

print(json.dumps(["foo", {"bar": ("baz", None, 1.0, 2)}]))

print(json.dumps('"foo\bar'))

config = {1: "primary_node", "tags": ("llm", "agent")}

with open("config.json", "w") as f:
    json.dump(config, f, indent=4)

with open("config.json", "r") as f:
    loaded_config = json.load(f)

print(loaded_config)

user_data = {"username": "Algo_driver", "scores": (98, 87, 92)}

# print(json.dumps(user_data))
print(json.loads(json.dumps(user_data)))
