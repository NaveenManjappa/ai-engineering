import time
import functools


def retry(max_retry=3,exceptions=(ConnectionError)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_retry):
                try:
                    result = func(*args, **kwargs)
                    return result
                except (KeyError, ValueError):
                    raise
                except Exception as e:
                    if isinstance(e,exceptions):
                      if i == max_retry - 1:
                        raise
                      time.sleep(2**i)
                    else:
                        raise

        return wrapper

    return decorator


attempts = 0


@retry(max_retry=3,exceptions=(ConnectionError))
def fetch_api_data(endpoint):
    global attempts
    attempts += 1
    print(f"Executing fetch_api_data for {endpoint}")
    if attempts < 3:
        raise RuntimeError("Temporary 503 Service Unavailable")
    return {"status": "success", "data": "LLM response"}


try:
    response = fetch_api_data("https://api.example.com/v1/chat")
    print(f"Success result: {response}")
except Exception as final_err:
    print(f"Failed completely: {final_err}")
