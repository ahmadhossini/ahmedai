import pytest
import json
import os
from task_manager import load_tasks, save_tasks, add_task, list_tasks, complete_task, delete_task, TASK_FILE

# Fixture to manage a temporary task file for testing
@pytest.fixture
def temp_task_file(tmp_path, monkeypatch):
    test_file_path = tmp_path / "test_tasks.json"
    # Temporarily change TASK_FILE constant in task_manager.py
    monkeypatch.setattr('task_manager.TASK_FILE', str(test_file_path))
    # Ensure the file doesn't exist at the start of the test
    if test_file_path.exists():
        test_file_path.unlink()
    yield
    # Clean up after the test
    if test_file_path.exists():
        test_file_path.unlink()


def test_load_tasks_empty_file(temp_task_file):
    # File doesn't exist initially
    tasks = load_tasks()
    assert tasks == []
    # Create an empty but existing file
    open(temp_task_file, 'a').close()
    tasks = load_tasks()
    assert tasks == []

def test_load_tasks_corrupted_json(temp_task_file):
    with open(TASK_FILE, 'w') as f:
        f.write("{invalid json")
    tasks = load_tasks()
    assert tasks == []

def test_load_tasks_not_list(temp_task_file):
    with open(TASK_FILE, 'w') as f:
        json.dump({"key": "value"}, f)
    tasks = load_tasks()
    assert tasks == []

def test_save_tasks(temp_task_file):
    tasks_data = [{"id": 1, "description": "Test Task", "completed": False}]
    save_tasks(tasks_data)
    with open(TASK_FILE, 'r') as f:
        loaded_data = json.load(f)
    assert loaded_data == tasks_data

def test_add_task(temp_task_file):
    task1 = add_task("Buy groceries")
    assert task1 == {"id": 1, "description": "Buy groceries", "completed": False}
    tasks = load_tasks()
    assert len(tasks) == 1
    assert tasks[0] == task1

    task2 = add_task("Do laundry")
    assert task2 == {"id": 2, "description": "Do laundry", "completed": False}
    tasks = load_tasks()
    assert len(tasks) == 2
    assert tasks[1] == task2

def test_list_tasks(temp_task_file):
    assert list_tasks() == []
    add_task("Walk the dog")
    add_task("Pay bills")
    tasks = list_tasks()
    assert len(tasks) == 2
    assert tasks[0]['description'] == "Walk the dog"
    assert tasks[1]['description'] == "Pay bills"

def test_complete_task(temp_task_file):
    task1 = add_task("Task to complete")
    add_task("Another task")
    
    assert complete_task(task1['id']) is True
    tasks = load_tasks()
    assert tasks[0]['completed'] is True
    assert tasks[1]['completed'] is False # ensure other tasks are untouched

    # Test completing non-existent task
    assert complete_task(999) is False
    tasks_after_non_existent = load_tasks()
    assert tasks_after_non_existent == tasks # No change

def test_delete_task(temp_task_file):
    task1 = add_task("Task to delete")
    task2 = add_task("Keep this task")

    assert delete_task(task1['id']) is True
    tasks = load_tasks()
    assert len(tasks) == 1
    assert tasks[0]['id'] == task2['id']

    # Test deleting non-existent task
    assert delete_task(999) is False
    tasks_after_non_existent = load_tasks()
    assert len(tasks_after_non_existent) == 1 # No change
