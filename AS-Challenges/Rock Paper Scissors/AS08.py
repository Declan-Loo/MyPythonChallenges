"""
AS08	50	
ROCK PAPER SCISSORS	
Create a game of rock, paper, Scissors to play against the computer.	
"""

import random

#List of allowed moves
moves = ["rock", "paper", "scissors"]

print("Welcome to rock, paper, scissors!")

user_move = ''
while user_move != 'quit':
    #Prompt the user to make a move
    user_move = input("Enter your move (rock, paper, scissors, or quit): ").lower()
    #Make sure the user entered a valid move
    while user_move not in moves:
        print("Invalid move. Please try again.")
        user_move = input("Enter your move (rock, paper, scissors, or quit): ").lower()
    #Have the computer make a random move
    computer_move = random.choice(moves)
    print("Computer move: " + computer_move)
    #Determine the winner of the round
    if user_move == computer_move:
        print("It's a tie!")
    elif user_move == "rock" and computer_move == "scissors":
        print("You win! Rock beats scissors.")
    elif user_move == "paper" and computer_move == "rock":
        print("You win! Paper beats rock.")
    elif user_move == "scissors" and computer_move == "paper":
        print("You win! Scissors beats paper.")
    else:
        print("You lose!",computer_move.capitalize(),"beats",user_move)
    print()

print("Thanks for playing!")
