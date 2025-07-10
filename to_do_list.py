# to-do-list.py

TODO_FILE = "todo.txt"

def load_tasks():
    try:
        with open(TODO_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def main():
    tasks = load_tasks()
    
    while True:
        print("Options: add | remove | list | quit")
        command = input("Enter command: ").strip().lower()

        if command == "add":
            task = input("Enter a task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("Task added.\n")

        elif command == "remove":
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"Removed: {removed}\n")
                else:
                    print("Invalid task number.\n")
            except ValueError:
                print("Please enter a valid number.\n")

        elif command == "list":
            show_tasks(tasks)

        elif command == "quit":
            print("Goodbye!")
            break

        else:
            print("Unknown command. Try again.\n")

if __name__ == "__main__":
    main()
