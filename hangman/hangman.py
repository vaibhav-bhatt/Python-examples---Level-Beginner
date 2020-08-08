import random
import re
import hangmanpics

with open("words.txt") as word_file:
    words_list = word_file.read().splitlines()

HANGMANPICS = hangmanpics.hangmanpics_list


def blankout_letters(word):
    length = len(word)
    if length > 4:
        blank_positions = random.sample(range(1, length), int(2 * length / 3))
    else:
        blank_positions = random.sample(range(1, 5), 2)
    return blank_positions


def generate_word():
    chosen_word = words_list[random.randint(0, int(len(words_list) - 1))]
    blankList = blankout_letters(chosen_word)
    chosen_word_list = list(chosen_word)
    return chosen_word, [letter if count not in blankList else "_" for count, letter in enumerate(chosen_word_list)]


chosen_word, final_word_list = generate_word()
total_attempts = 4
attempts = total_attempts
game_won = False


def guess_name():
    global attempts, final_word_list, game_won, HANGMANPICS
    print(final_word_list)
    user_input = input(f"You have {attempts} attempts remaining \n")
    fill_positions = [i.start() for i in re.finditer(user_input, chosen_word)]
    if len(fill_positions) == 0:
        attempts -= 1
        print("WRONG guess")
        print(HANGMANPICS[total_attempts - attempts - 1])
    else:
        final_word_list = [user_input if count in fill_positions else letter for count, letter in
                           enumerate(final_word_list)]
        if "_" not in final_word_list:
            print("You guessed the work correctly!")
            attempts = 0
            game_won = True
            return
        print("Correct guess")


def reset_game():
    global attempts, game_won, final_word_list, chosen_word
    chosen_word, final_word_list = generate_word()
    game_won = False
    attempts = total_attempts


def play_game():
    print(f"Guess the word in {attempts} attempts")
    while attempts > 0:
        guess_name()
    if not game_won:
        print("Hangman - You lose")
    print(f"Word was - {chosen_word}")
    play_again = input("Play again ? - Y/N \n")
    if play_again == "Y" or play_again == 'y':
        reset_game()
        play_game()

if __name__ == "__main__":
    play_game()
