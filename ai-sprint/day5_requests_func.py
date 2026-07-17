import requests

url = "https://httpbin.org/status/404"


def send_post_request(payload):
    try:
        custom_headers = {
            "Content-Type": "application/json",
            "User-Agent": "MyTestApp/1.0",
        }
        response = requests.post(url=url, json=payload, headers=custom_headers)
        response.raise_for_status()
        print("Success")
    except requests.exceptions.HTTPError as error:
        print(f"Error happened {error}")


payload = {"language": "Python", "library": "requests"}
send_post_request(payload)
