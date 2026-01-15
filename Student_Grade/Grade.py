students_grades = {}

def add_student(name, grade):
    students_grades[name] = grade
    print(f"Added {name} with grade: {grade}")

def update_student(name, grade):
    if name in students_grades:
        students_grades[name] = grade
        print(f"Updated {name} with marks: {grade}")
    else:
        print(f"Student {name} does not exist")

def delete_student(name):
    if name in students_grades:
        del students_grades[name]
        print(f"Deleted student {name} successfully")
    else:
        print(f"Student {name} does not exist")

def display_students():
    if students_grades:
        for name, grade in students_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No students found")

def main():
    while True:
        print("\n------ Student Grades Management System ------")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display Students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            name = input("Enter student name: ")
            grade = int(input("Enter marks: "))
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student name to update: ")
            grade = int(input("Enter new marks: "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student name to delete: ")
            delete_student(name)

        elif choice == 4:
            display_students()

        elif choice == 5:
            print("----- Thanks for using Student Grades Module -----")
            break

        else:
            print("Invalid choice")

main()
