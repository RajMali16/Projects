def handle_todo_file(file_name, mode):
    """
    Handles all to-do list file operations in a single function.
    mode="r" -> View tasks
    mode="a" -> Add a task
    mode="w" -> Clear all tasks
    """

    # 1. VIEW MODE (Read)
    if mode == "r":
        print("\n--- Current To-Do List ---")
        try:
            with open(file_name, "r") as file:
                tasks = file.readlines()

            if len(tasks) == 0:
                print("No tasks found! Your list is empty.")
            else:
                counter = 1
                for task in tasks:
                    print(str(counter) + ". " + task.strip())
                    counter = counter + 1
        except FileNotFoundError:
            print("No tasks found! Your list is empty.")

    # 2. ADD MODE (Append)
    elif mode == "a":
        task = input("\nEnter the task you want to add: ")
        if task.strip() == "":
            print("Task cannot be empty!")
        else:
            with open(file_name, "a") as file:
                file.write(task + "\n")
            print("Success: Task added to your list.")

    # 3. CLEAR MODE (Write)
    elif mode == "w":
        confirm = input("\nAre you sure you want to delete ALL tasks? (y/n): ")
        if confirm.lower() == "y":
            with open(file_name, "w") as file:
                file.write("")
            print("All tasks have been cleared.")
        else:
            print("Action canceled.")

    # If someone types a mode that isn't r, w, or a
    else:
        print("Invalid mode! Use 'r' to read, 'a' to append, or 'w' to write.")


# --- Main Application Loop ---
MY_FILE = "todo.txt"

while True:
    print("\n====================")
    print("   TO-DO TERMINAL   ")
    print("====================")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Clear All Tasks")
    print("4. Exit")

    choice = input("\nChoose an option (1-4): ")

    if choice == "1":
        handle_todo_file(MY_FILE, "r")  # Passes file name and 'r' for read
    elif choice == "2":
        handle_todo_file(MY_FILE, "a")  # Passes file name and 'a' for append
    elif choice == "3":
        handle_todo_file(MY_FILE, "w")  # Passes file name and 'w' for write
    elif choice == "4":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")