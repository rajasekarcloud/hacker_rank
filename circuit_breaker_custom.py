import random
import time
from datetime import datetime
def working_service():
    if random.random() < 0.5:
        print(f"Request Completed - {datetime.now()}")
    else:
        raise Exception("Request Could Not Be Completed.")

def queue_service():
    print(f"Circuit Breaker Triggered. Request Queued And It Will Be Processed Later - {datetime.now()}")
    # Recovery time
    time.sleep(10)

fail_count = 0
for i in range(10):
    try:
        working_service()
    except Exception as e:
        fail_count = fail_count + 1
        if fail_count >=3:
            queue_service()
            fail_count = 0
        else:
            print(f"Request Failed. Circuit Breaker Not Triggered - {datetime.now()}")