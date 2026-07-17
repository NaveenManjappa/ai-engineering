import requests

url = "https://httpbin.org/get"
query_params = {"search": "python", "page": "1"}
response = requests.get(url, params=query_params)

# print(response.status_code)

url = "https://httpbin.org/post"
custom_headers = {"Content-Type": "application/json", "User-Agent": "MyTestApp/1.0"}

payload = {"language": "Python", "library": "requests"}

response = requests.post(url=url, json=payload, headers=custom_headers)

if response.ok:
    data = response.json()
    print(data["json"])
else:
    print(f"Request failed with status: {response.status_code}")

# data = response.json()

# print(data["json"])
