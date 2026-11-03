import json
import os

TASK_FILE = 'tasks.json'

def _get_next_id(tasks):
    """Generates a unique ID for a new task."""
    return max([task['id'] for task in tasks]) + 1 if tasks else 1

def load_tasks():
    """Loads tasks from the JSON file. Returns an empty list if file doesn't exist or is corrupted."""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as f:
        try:
            tasks = json.load(f)
            # Ensure tasks is a list
            if not isinstance(tasks, list):
                return []
            return tasks
        except json.JSONDecodeError:
            # File exists but is not valid JSON
            return []

def save_tasks(tasks):
    """Saves the current list of tasks to the JSON file."""
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    """Adds a new task with the given description."""
    tasks = load_tasks()
    new_id = _get_next_id(tasks)
    task = {"id": new_id, "description": description, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    return task

def list_tasks():
    """Returns all tasks currently stored."""
    return load_tasks()

def complete_task(task_id):
    """Marks a task as completed based on its ID."""
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            found = True
            break
    if found:
        save_tasks(tasks)
    return found

def delete_task(task_id):
    """Deletes a task based on its ID."""
    tasks = load_tasks()
    initial_len = len(tasks)
    tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) < initial_len: # Task was deleted
        save_tasks(tasks)
        return True
    return False
