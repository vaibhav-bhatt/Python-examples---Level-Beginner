import random

number_chosen= random.randint(1,100)

def checkIfInt(i):
    try:
        num = int(i)
        if num < 1 or num > 100:
            return False
        return True
    except ValueError:
        return False

print(
    '''
    Welcome to Higher Lower Guessing Game !
    Rules:
    1. Guess the number between 1 and 100 to match the number chosen in each round
    2. If your guess is wrong you will be shown if your guess was lower or higher.
    3. Guess the correct number in least number of attempts. 
    
    Happy Gaming !! \n
    '''
)
game_complete = False
attempts=0
def check_the_guess():
    global game_complete,attempts, number_chosen
    user_guess = input("Please enter your guess \n")
    if not checkIfInt(user_guess):
        print("Please input a valid number between 1 and 100\n")
    user_guess = int(user_guess)
    attempts += 1
    if user_guess == number_chosen:
        print(f"Congratulations!! Your guessed the number correctly in {attempts} attempts\n")
        game_complete = True
    elif user_guess > number_chosen:
        print("Your guess is higher\n")
    elif user_guess < number_chosen:
        print("Your guess is lower\n")

def play_game():
    continue_game = True
    global game_complete, attempts, number_chosen
    while continue_game:
        check_the_guess()
        if game_complete:
            choice = input("Do you want to play again? - Y/N \n")
            if choice == "N" or choice == "n":
                continue_game = False
            game_complete = False
            attempts = 0
            number_chosen = random.randint(1, 100)

if __name__ == "__main__":
    play_game()
