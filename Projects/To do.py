def task_manager():
    tasks = []
    print("------ Welcome to the Task Management App ------")

    total_tasks = int(input("Enter how many tasks you want to add: "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter Task {i}: ")
        tasks.append(task_name)

    print(f"Today's tasks are: {tasks}")

    while True:
        try:
            operation = int(
                input(
                    "\nEnter an option:\n"
                    "1-Add\n"
                    "2-Update\n"
                    "3-Delete\n"
                    "4-View\n"
                    "5-Exit/Stop\n"
                    "Your choice: "
                )
            )

            if operation == 1:  # Add a task
                new_task = input("Enter the task you want to add: ")
                tasks.append(new_task)
                print(f"Task '{new_task}' has been added successfully!")

            elif operation == 2:  # Update a task
                task_to_update = input("Enter the task name you want to update: ")
                if task_to_update in tasks:
                    new_task = input("Enter the new task: ")
                    index = tasks.index(task_to_update)
                    tasks[index] = new_task
                    print(f"Task '{task_to_update}' has been updated to '{new_task}'.")
                else:
                    print(f"Task '{task_to_update}' not found.")

            elif operation == 3:  # Delete a task
                task_to_delete = input("Enter the task you want to delete: ")
                if task_to_delete in tasks:
                    tasks.remove(task_to_delete)
                    print(f"Task '{task_to_delete}' has been deleted successfully!")
                else:
                    print(f"Task '{task_to_delete}' not found.")

            elif operation == 4:  # View tasks
                if tasks:
                    print(f"Total tasks: {tasks}")
                else:
                    print("No tasks to show!")

            elif operation == 5:  # Exit the program
                print("Exiting the program... Goodbye!")
                break

            else:
                print("Invalid option. Please choose a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Run the task manager
task_manager()
