from datetime import datetime

def log_request(user_input):
    print(
        f"[{datetime.now()}] "
        f"User Input: {user_input}"
)