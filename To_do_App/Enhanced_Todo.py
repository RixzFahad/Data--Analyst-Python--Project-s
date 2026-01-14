def task():
    # task → list to store all task names
    task = []

    # Welcome message
    print("--- Welcome To The Task Management App ---")

    # Take input for number of initial tasks
    # int() converts input string into integer
    total_tasks = int(input("Enter The Total Number Of Tasks: "))

    # Loop to take initial task names
    # range(1, total_tasks + 1) → starts from 1 to total_tasks
    for i in range(1, total_tasks + 1):
        # input() → takes task name from user
        task_name = input(f"Enter The Task Name {i}: ")

        # append() → adds task at the end of the list
        task.append(task_name)

    # Display all tasks entered initially
    print(f"\nToday's Tasks Are:\n{task}")

    # Infinite loop to keep the app running until user exits
    while True:
        # Menu options for user
        operation = int(input(
            "\nEnter Operation:\n"
            "1 - Add Task\n"
            "2 - Update Task\n"
            "3 - Delete Task\n"
            "4 - View Tasks\n"
            "5 - Exit\n"
        ))

        # -------- ADD TASK --------
        if operation == 1:
            add = input("Enter The New Task Name: ")
            task.append(add)  # Add new task to list
            print(f"Task '{add}' added successfully")

        # -------- UPDATE TASK --------
        elif operation == 2:
            updated_val = input("Enter The Task To Update: ")

            # Check if task exists in list
            if updated_val in task:
                up = input("Enter The New Task Name: ")

                # index() → returns position of the task
                ind = task.index(updated_val)

                # Replace old task with new task
                task[ind] = up
                print("Task updated successfully")
            else:
                print("Task not found!")

        # -------- DELETE TASK --------
        elif operation == 3:
            delete_val = input("Enter The Task To Delete: ")

            if delete_val in task:
                ind = task.index(delete_val)

                # del → removes element at given index
                del task[ind]
                print(f"Task '{delete_val}' deleted successfully")
            else:
                print("Task not found!")

        # -------- VIEW TASKS --------
        elif operation == 4:
            print("\nYour Tasks:")
            # enumerate() → gives index + value
            for i, t in enumerate(task, start=1):
                print(f"{i}. {t}")

        # -------- EXIT APP --------
        elif operation == 5:
            print("Thank You For Using The Task Management App 🙌")
            break  # Exit the while loop

        # -------- INVALID INPUT --------
        else:
            print("Invalid choice! Please enter 1–5.")

# Function call → starts the program
task()
