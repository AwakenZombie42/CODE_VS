from random import choice

def game():
    computer = choice(["rock", "paper", "scissors"])
    player = input("Rock, Paper, or Scissors? ").lower()
    print(f"Computer chose: {computer}")
    if computer == player:
        print("Tie!")
    elif computer == "rock" and player == "paper":
        print("You win!")
    elif computer == "paper" and player == "scissors":
        print("You win!")
    elif computer == "scissors" and player == "rock":
        print("You win!")
    else:
        print("You lose!")

game()

'''
from random import choice

def game():
    # Randomly select rock, paper, or scissors for the computer
    computer = choice(["rock", "paper", "scissors"])
    # Get the player's input
    player = input("Rock, Paper, or Scissors? ").lower()
    print(f"Computer chose: {computer}")
    # Determine the outcome
    if computer == player:
        print("Tie!")
    elif (computer == "rock" and player == "paper") or \
         (computer == "paper" and player == "scissors") or \
         (computer == "scissors" and player == "rock"):
        print("You win!")
    else:
        print("You lose!")

game()
'''