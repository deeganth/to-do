# 📝 Automated To-Do Reminder System (Python)

A simple yet powerful **command-line based To-Do Reminder System** built with Python.
This application allows users to add tasks with specific date & time and receive **desktop notifications** when the task is due.

---

## 🚀 Features

* ✅ Add tasks with date & time
* 📋 View all scheduled tasks
* 🔔 Automatic desktop notifications
* 💾 Persistent storage using JSON
* ⚡ Background scheduler running continuously

---

## 📁 Project Structure

```
todo_reminder/
│── main.py          # CLI interface
│── scheduler.py     # Task scheduler logic
│── notifier.py      # Notification system
│── tasks.json       # Task storage
```

---

## 🛠️ Requirements

* Python 3.x
* Required libraries:

```bash
pip install plyer schedule
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/deeganth/todo-reminder.git
cd todo-reminder
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

---

## 🧑‍💻 Usage

### 1. Add a Task

* Enter task name
* Enter date & time in format:

```
YYYY-MM-DD HH:MM
```

### 2. View Tasks

* Displays all tasks with their status

### 3. Automatic Reminder

* The system checks every minute
* Sends notification when task time matches current time

---

## 🔔 Example

```
Enter task: Submit project
Enter time: 2026-03-30 18:30
```

At **6:30 PM**, you will receive a desktop notification.

---

## ⚙️ How It Works

* Tasks are stored in `tasks.json`
* A background thread runs the scheduler
* Every minute:

  * Current time is checked
  * Matching tasks trigger notifications
  * Task is marked as "notified"

---

## 📌 Future Enhancements

* 📧 Email notifications
* 📱 SMS/WhatsApp reminders
* 🖥️ GUI (Tkinter / PyQt)
* 🔁 Recurring tasks
* ⭐ Priority levels

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 💡 Author

Your Name
GitHub: https://github.com/deeganth
---
