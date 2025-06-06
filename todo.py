tasks = []

def menu():
    print("\n--- T-Do List ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")


def view_task():
    if not tasks:
        print("No tasks yet.")
    for i, t in enumerate(tasks, 1):
        status = "✔" if t["done"] else "❌"
        print(f"{i}. {t['task']} [{status}]")

def mark_done():
    
    i = int(input("Enter task number to mark done: ")) - 1
    if 0 <= i <= len(tasks):
        tasks[i]["done"] = True
        print("Marked as done!")
    else:
        print("Invalid number.")


def del_task():
    task = int(input("Enter a task number to be deleted: ")) -1
    tasks.pop(task)
    print(tasks)

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        del_task()
    elif choice == "5":
        break
    else:
        print("Invalid Input")

