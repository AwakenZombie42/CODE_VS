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