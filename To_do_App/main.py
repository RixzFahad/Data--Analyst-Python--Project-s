def task():
    task = []
    print("---Welcome To The Task Management App---")

    total_tasks = int(input("Enter The Total Number Of Tasks: "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter The Task Name{i}:")
        task.append(task_name)
        print(f"Today's Task's Are \n{task}")

    while True:
        operation = int(input("Enter 1- Add\n 2- Update\n 3- Delete\n 4- View\n 5- Exit"))

        if operation == 1:
            add = input("Enter The New Task Name: ")
            task.append(add)
            print(f"task {task} added successfully")

        elif operation == 2:
            updated_val = input("Enter The Task To Update: ")
            if updated_val in task:
                up = input("Enter The New Task Name: ")
                ind = task.index(updated_val)
                task[ind] = up
                print("Task updated successfully")
        elif operation == 3:
            delete_val= input ("Enter The Task To Delete:")
            if delete_val in task:
                ind = task.index(delete_val)
                del task[ind]
                print(f"Task {delete_val} deleted successfully")
        elif operation == 4:
            print(f"Total Tasks: {task}")
        elif operation ==5 :
            print("Thank You For The Task Management App")
            break

task()  # 🔥 REQUIRED
