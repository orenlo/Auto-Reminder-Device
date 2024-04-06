import json
from datetime import datetime
import random

# Define sample data
user_list = ["User1", "User2", "User3"]
gps_list = ["Location1", "Location2", "Location3"]
count_yes = random.randint(0, 10)  # Sample count for "Got_back"
count_general = random.randint(0, 10)  # Sample count for "forgot"

# Generate a random timestamp
random_time = datetime.now()

# Create a dictionary to represent the message data
message_data = {
    "time": int(random_time.timestamp()),  # Convert timestamp to Unix timestamp
    "user_name": random.choice(user_list),  # Select a random user name from the list
    "location": random.choice(gps_list),   # Select a random location from the list
    "Got_back": count_yes,   # Count for "Got_back"
    "forgot": count_general   # Count for "forgot"
}

# Convert the dictionary to a JSON string
message_json = json.dumps(message_data)

# Print the JSON string
print("Generated JSON message:")
print(message_json)
