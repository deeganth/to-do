import schedule
import time
import json
from datetime import datetime
from notifier import send_notification

TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def check_tasks():
    tasks = load_tasks()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    for task in tasks:
        if task["time"] == now and not task["notified"]:
            send_notification("Reminder", task["task"])
            task["notified"] = True

    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def run_scheduler():
    schedule.every(1).minutes.do(check_tasks)

    print("⏳ Reminder system running...")
    while True:
        schedule.run_pending()
        time.sleep(1)