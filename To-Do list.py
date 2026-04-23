tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except:
        pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

load_tasks()

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)

    elif choice == "4":
        show_tasks()
        num = int(input("Enter task number to mark done: "))
        if 0 < num <= len(tasks):
            tasks[num-1] = tasks[num-1] + " ✔"

    elif choice == "5":
        save_tasks()
        print("Tasks saved. Goodbye!")
        break