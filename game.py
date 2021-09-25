import random

print("Welcome 'Player One' to my rock, paper, scissors game")

print("Rock, Paper, Scissors, Shoot!")

# PROMPT USER FOR INPUT

user_choice = input("Choose 'rock' or 'paper' or 'scissors' : ")
print("User Chose:")
print(user_choice)

# Computer choice at random

options = ["rock", "paper", "scissors"]

if user_choice not in options:
    print("Sorry that is not a valid option")
    exit()

computer_choice = random.choice(options)
print("Computer Chose:")
print(computer_choice)

#Worked with Andrew from this point forward

if (computer_choice == user_choice):
    print("You chose the same option, please choose again")
elif (user_choice == "rock" ):
    if (computer_choice == "scissors"):
        print("rock beats scissors, congratulations 'Player One' wins")
    else:
        print("paper covers rock, sorry you lost. Computer Wins")
elif (user_choice == "scissors"):
    if (computer_choice == "rock"):
        print("rock beats scissors, sorry you lost. Computer Wins")
    else:
        print("scissors cust paper, congratulations 'Player One' wins")
elif (user_choice == "paper"):
    if (computer_choice == "rock"):
        print("paper covers rock, congratulations 'Player One' wins")
    else:
        print("scissors cuts paper, sorry you lost. Computer Wins")
