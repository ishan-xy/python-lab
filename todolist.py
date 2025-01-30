# List to store tasks
tasks = []

def add_task():
    task = input("Enter the task to add: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added.")
    else:
        print("Task cannot be empty.")

def view_tasks():
    if tasks:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("\nYour To-Do list is empty.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter the number of the task to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid index. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the to-do list application
main()