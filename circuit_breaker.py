from circuitbreaker import circuit
import random

# Simulated flaky service
@circuit(failure_threshold=3, recovery_timeout=5)
def unreliable_service():
    if random.random() < 0.7:
        raise Exception("Service failed!")
    return "Success!"

# Test loop
for i in range(10):
    try:
        result = unreliable_service()
        print(f"[{i}] Call succeeded: {result}")
    except Exception as e:
        print(f"[{i}] Call failed: {e}")