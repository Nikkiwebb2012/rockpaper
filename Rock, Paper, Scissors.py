# Import the random module
import random

# Define a list of possible actions
actions = ["Rock", "Paper", "Scissors"]

# Define a function to compare the player's and the computer's choices
def compare(player, computer):
    # If the choices are the same, it is a tie
    if player == computer:
        return "Game Tied"
    # If the player chooses Rock, check the computer's choice
    elif player == "Rock":
        # If the computer chooses Paper, the player loses
        if computer == "Paper":
            return "You lose"
        # If the computer chooses Scissors, the player wins
        else:
            return "You win"
    # If the player chooses Paper, check the computer's choice
    elif player == "Paper":
        # If the computer chooses Scissors, the player loses
        if computer == "Scissors":
            return "You lose"
        # If the computer chooses Rock, the player wins
        else:
            return "You win"
    # If the player chooses Scissors, check the computer's choice
    else:
        # If the computer chooses Rock, the player loses
        if computer == "Rock":
            return "You lose"
        # If the computer chooses Paper, the player wins
        else:
            return "You win"

# Start the game loop
while True:
    # Ask the player for their choice
    player = input("Enter your choice (Rock, Paper or Scissors): ")
    # If the player wants to quit, end the game and thank them for playing
    if player == "I quit":
        print("Thank you for playing")
        break
    # Otherwise, check if the player's choice is valid
    elif player not in actions:
        print("Invalid choice. Please try again.")
        continue
    # Generate a random choice for the computer
    computer = random.choice(actions)
    # Print the choices of both players
    print(f"You chose {player}, and the computer chose {computer}.")
    # Compare the choices and print the result
    result = compare(player, computer)
    print(result)