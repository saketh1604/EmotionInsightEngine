import requests
from datetime import date, timedelta
import sys

BASE_URL = "http://127.0.0.1:8000"

def add_mood(mood_date, mood_str):
    response = requests.post(f"{BASE_URL}/moods", json={"date": str(mood_date), "mood": mood_str})
    if response.status_code != 200:
        print(f"Failed to add mood for {mood_date}: {response.text}")
    return response.json()

def get_streak():
    response = requests.get(f"{BASE_URL}/moods/streak")
    if response.status_code != 200:
        print(f"Failed to get streak: {response.text}")
        return -1
    return response.json()["streak_count"]

def run_tests():
    print("Running tests...")
    
    # Note: This test assumes a clean DB or at least doesn't conflict with existing data too much.
    # Ideally we'd clear the DB first, but for this quick check we'll just try to add data.
    # If the DB is persistent, we might need to be careful.
    # Let's assume we can add moods.
    
    today = date.today()
    yesterday = today - timedelta(days=1)
    day_before = today - timedelta(days=2)
    
    print(f"Adding mood for today ({today})...")
    add_mood(today, "Happy")
    
    print(f"Adding mood for yesterday ({yesterday})...")
    add_mood(yesterday, "Neutral")
    
    print(f"Adding mood for day before ({day_before})...")
    add_mood(day_before, "Sad")
    
    streak = get_streak()
    print(f"Streak: {streak}")
    
    if streak >= 3:
        print("PASS: Streak is at least 3 (assuming no gaps from previous runs)")
    else:
        print("FAIL: Streak should be at least 3")

    # Test broken streak
    # We can't easily "un-add" data without a delete endpoint or direct DB access.
    # So we'll just verify the positive case for now.
    
if __name__ == "__main__":
    run_tests()
