#!/usr/bin/env python3
import argparse
import sys
from task_manager import add_task, list_tasks, complete_task, delete_task

def main():
    parser = argparse.ArgumentParser(description="A simple CLI Task Manager.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Description of the task")

    # List command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("--all", "-a", action="store_true", help="Show all tasks (including completed)")
    list_parser.add_argument("--pending", "-p", action="store_true", help="Show only pending tasks (default)")
    list_parser.add_argument("--completed", "-c", action="store_true", help="Show only completed tasks")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("id", type=int, help="ID of the task to complete")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="ID of the task to delete")

    args = parser.parse_args()

    # Filter logic for list command
    if args.command == "list":
        tasks = list_tasks()
        if not tasks:
            print("No tasks found.")
            sys.exit(0)

        # Determine filter preference
        show_all = args.all
        show_pending = args.pending
        show_completed = args.completed

        # Default to pending if no specific filter is chosen
        if not show_all and not show_pending and not show_completed:
            show_pending = True

        filtered_tasks = []
        for task in tasks:
            if show_all:
                filtered_tasks.append(task)
            elif show_pending and not task['completed']:
                filtered_tasks.append(task)
            elif show_completed and task['completed']:
                filtered_tasks.append(task)

        if not filtered_tasks:
            filter_name = "pending" if show_pending else "completed" if show_completed else "all" if show_all else "matching"
            print(f"No {filter_name} tasks found.")
            sys.exit(0)

        print("Your tasks:")
        for task in filtered_tasks:
            status = "[x]" if task['completed'] else "[ ]"
            print(f"{status} {task['id']}: {task['description']}")

    # Other commands
    elif args.command == "add":
        task = add_task(args.description)
        print(f"Added task {task['id']}: '{task['description']}'")
    elif args.command == "complete":
        if complete_task(args.id):
            print(f"Task {args.id} marked as completed.")
        else:
            print(f"Error: Task {args.id} not found.")
            sys.exit(1)
    elif args.command == "delete":
        if delete_task(args.id):
            print(f"Task {args.id} deleted.")
        else:
            print(f"Error: Task {args.id} not found.")
            sys.exit(1)

if __name__ == "__main__":
    main()
