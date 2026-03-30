import json
from datetime import datetime
from scheduler import run_scheduler
import threading

TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task():
    task_name = input("Enter task: ")
    task_time = input("Enter time (YYYY-MM-DD HH:MM): ")

    try:
        datetime.strptime(task_time, "%Y-%m-%d %H:%M")
    except:
        print("❌ Invalid time format")
        return

    tasks = load_tasks()
    tasks.append({
        "task": task_name,
        "time": task_time,
        "notified": False
    })

    save_tasks(tasks)
    print("✅ Task added!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t['task']} at {t['time']} | Notified: {t['notified']}")

def menu():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    # Run scheduler in background
    t = threading.Thread(target=run_scheduler, daemon=True)
    t.start()

    menu()