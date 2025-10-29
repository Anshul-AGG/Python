import os

# File to store tasks
TASK_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []


# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Main loop

def todo_app():

    tasks = load_tasks()
    print(tasks)

    while True:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("\nOptions: [A]dd  [R]emove  [Q]uit")
        choice = input("Choose an option: ").strip().lower()

        if choice == "a":
            new_task = input("Enter a new task: ").strip()
            tasks.append(new_task)
            save_tasks(tasks)
            print("Task added.")
            
        elif choice == "r":
            try:
                num = int(input("Enter task number to remove: "))
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"Removed: {removed}")
            except (ValueError, IndexError):
                print("Invalid task number.")
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

todo_app()