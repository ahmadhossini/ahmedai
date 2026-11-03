# Task Manager CLI

A simple command-line interface (CLI) task manager written in Python, allowing users to create, list, complete, and delete tasks. Task data is persisted in a JSON file.

## Features

*   **Add Tasks**: Quickly add new tasks with a description.
*   **List Tasks**: View all tasks, pending tasks, or completed tasks.
*   **Complete Tasks**: Mark tasks as completed.
*   **Delete Tasks**: Remove tasks from the list.
*   **Persistence**: All tasks are saved to `tasks.json` and loaded automatically.

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/task-manager-cli.git
    cd task-manager-cli
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Make sure your virtual environment is activated, then run the `cli.py` script from your terminal.

### Add a Task

```bash
python cli.py add "Buy groceries"
python cli.py add "Finish report by Friday"
```

### List Tasks

*   **List all pending tasks (default)**:
    ```bash
    python cli.py list
    python cli.py list --pending
    python cli.py list -p
    ```

*   **List all tasks (including completed)**:
    ```bash
    python cli.py list --all
    python cli.py list -a
    ```

*   **List only completed tasks**:
    ```bash
    python cli.py list --completed
    python cli.py list -c
    ```

### Complete a Task

Mark a task as completed using its ID.

```bash
python cli.py complete 1
```

### Delete a Task

Remove a task using its ID.

```bash
python cli.py delete 2
```

## Running Tests

To run the unit tests, make sure `pytest` is installed (it's specified in `requirements.txt`).

```bash
pytest
```
