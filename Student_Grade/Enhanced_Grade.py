# ===============================
# Student Grades Management System
# ===============================

# Dictionary to store student names as keys
# and their grades as values
# Example: {"Rixz": 95, "Alex": 88}
students_grades = {}


def add_student(name, grade):
    """
    Adds a new student to the dictionary.
    If the student already exists, their grade will be overwritten.
    """
    students_grades[name] = grade
    print(f"✅ Added {name} with grade: {grade}")


def update_student(name, grade):
    """
    Updates the grade of an existing student.
    """
    if name in students_grades:        # Check if key exists in dictionary
        students_grades[name] = grade
        print(f"✏️ Updated {name} with new grade: {grade}")
    else:
        print(f"❌ Student '{name}' does not exist")


def delete_student(name):
    """
    Deletes a student from the dictionary.
    """
    if name in students_grades:
        del students_grades[name]      # Remove key-value pair
        print(f"🗑️ Deleted student '{name}' successfully")
    else:
        print(f"❌ Student '{name}' does not exist")


def display_students():
    """
    Displays all students and their grades.
    """
    if students_grades:                # Check if dictionary is not empty
        print("\n📋 Student List:")
        for name, grade in students_grades.items():
            print(f"• {name}: {grade}")
    else:
        print("⚠️ No students found")


def get_valid_integer(prompt):
    """
    Utility function to safely take integer input.
    Prevents program crash due to invalid input.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("⚠️ Please enter a valid number.")


def main():
    """
    Main function that controls the menu-driven program.
    """
    while True:
        print("\n------ Student Grades Management System ------")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display Students")
        print("5. Exit")

        choice = get_valid_integer("Enter your choice: ")

        if choice == 1:
            name = input("Enter student name: ").strip()
            grade = get_valid_integer("Enter marks: ")
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student name to update: ").strip()
            grade = get_valid_integer("Enter new marks: ")
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student name to delete: ").strip()
            delete_student(name)

        elif choice == 4:
            display_students()

        elif choice == 5:
            print("🙏 Thanks for using Student Grades Module")
            break

        else:
            print("❌ Invalid choice. Please select between 1–5.")


# Program execution starts here
main()
