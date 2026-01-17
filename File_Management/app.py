import os

def create_file(file_name):
    try:
        with open(file_name, 'x'):
            print(f"{file_name} created successfully")
    except FileExistsError:
        print(f"{file_name} already exists")
    except Exception:
        print("An error occurred")


def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found")
    else:
        print("Files in directory:")
        for file in files:
            print(file)


def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"{file_name} deleted successfully")
    except FileNotFoundError:
        print("File not found")
    except Exception:
        print("An error occurred")


def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            content = f.read()
            print(f"\nContent of {file_name}:\n{content}")
    except FileNotFoundError:
        print("File does not exist")
    except Exception:
        print("An error occurred")


def edit_file(file_name):
    try:
        with open(file_name, 'a') as f:
            content = input("Enter content to add: ")
            f.write(content + "\n")
            print(f"Content added to {file_name}")
    except FileNotFoundError:
        print("File does not exist")
    except Exception:
        print("An error occurred")


def main():
    while True:
        print("\n--- File Management System ---")
        print("1. Create File")
        print("2. View All Files")
        print("3. Delete File")
        print("4. Read File")
        print("5. Edit File")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number")
            continue

        if choice == 1:
            filename = input("Enter file name: ")
            create_file(filename)

        elif choice == 2:
            view_all_files()

        elif choice == 3:
            filename = input("Enter file name to delete: ")
            delete_file(filename)

        elif choice == 4:
            filename = input("Enter file name to read: ")
            read_file(filename)

        elif choice == 5:
            filename = input("Enter file name to edit: ")
            edit_file(filename)

        elif choice == 6:
            print("Thank you! Come back later 👋")
            break

        else:
            print("Choose a correct option")


if __name__ == "__main__":
    main()
