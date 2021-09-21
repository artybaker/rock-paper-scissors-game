import random

print("Rock, Paper, Scissors, Shoot!")

# PROMPT USER FOR INPUT

user_choice = input("Choose 'rock' or 'paper' or 'scissors' : ")
print("User Chose:")
print(user_choice)

# Computer choice at random

options = ["rock", "paper", "scissors"]

if user_choice not in options:
    print("Not valid option")
    exit()

computer_choice = random.choice(options)
print("Computer Chose:")
print(computer_choice)

#Worked with Andrew from this point forward

if (computer_choice == user_choice):
    print("You chose the same option, please choose again")
elif (user_choice == "rock" ):
    if (computer_choice == "scissors"):
        print("rock beats scissors, congratulations you won")
    else:
        print("paper covers rock, sorry you lost")
elif (user_choice == "scissors"):
    if (computer_choice == "rock"):
        print("rock beats scissors, sorry you lost")
    else:
        print("scissors cust paper, congratulations you won")
elif (user_choice == "paper"):
    if (computer_choice == "rock"):
        print("paper covers rock, congratulations you won")
    else:
        print("scissors cuts paper, sorry you lost")
