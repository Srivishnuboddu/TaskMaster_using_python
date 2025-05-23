def main():
    print("Welcome to the To-Do List Application")
    while True:
        print("\nMenu:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == '3':
            task_idx = int(input("Enter the number of the task to remove: ")) - 1
            remove_task(task_idx)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def view_tasks():
    tasks = get_tasks()
    if not tasks:
        print("No tasks in the list.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(task):
    tasks = get_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def remove_task(task_idx):
    tasks = get_tasks()
    if 0 <= task_idx < len(tasks):
        removed_task = tasks.pop(task_idx)
        save_tasks(tasks)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task number.")

def get_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

if __name__ == "__main__":
    main()
