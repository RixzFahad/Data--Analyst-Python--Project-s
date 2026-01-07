"""
#1.WorkFlow For Project:-
Input From user(Rock, Paper, Scissors):-

#2.Computer Choice:-
(Randomly)-- Computer Choose Randomly no Condition's Apply here!

#3. Result Print:-
With Logic's Like When i And Computer Wins

--Cases--
~ 1- Rock
A - Rock - Rock = Tie
B - Rock - Paer = Paper Win's
C - Rock - Scissors = Rock Win's

~ 2- Paper
A - Paper - Paper = Tie
B - Paper - Rock = Paer Win's
C - Paper - Scissors = Scissors Win's

~ 3- Scissors
A - Scissors - Scissors = Tie
B - Scissors - Paper = Scissors Win's
C - Scissors - Rock = Rock Win's
"""

#Step One
import random
item_list = ["Rock", "Paper", "Scissors"]
user_choice = (input("Choose Your choice : Rock, Paper, Scissors:-"))

comp_choice =random.choice(item_list)

print(f"User Choice:{user_choice}, Computer Choice: {comp_choice}")


# Applying Conditon's

if user_choice == comp_choice:
    print("Both Moves Are Same : It's A Tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper Cover's Rock So : Computer Wins ")
    else:
        print("Rock Smash Scissor : User Wins")
elif user_choice == "paper":
     if comp_choice == "Scissors":
         print("Scissors Cut's Paper : Computer Wins ")
     else:
         print("Paper Cover Rock : User Wins")
elif user_choice == "Scissors":
    if comp_choice == "Paper":
        print("Scissors Cut's Paper : User Wins ")
    else:
        print("Rock Smash Scissors : Computer Wins")

# In That Code I Stuck In Casing :- Somewhere I Gave Small Letter By Assign Variable's As CAPITAL
"""
There Are Many Issues Which I Want To Work:- 
#1. If You Gave Another Move- Variable For Game It Accepted By Not Give OutPut
#2. For OutPut It's Not Good To Write Which Move I Want To Play
#3. I Should Assign Them Number's Like One Two Three And Pick One - 
1 == Rock
2 == Paper
3 == Scissors
"""

