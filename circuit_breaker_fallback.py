from circuitbreaker import circuit
import random
import time

# Simulated flaky service
@circuit(failure_threshold=3, recovery_timeout=5)
def unreliable_service():
    if random.random() < 0.7:
        raise Exception("Service failed!")
    return "✅ Service succeeded"

# Fallback function
def fallback():
    return "⚠️ Fallback: Service is temporarily unavailable"

# Main loop
for i in range(10):
    try:
        result = unreliable_service()
    except Exception as e:
        result = fallback()
    print(f"[{i}] Result: {result}")
    time.sleep(1)