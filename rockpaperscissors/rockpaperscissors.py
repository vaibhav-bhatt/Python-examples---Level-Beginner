
import random

actions_list = ["rock","paper","scissors"]
allowed_user_values = ["1","2","3"]
killer_dict = {"rock":"paper","paper":"scissors","scissors":"rock"}

bot_score = 0
player_score = 0
def evaluate_winner():
    global bot_score
    global player_score
    computer_choice = actions_list[random.randint(0, len(actions_list) - 1)]
    print("You: {}", user_choice)
    print("Bot: {}", computer_choice)
    if user_choice == computer_choice:
        print("Its a tie")
    elif killer_dict[user_choice] == computer_choice:
        print("Bot wins")
        bot_score = bot_score + 1
    elif killer_dict[computer_choice] == user_choice:
        print("You win")
        player_score = player_score+1

i=0
rounds = input("how many rounds do u want to play for ? \n")
rounds = int(rounds)

while i < rounds:
    user_choice = input("Enter ur choice : 1-rock ,  2-paper, 3-scissor \n")
    if user_choice not in allowed_user_values:
        print("Invalid input : the value has to be among these - 1,2,3")
        continue
    user_choice = actions_list[int(user_choice) - 1]
    evaluate_winner()
    i = i + 1

print(f"End scores: Bot = {bot_score} and Player = {player_score}")




