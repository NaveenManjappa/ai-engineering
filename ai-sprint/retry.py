import functools
import random
import time
import logging
import os

VALID_LEVELS = {"DEBUG","WARNING","INFO","ERROR","CRITICAL"}
env_level = os.environ.get("LOG_LEVEL","WARNING").upper()
log_level = env_level if env_level in VALID_LEVELS else "WARNING"
logging.basicConfig(
    level=log_level,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("RetryLogger")

class Retry:
    def __init__(self, max_retry, exceptions=(ConnectionError)):
        self.max_retry = max_retry
        self.exceptions = exceptions

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(self.max_retry):
                try:
                    randomize = random.uniform(0, 1)
                    result = func(*args, **kwargs)
                    return result               
                except Exception as e:
                    if isinstance(e, self.exceptions):
                        if i == self.max_retry - 1:
                            logger.error(f"Max retry attempts reached, Error {e}")
                            raise
                        logger.warning(f"Attempt {i + 1} failed with the error {e}")
                        time.sleep(2**i + randomize)
                    else:
                        raise

        return wrapper
