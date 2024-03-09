tasks = []

def taskcomplete():
    listalltasks()
    taskindex = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= taskindex < len(tasks):
        print(f"Task '{tasks[taskindex]}' marked as complete.")
        tasks.pop(taskindex)
    else:
        print("Invalid task number.")

def listalltasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks in the list:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

def addatask():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")



while True:
    print("\nTo-Do List Application")
    print("1. Add a Task")
    print("2. List all the Tasks")
    print("3. Mark the Task as Completed")
    print("4. Quit the Task")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        addatask()
    elif choice == "2":
        listalltasks()
    elif choice == "3":
        taskcomplete()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")