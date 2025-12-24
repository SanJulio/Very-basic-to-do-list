tasks = []

while True:
    action = input("What would you like to do? Type 'add' to add a task, 'view' to view tasks, or 'quit' to exit: ")
    
    if action == 'add':
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"Added task: {task}")

    elif action == 'view':
        print("Your tasks:")
        for t in tasks:
            print(f"- {t}")
    
    elif action == 'quit':
        print("Goodbye!")
        break

    else:
        print("Invalid action.")
