"""
Project porfolio 3, Code Institute
"""
import random
import os
import words
from hangman_lives import display_hangman

EASY_LEVEL = words.easy_words
MEDIUM_LEVEL = words.med_words
HARD_LEVEL = words.hard_words


def clear_terminal():
    """"
    Clear terminal
    """
    os.system(('cls' if os.name == 'nt' else 'clear'))
    title()


def title():
    """
    Display the title
    """
    print(
        """
                    _  _
                   | || | __ _  _ _   __ _  _ __   __ _  _ _
                   | __ |/ _` || ' \\ / _` || '  \\ / _` || ' \\
                   |_||_|\\__,_||_||_|\\__, ||_|_|_|\\__,_||_||_|
                                      |___/
        """
    )


def welcome():
    """
    Display a welcome title and navigate to start the game or see rules
    """
    clear_terminal()
    print('\n')
    print(' 1 PLAY GAME '.center(80))
    print(' 2 SEE RULES '.center(80))
    print('\n' * 4)
    while True:
        player_choice = input(' ' * 28 + 'Please select 1 or 2: ')
        if player_choice == '1':
            start_game()
        elif player_choice == '2':
            rules()
        else:
            print('You must choose 1 or 2'.center(77))
            print('\n')


def rules():
    """
    Display rules after the title
    """
    clear_terminal()
    print(
        """
            To play the game you must guess the letters of the hidden word.
            If the guess is correct, the letter missing in the word
            is replaced by the correct letter.
            You can enter the whole word if you know what the word is.
            Each wrong guess takes one life.
            You can choose the difficulty level,
            E for easy (10 lives), M for medium (8 lives)
            or H for hard (6 lives).
            But be careful because a harder level means more letters.
            \n
            Good luck!
            """
            )

    input(' ' * 12 + "Press enter to return to the main menu\n")
    welcome()


def set_difficulty():
    """
    This function will set the dificulty level
    depending on the user input
    """

    print('\n')
    print('Please select E for easy(10 lives),'.center(80))
    print('M for medium (8 lives) and H for hard(6 lives)'.center(80))
    difficulty = False
    while not difficulty:
        difficulty_level = input(' '.center(40)).upper()
        if difficulty_level == 'E':
            difficulty = True
            lives = 10
        elif difficulty_level == 'M':
            difficulty = True
            lives = 8
        elif difficulty_level == 'H':
            difficulty = True
            lives = 6
        else:
            print('Select E, M or H'.center(80))
    return lives


def random_word(lives):
    """
    Set the random word depending on user difficulty level
    """

    if lives == 10:
        get_words = random.choice(EASY_LEVEL).upper()
    elif lives == 8:
        get_words = random.choice(MEDIUM_LEVEL).upper()
    elif lives == 6:
        get_words = random.choice(HARD_LEVEL).upper()
    return get_words


def game(word, lives_num):
    """
    This fucntion will set the difficulty level
    and start the game
    """
    clear_terminal()
    blanks = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_word = []
    print(display_hangman(lives_num))
    print(" ".join(blanks).center(76))
    print('\n')
    while not guessed and lives_num > 0:
        print(f"Lives: {lives_num}".center(76))
        player_guess = input(' ' * 25 + 'Please guess a letter: '
                             ).upper()
        if len(player_guess) == 1 and player_guess.isalpha():
            if player_guess in guessed_letters:
                clear_terminal()
                print(' ' * 25 + 'You already guessed the letter ' +
                      player_guess)
            elif player_guess not in word:
                clear_terminal()
                print(' ' * 25 + 'Sorry ' + player_guess +
                      ' is not in the word')
                lives_num -= 1
                guessed_letters.append(player_guess)
            else:
                clear_terminal()
                print(' ' * 25 + 'Great ' + player_guess +
                      ' is in the word!')
                guessed_letters.append(player_guess)
                word_list = list(blanks)
                indices = [i for (i, letter) in enumerate(word)
                           if letter == player_guess]
                for index in indices:
                    word_list[index] = player_guess
                blanks = ''.join(word_list)
                if '_' not in blanks:
                    guessed = True
        elif len(player_guess) == len(word) and player_guess.isalpha():
            if player_guess in guessed_word:
                clear_terminal()
                print(' ' * 25 + 'You already guessed the word ' +
                      player_guess)
            elif player_guess != word:
                clear_terminal()
                print(' ' * 25 + player_guess + 'is not in the word')
                lives_num -= 1
                guessed_word.append(player_guess)
            else:
                guessed = True
                blanks = word
        else:
            clear_terminal()
            print('Not a valid guess'.center(80))
        print(display_hangman(lives_num))
        print(" ".join(blanks).center(76))
        print('\n')

    restart_game(guessed, word)


def restart_game(guessed, word):
    """
    This function will triger when user lost all his lives
    or guess a word
    """
    if guessed:
        clear_terminal()
        print('Congratulations you guessed the word'.center(80))
        print("\n")
        play_again()
    else:
        clear_terminal()
        print(' ' * 20 + 'Sorry, you run out of lives. The word was: ' +
              word)
        print("\n")
        play_again()


def play_again():
    """
    This function will start the game again or return
    to the main menu
    """
    while True:
        player_input = input(' ' * 23 +
                             'Would you like to play again? Y/N '
                             ).upper()
        print('\n')
        if player_input == 'Y':
            start_game()
        elif player_input == 'N':
            welcome()
        else:
            print('You must press Y or N'.center(80))


def start_game():
    """
    This function will start the game
    """

    clear_terminal()
    lives_num = set_difficulty()
    get_random_word = random_word(lives_num)
    game(get_random_word, lives_num)


def main():
    """
    Main function
    """

    welcome()


main()
