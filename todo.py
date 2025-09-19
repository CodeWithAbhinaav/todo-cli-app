# todo.py - To-Do CLI App

def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("✅ No tasks yet!")
        return
    print("\n📌 Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task(tasks, task, filename="tasks.txt"):
    task = task.strip()
    if not task:
        print("⚠️ Empty task not added.")
        return
    tasks.append(task)
    save_tasks(tasks, filename)
    print("✅ Task added!")

def delete_task(tasks, index, filename="tasks.txt"):
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks, filename)
        print(f"❌ Deleted: {removed}")
        return removed
    else:
        print("⚠️ Invalid task number.")
        return None

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("\n===== To-Do App =====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            task = input("Enter new task: ")
            add_task(tasks, task, filename)

        elif choice == "3":
            view_tasks(tasks)
            num_str = input("Enter task number to delete: ").strip()
            try:
                num = int(num_str)
                delete_task(tasks, num, filename)
            except ValueError:
                print("⚠️ Enter a valid number.")

        elif choice == "4":
            print("👋 Goodbye!")
            break

        else:
            print("⚠️ Invalid option, try again.")

if __name__ == "__main__":
    main()
