from datetime import datetime
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), "activity_log.txt")


def write_log(username, action):



    with open(LOG_FILE, "a", encoding="utf-8") as file:

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(f"{time} - {username} - {action}\n")