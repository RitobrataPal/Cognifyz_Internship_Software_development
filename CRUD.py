class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description
    
    def __str__(self):
        return f"Task ID: {self.task_id}, Title: {self.title}, Description: {self.description}"
tasks = []
task_id_counter = 1

def create_task(title, description):
    global task_id_counter
    new_task = Task(task_id_counter, title, description)
    tasks.append(new_task)
    task_id_counter += 1
    print("Task created successfully!")
def read_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            print(task)
def update_task(task_id, new_title, new_description):
    for task in tasks:
        if task.task_id == task_id:
            task.title = new_title
            task.description = new_description
            print("Task updated successfully!")
            return
    print("Task not found.")
def delete_task(task_id):
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            print("Task deleted successfully!")
            return
    print("Task not found.")
def main():
    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            create_task(title, description)
        elif choice == '2':
            read_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            new_title = input("Enter new title: ")
            new_description = input("Enter new description: ")
            update_task(task_id, new_title, new_description)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            print("Exiting the Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
main()
