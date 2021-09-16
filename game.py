import random

print("Rock, Paper, Scissors, Shoot!")

# PROMPT USER FOR INPUT

user_choice = input("Choose 'rock' or 'paper' or 'scissors' : ")
print("User Chose:")
print(user_choice)

# Computer choice at random

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer Chose:")
print(computer_choice)