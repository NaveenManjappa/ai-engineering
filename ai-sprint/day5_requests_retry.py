import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get("API_KEY")
api_url = os.environ.get("API_URL")

headers = {"Authorization": f"Bearer {api_key}"}


retry_strategy = Retry(total=1, status_forcelist=[500, 502, 503, 504], backoff_factor=1)

session = requests.Session()
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)
session.headers.update(headers)


try:
    # response = session.get("https://httpbin.org/delay/5", timeout=(3.05, 0.3))
    # response = session.get("https://httpbin.org/status/404")
    # response = requests.get("https://httpbin.org/delay/5", timeout=(3.05, 0.3))
    #response = session.get("https://thisdomaindoesnotexist12345.com")
    response = session.get("https://httpbin.org/status/500")
    response.raise_for_status()
    print("Fetched successfully!")

except requests.exceptions.Timeout:
    print("The request timed out!")
except requests.exceptions.RetryError:
    print("Retry failed after maximum retries")
except requests.exceptions.ConnectionError as error:
    print(f"Connection error {error}")
except requests.exceptions.HTTPError as error:
    print(f"Http Error: {error}")
