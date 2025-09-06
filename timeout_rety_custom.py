import time

from requests.exceptions import Timeout, RequestException
import requests
MAX_RETRIES = 5
TIMEOUT = 2

def call_service(MAX_RETRIES, TIMEOUT):
    url = "https://httpbin.org/delay/3"
    timeout_counter=0
    try:
        response = requests.get(url,timeout=TIMEOUT)
        print(f"Good Response {response.status_code}")
    except Timeout as e:
        print(f"Time out occured.")
        timeout_counter = timeout_counter + 1
    except Exception as e:
        print(f"URL not responding.")
    if timeout_counter >=5:
        time.sleep(10) # Sleep for 10 sec if the timeout happend for 5 times continously.
        print(f"Time out exceeded. Sleeping for 10 sec")
        # Resetting the counter
        timeout_counter = 0

if __name__ == "__main__":
    for i range()
    call_service(MAX_RETRIES,TIMEOUT)
