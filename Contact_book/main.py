#Empty Dictionary
contacts = {}
while True:
    print("\n Contact Book App")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contacts")
    print("7. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        name = input("Enter your name:")
        if name in contacts:
            print(f"Contact {name} Already Exists")
        else:
            age = int(input ("Enter Contact Person's Age:"))
            email = input("Enter Contact Person's Email:")
            number = input("Enter Contact Person's Number:")
            contacts[name] = {'age':int(age),'email':email, 'number':number}
            print(f"--Contact {name} Created Sucessfully--")



    elif choice == 2:

        name = input("Enter User Name To View: ")

        if name in contacts:

            contact = contacts[name]

            print(f"Name   : {name}")

            print(f"Age    : {contact['age']}")

            print(f"Email  : {contact['email']}")

            print(f"Number : {contact['number']}")

        else:

            print("Contact not found")
    elif choice == 3:
        name = input("Enter User Name To Update:")
        if name in contacts:
            age = int(input("Enter Contact Person's Age:"))
            email = input("Enter Contact Person's Email:")
            number = input("Enter Contact Person's Number:")
            contacts[name] = {'age':int(age),'email':email, 'number':number}
        else:
            print("Contact Not Found")

    elif choice == 4:
        name = input("Enter User Name To Delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} Deleted Sucessfully")
        else:
            print("contact not found")

    elif choice == 5:
        contact = input("Enter User Name To Search:")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found Contact: {name}, Age: {age}, Email: {email}, Number: {number}')
                found = True
                if not found:
                    print("Contact not found")
    elif choice == 6:
        print(f'Total Contacts: {len(contacts)}')

    elif choice == 7:
        print("---ThankYou For Using Contact Book---")
        break
    else:
        print("Enter a valid choice")





