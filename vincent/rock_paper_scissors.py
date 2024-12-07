import random

user_move = input("rock paper scissor : ")
moves = ["rock", "paper", "scissors"]
pc_move = random.choice(moves)

if user_move == pc_move:
    print("Tie")
elif (
    (user_move == "rock" and pc_move == "scissors")
    or (user_move == "paper" and pc_move == "rock")
    or (user_move == "scissors" and pc_move == "paper")
):
    print("User Win")
else:
    print("User Lose")
