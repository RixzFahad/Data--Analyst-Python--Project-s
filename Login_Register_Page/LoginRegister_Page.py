import re
import os

FILE_NAME = "users.txt"

# ----------------- EMAIL VALIDATION -----------------
def validate_email(email):
    """Validate email format in a friendly way"""
    if "@" not in email or "." not in email:
        return False
    if not email[0].isalpha():
        return False
    at_index = email.index("@")
    dot_index = email.rindex(".")
    if at_index > dot_index:
        return False
    if email[at_index + 1] == ".":
        return False
    return True

# ----------------- PASSWORD VALIDATION -----------------
def validate_password(password):
    """Password must be 6-16 chars, with upper, lower, digit, and special char"""
    if len(password) < 8 or len(password) > 16:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[@#$%!&*]", password):
        return False
    return True

# ----------------- CHECK IF USER EXISTS -----------------
def user_exists(email):
    """Check if email already exists in file"""
    if not os.path.exists(FILE_NAME):
        return False
    with open(FILE_NAME, "r") as file:
        for line in file:
            try:
                stored_email, _ = line.strip().split(":")
                if stored_email == email:
                    return True
            except ValueError:
                continue
    return False

# ----------------- REGISTER USER -----------------
def register():
    print("\n--- Welcome to Registration ---")
    email = input("Enter your Email ID: ").strip()
    if not validate_email(email):
        print("❌ Invalid email format. Example: example@mail.com")
        return
    if user_exists(email):
        print("⚠️ This email is already registered. Try logging in.")
        return

    password = input("Enter a strong Password: ").strip()
    if not validate_password(password):
        print("❌ Password must be 6-16 chars, with at least 1 uppercase, 1 lowercase, 1 number & 1 special char (@#$%!&*)")
        return

    with open(FILE_NAME, "a") as file:
        file.write(f"{email}:{password}\n")
    print("✅ Registration successful! You can now log in.")

# ----------------- LOGIN USER -----------------
def login():
    print("\n--- Welcome to Login ---")
    email = input("Enter your Email ID: ").strip()
    password = input("Enter your Password: ").strip()

    if not os.path.exists(FILE_NAME):
        print("⚠️ No registered users found. Please register first.")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            try:
                stored_email, stored_pass = line.strip().split(":")
                if stored_email == email and stored_pass == password:
                    print(f"✅ Login successful! Welcome back, {email}")
                    return
            except ValueError:
                continue
    print("❌ Login failed! Check your email or password.")

# ----------------- RESET PASSWORD -----------------
def reset_password():
    print("\n--- Password Reset ---")
    email = input("Enter your registered Email ID: ").strip()
    if not user_exists(email):
        print("⚠️ Email not found. Please register first.")
        return

    lines = []
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    new_password = input("Enter your new Password: ").strip()
    if not validate_password(new_password):
        print("❌ Password must be 6-16 chars, with at least 1 uppercase, 1 lowercase, 1 number & 1 special char (@#$%!&*)")
        return

    with open(FILE_NAME, "w") as file:
        for line in lines:
            try:
                stored_email, _ = line.strip().split(":")
                if stored_email == email:
                    file.write(f"{email}:{new_password}\n")
                else:
                    file.write(line)
            except ValueError:
                file.write(line)
    print("✅ Password updated successfully!")

# ----------------- MAIN MENU -----------------
def main():
    while True:
        print("\n===== User Authentication System =====")
        print("1. Register")
        print("2. Login")
        print("3. Reset Password")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            reset_password()
        elif choice == "4":
            print("👋 Goodbye! Stay safe.")
            break
        else:
            print("❌ Invalid choice! Please select 1, 2, 3, or 4.")

# Run the program
if __name__ == "__main__":
    main()
