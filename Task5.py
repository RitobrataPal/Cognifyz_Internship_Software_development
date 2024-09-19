import os

# Task class to manage task details
class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description

# Function to load tasks from a text file
def load_tasks(filename):
    tasks = []
    try:
        # Check if the file exists before reading
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                for line in file:
                    task_id, description = line.strip().split(',', 1)
                    tasks.append(Task(int(task_id), description))
    except Exception as e:
        print(f"Error loading tasks: {e}")
    return tasks

# Function to save tasks to a text file
def save_tasks(tasks, filename):
    try:
        with open(filename, 'w') as file:
            for task in tasks:
                file.write(f"{task.task_id},{task.description}\n")
    except Exception as e:
        print(f"Error saving tasks: {e}")

# Function to display tasks
def display_tasks(tasks):
    if tasks:
        print("Current Tasks:")
        for task in tasks:
            print(f"ID: {task.task_id}, Description: {task.description}")
    else:
        print("No tasks available.")

# Function to add a task
def add_task(tasks, task_id, description):
    tasks.append(Task(task_id, description))

# Function to delete a task
def delete_task(tasks, task_id):
    tasks = [task for task in tasks if task.task_id != task_id]
    return tasks

# Main function to manage CRUD operations
def manage_tasks():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)

    while True:
        print("\nTask Manager:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Save & Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            task_id = int(input("Enter task ID: "))
            description = input("Enter task description: ")
            add_task(tasks, task_id, description)
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            tasks = delete_task(tasks, task_id)
        elif choice == '4':
            save_tasks(tasks, filename)
            print("Tasks saved successfully.")
            break
        else:
            print("Invalid option, please choose again.")

# Test the program
manage_tasks()
