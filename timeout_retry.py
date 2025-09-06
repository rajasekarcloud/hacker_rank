import requests
from requests.exceptions import Timeout, RequestException
import time

# Retry configuration
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds

# Target URL
url = "https://httpbin.org/delay/3"  # Simulates a 3-second delay

for attempt in range(1, MAX_RETRIES + 1):
    try:
        print(f"Attempt {attempt}: Sending request...")
        response = requests.get(url, timeout=2)  # Set timeout to 2 seconds
        print("✅ Success:", response.status_code)
        break  # Exit loop on success
    except Timeout as e:
        print(f"⏱️ Timeout occurred. Retrying... {e}")
    except RequestException as e:
        print(f"❌ Request failed: {e}")
    time.sleep(RETRY_DELAY)
else:
    print("🚨 All retries failed. Giving up.")