import random

# Mapping numbers to moves
choices = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

# User input
print("Choose your move:")
print("1 - Rock")
print("2 - Paper")
print("3 - Scissors")

try:
    user_input = int(input("Enter your choice (1/2/3): "))

    if user_input not in choices:
        print("Invalid choice! Please select 1, 2, or 3.")
    else:
        user_choice = choices[user_input]
        comp_choice = random.choice(list(choices.values()))

        print(f"\nUser Choice: {user_choice}")
        print(f"Computer Choice: {comp_choice}")

        # Game logic
        if user_choice == comp_choice:
            print("Result: It's a Tie")

        elif user_choice == "Rock":
            if comp_choice == "Paper":
                print("Result: Computer Wins (Paper covers Rock)")
            else:
                print("Result: User Wins (Rock smashes Scissors)")

        elif user_choice == "Paper":
            if comp_choice == "Scissors":
                print("Result: Computer Wins (Scissors cut Paper)")
            else:
                print("Result: User Wins (Paper covers Rock)")

        elif user_choice == "Scissors":
            if comp_choice == "Rock":
                print("Result: Computer Wins (Rock smashes Scissors)")
            else:
                print("Result: User Wins (Scissors cut Paper)")

except ValueError:
    print("Invalid input! Please enter a number.")
