#I am building my first game on python
import random

print("Welcome to rock paper scissors.")
print("Type 'quit' anytime to stop playing.\n")

#possible moves
choices = ["rock", "paper", "scissors"]

#score-tracking
player_score = 0
computer_score = 0

while True:
    player_choice = input("Choose rock, paper or scissors: ").lower()
    
    if player_choice == "quit":
        print("Thanks for playing!")
        break

    if player_choice not in choices:
        print("This is not a valid choice")
        continue

    #the computer randomly picks out of the 3 choices
    computer_choice = random.choices(choices)
    print(f"The computer chose:{computer_choice}")

    #determine winner
    if player_choice == computer_choice:
        print("Tie!")
    elif (
        (player_choice == "rock" and computer_choice == "paper") or
        (player_choice == "scissors" and computer_choice == "rock") or
        (player_choice == "paper" and computer_choice == "scissors")
        ):
        print("The computer has won this round!")
        computer_score+=1
    else:
        print("You won this round!")
        player_score+=1
    
    #printing the scores
    print(f"score: player {player_score} - score: computer {computer_score}.")
print(f"Final score: player { player_score} - final score: computer {computer_score}.")
print("Good game!")
    