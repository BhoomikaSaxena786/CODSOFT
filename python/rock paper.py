import random

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
user_choice = input("Enter rock/paper/scissors = ")

if user_choice != "paper" and user_choice != "rock" and user_choice != "scissors":
    print("Invalid Choice")
elif user_choice == "paper" and computer_choice == "rock":
    print("You won")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You won")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You won")
elif user_choice == computer_choice:
    print("You both tied")
else:
    print(f"You lost, computer choice was {computer_choice}")




