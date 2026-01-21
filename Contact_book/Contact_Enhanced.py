# ---------------------------------------
# CONTACT BOOK APPLICATION (END-TO-END)
# ---------------------------------------

# Import json module
# Used to store and retrieve contact data in JSON format
import json

# Import os module
# Used to check whether the data file already exists
import os


# ---------------------------------------
# CONSTANT: File name where data is saved
# ---------------------------------------
FILE_NAME = "contacts.json"


# ---------------------------------------
# FUNCTION: Load contacts from file
# ---------------------------------------
def load_contacts():
    """
    Loads contacts from a JSON file if it exists.
    Returns an empty dictionary if file is not found or corrupted.
    """
    if os.path.exists(FILE_NAME):          # Check if file exists
        try:
            with open(FILE_NAME, "r") as file:   # Open file in read mode
                return json.load(file)           # Convert JSON to dictionary
        except json.JSONDecodeError:       # Handle corrupted JSON file
            return {}
    return {}


# ---------------------------------------
# FUNCTION: Save contacts to file
# ---------------------------------------
def save_contacts(contacts):
    """
    Saves all contacts to a JSON file.
    """
    with open(FILE_NAME, "w") as file:      # Open file in write mode
        json.dump(contacts, file, indent=4)  # Convert dictionary to JSON


# ---------------------------------------
# FUNCTION: Create a new contact
# ---------------------------------------
def create_contact(contacts):
    """
    Creates a new contact and stores it in dictionary.
    """
    name = input("Enter Contact Name: ")

    if name in contacts:                   # Check if contact already exists
        print(f"❌ Contact '{name}' already exists")
        return

    age = int(input("Enter Age: "))
    email = input("Enter Email: ")
    number = input("Enter Phone Number: ")

    # Store contact data as a nested dictionary
    contacts[name] = {
        "age": age,
        "email": email,
        "number": number
    }

    print(f"✔ Contact '{name}' created successfully")


# ---------------------------------------
# FUNCTION: View a contact
# ---------------------------------------
def view_contact(contacts):
    """
    Displays details of a specific contact.
    """
    name = input("Enter Contact Name to View: ")

    if name in contacts:
        contact = contacts[name]
        print("\n--- Contact Details ---")
        print(f"Name   : {name}")
        print(f"Age    : {contact['age']}")
        print(f"Email  : {contact['email']}")
        print(f"Number : {contact['number']}")
    else:
        print("❌ Contact not found")


# ---------------------------------------
# FUNCTION: Update an existing contact
# ---------------------------------------
def update_contact(contacts):
    """
    Updates details of an existing contact.
    """
    name = input("Enter Contact Name to Update: ")

    if name not in contacts:
        print("❌ Contact not found")
        return

    contacts[name]["age"] = int(input("Enter New Age: "))
    contacts[name]["email"] = input("Enter New Email: ")
    contacts[name]["number"] = input("Enter New Phone Number: ")

    print(f"✔ Contact '{name}' updated successfully")


# ---------------------------------------
# FUNCTION: Delete a contact
# ---------------------------------------
def delete_contact(contacts):
    """
    Deletes a contact from the dictionary.
    """
    name = input("Enter Contact Name to Delete: ")

    if name in contacts:
        del contacts[name]                 # Remove contact from dictionary
        print(f"✔ Contact '{name}' deleted successfully")
    else:
        print("❌ Contact not found")


# ---------------------------------------
# FUNCTION: Search for contacts
# ---------------------------------------
def search_contact(contacts):
    """
    Searches contacts by partial name match.
    """
    search_name = input("Enter name to search: ").lower()
    found = False

    for name, contact in contacts.items(): # Loop through all contacts
        if search_name in name.lower():
            print("\n✔ Contact Found")
            print(f"Name   : {name}")
            print(f"Age    : {contact['age']}")
            print(f"Email  : {contact['email']}")
            print(f"Number : {contact['number']}")
            found = True

    if not found:
        print("❌ No matching contact found")


# ---------------------------------------
# FUNCTION: Count total contacts
# ---------------------------------------
def count_contacts(contacts):
    """
    Displays total number of contacts.
    """
    print(f"📊 Total Contacts: {len(contacts)}")


# ---------------------------------------
# MAIN PROGRAM STARTS HERE
# ---------------------------------------

# Load existing contacts from file
contacts = load_contacts()

# Infinite loop to keep application running
while True:

    # Display menu
    print("\n--- Contact Book App ---")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contacts")
    print("7. Exit")

    # Take user input safely
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("⚠ Please enter a valid number (1-7)")
        continue

    # Menu selection
    if choice == 1:
        create_contact(contacts)

    elif choice == 2:
        view_contact(contacts)

    elif choice == 3:
        update_contact(contacts)

    elif choice == 4:
        delete_contact(contacts)

    elif choice == 5:
        search_contact(contacts)

    elif choice == 6:
        count_contacts(contacts)

    elif choice == 7:
        save_contacts(contacts)             # Save data before exit
        print("\n✔ Contacts saved successfully")
        print("--- Thank You for Using Contact Book ---")
        break

    else:
        print("⚠ Please enter a valid option (1-7)")
