import click  # To create a CLI
import json   # To save & load tasks from a file
import os     # To check if the file exists

TODO_FILE = "todo.json"

def load_task():
    """Load tasks from the JSON file"""
    if not os.path.exists(TODO_FILE):  # Check if the file exists
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to the JSON file"""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

@click.group()
def cli():
    """Simple Todo List Manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_task()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Task added successfully: {task}")

@click.command()
def list():
    """List All The List"""
    tasks = load_task()
    if not tasks:
        click.echo("No tasks found.")
        return
    for index,task in enumerate(tasks,1):
        status = "Y" if task["done"] else "F"
        click.echo(f"{index}. {task['task']} [{status}]")


@click.command()
@click.argument("task_number",type=int)
def complete(task_number):
    """Make a tasks as completed"""
    tasks = load_task()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1] ["done"] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} marked as completed.")
    else:
        click.echo(f"invalid task number:{task_number}")

@click.command()
@click.argument("task_number",type=int)
def delete(task_number):
    """Del a Task"""
    tasks = load_task()

    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Removed Task:{removed_task["task"]}")
    else:
        click.echo(f"Invalid Task number")


 

# Registering the add command
cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)
if __name__ == "__main__":
    cli()

