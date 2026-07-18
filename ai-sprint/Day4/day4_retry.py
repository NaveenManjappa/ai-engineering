import time
import random


def always_succeeds():
    print("Operation succeeded")
    return "ok"


def fails_once_then_succeeds():
    if not hasattr(fails_once_then_succeeds, "called"):
        fails_once_then_succeeds.called = 0

    fails_once_then_succeeds.called += 1
    if fails_once_then_succeeds.called == 1:
        raise ConnectionError("temporary network issue")

    print("Succeeded on retry")
    return "ok"


def always_fails():
    raise RuntimeError("persistent failure")


def always_valueerror():
    raise ValueError("Value error")


def fails_with_probability(p=0.7):
    if random.random() < p:
        raise TimeoutError("temporary timeout")
    return "ok"


def flaky_call(func, max_retry=3, delay=1):
    for i in range(max_retry):
        try:
            print("try something")
            return func()
        except (KeyError, ValueError):
            print("Value error caught")
            raise
        except Exception as e:
            print(f"Attemp {i + 1} failed due to transient error {e}")
            if i == max_retry - 1:
                raise
            time.sleep(2**i)


flaky_call(always_valueerror)
