import requests
import time
start_time = time.time()
url="https://httpbin.org/delay/3"
response = requests.get(url,timeout=5)
if response.status_code == 200:
    response_time = time.time() - start_time
    response_time = round(response_time,2)
    if response_time > 1:
        print(f'Latency Identified: {response_time}sec')
    else:
        print(f'Response_time: {response_time}sec')