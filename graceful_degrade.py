import requests
import json

# Primary function: fetch user data from external API
def get_user_data_from_api(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, json.JSONDecodeError) as e:
        print(f"⚠️ API error: {e}")
        return None

# Fallback function: return local or default data
def get_fallback_user_data(user_id):
    fallback_data = {
        1: {"name": "John Doe", "email": "john@example.com"},
        2: {"name": "Jane Smith", "email": "jane@example.com"},
    }
    return fallback_data.get(user_id, {"name": "Unknown", "email": "unknown@example.com"})

# Wrapper: handles graceful degradation
def get_user_data(user_id):
    data = get_user_data_from_api(user_id)
    if data:
        print("✅ Data retrieved from API")
        return data
    else:
        print("🔁 Using fallback data")
        return get_fallback_user_data(user_id)

# Main execution
if __name__ == "__main__":
    user_id = 13
    user_data = get_user_data(user_id)
    print(f"\nUser {user_id} Info:")
    print(f"Name: {user_data['name']}")
    print(f"Email: {user_data['email']}")