import os  # os module is used for file and directory operations


# -------------------- FILE CREATION --------------------
def create_file(file_name):
    """
    Creates a new file with the given name.
    Uses 'x' mode to avoid overwriting existing files.
    """
    try:
        # 'x' mode creates file only if it does not exist
        with open(file_name, 'x'):
            print(f"{file_name} created successfully")
    except FileExistsError:
        # Triggered if file already exists
        print(f"{file_name} already exists")
    except Exception:
        # Handles any unexpected error
        print("An error occurred while creating the file")


# -------------------- VIEW FILES --------------------
def view_all_files():
    """
    Displays all files present in the current directory.
    """
    # Fetch list of all files and folders
    files = os.listdir()

    # Check if directory is empty
    if not files:
        print("No files found")
    else:
        print("Files in directory:")
        for file in files:
            print(file)


# -------------------- DELETE FILE --------------------
def delete_file(file_name):
    """
    Deletes a file if it exists.
    """
    try:
        os.remove(file_name)  # Remove the specified file
        print(f"{file_name} deleted successfully")
    except FileNotFoundError:
        # If file does not exist
        print("File not found")
    except Exception:
        print("An error occurred while deleting the file")


# -------------------- READ FILE --------------------
def read_file(file_name):
    """
    Reads and displays the content of a file.
    """
    try:
        # Open file in read mode
        with open(file_name, 'r') as f:
            content = f.read()
            print(f"\nContent of {file_name}:\n{content}")
    except FileNotFoundError:
        print("File does not exist")
    except Exception:
        print("An error occurred while reading the file")


# -------------------- EDIT FILE --------------------
def edit_file(file_name):
    """
    Appends new content to an existing file.
    """
    try:
        # Open file in append mode
        with open(file_name, 'a') as f:
            content = input("Enter content to add: ")
            f.write(content + "\n")  # Add content with newline
            print(f"Content added to {file_name}")
    except FileNotFoundError:
        print("File does not exist")
    except Exception:
        print("An error occurred while editing the file")


# -------------------- MAIN MENU --------------------
def main():
    """
    Main function that displays menu and handles user choices.
    """
    while True:
        print("\n--- File Management System ---")
        print("1. Create A File")
        print("2. View All Files")
        print("3. Delete File")
        print("4. Read File")
        print("5. Edit File")
        print("6. Exit")

        try:
            # Convert input to integer
            choice = int(input("Enter your choice: "))
        except ValueError:
            # Handles non-integer input
            print("Please enter a valid number")
            continue

        # Match user choice with operation
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
            break  # Exit the loop

        else:
            print("Choose a correct option (1-6)")


# -------------------- PROGRAM ENTRY POINT --------------------
if __name__ == "__main__":
    # Ensures program runs only when executed directly
    main()
