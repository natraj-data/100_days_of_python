# Day 4 Project
# Rock, Paper , Scissor game

import random as r
print("Welcome to Play the Rock , Paper , Scissor game")
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for paper , 2 for Scissor. \n"))
computer_choice = r.randint(0, 2)
game_string = ["rock", "paper", "scissors"]
print("User choice is : ", game_string[user_choice])
user_signal = rock if game_string[user_choice] == "rock" else paper if game_string[user_choice] == "paper" else scissors
print(user_signal)
print("Computer choice is : ", game_string[computer_choice])
computer_signal = rock if game_string[computer_choice] == "rock" else paper if game_string[computer_choice] == "paper" else scissors
print(computer_signal)
if 0 <= user_choice < 3:
    if user_choice == computer_choice:
        print("Match Draw")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1) or (user_choice == 1 and computer_choice == 0):
        print("You win")
    else:
        print("Computer wins")
else:
    print("You have chosen the wrong input! Try again with right input")
