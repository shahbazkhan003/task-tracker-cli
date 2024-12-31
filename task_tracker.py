import os
import json
import sys
from datetime import datetime

if not os.path.exists("task.json"):
    with open("task.json", "w") as file:
        json.dump([], file)  # Empty list to store tasks

def load_tasks():
    with open("task.json", "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open("task.json", "w") as file:
        json.dump(tasks, file, indent=4)

def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")



def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": current_time(),
        "updatedAt": current_time()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

    import sys

if len(sys.argv) < 2:
    print("Usage: task-cli <command> [arguments]")
    sys.exit(1)

command = sys.argv[1]

if command == "add":
    description = " ".join(sys.argv[2:])
    add_task(description)