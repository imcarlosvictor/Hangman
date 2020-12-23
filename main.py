import random
import string
from words import words


def pick_random_word(words):
    active_word = random.choice(words)
    active_word = active_word.upper()
    active_letters, active_underscore = active_word_breakdown(active_word)
    return active_word, active_letters, active_underscore


def active_word_breakdown(active_word):
    """
    Transforms the chosen word into lists.

    RETURNS:
    active_to_letters
    active_to_underscore
    """
    active_to_underscore = []

    # active_to_letters = active_word.upper()
    active_to_letters = list(active_word)
    for letter in active_to_letters:
        active_to_underscore.append('_')
    return active_to_letters, active_to_underscore


def ask_player(active_word):
    """
    Prompts and validates if the letter the player to entered is a letter.

    RETURNS:
    player_guess
    """
    while True:
        guess = input('\nEnter a letter or word: ')
        guess = guess.upper()
        if guess == active_word:
            print('\nYou are correct!\n')
            play_again()
        elif guess in string.ascii_uppercase:
            return guess
        else:
            print('\nEnter a letter in the alphabet.\n')
            continue


def update_active(active_letters, active_underscore, player_guess):
    """
    Replaces the underscore with the player's guess.

    RETURNS:
    active_underscore
    """
    guess_index = []
    # Find instances letter in active_letters
    for i, letter in enumerate(active_letters):
        if letter == player_guess:
            guess_index.append(i)
        else:
            pass
    # match the index in active_underscore to guess_index and mutate the element
    for i, letter in enumerate(active_underscore):
        if i in guess_index:
            active_underscore[i] = player_guess
        else:
            pass
    
    return active_underscore


def play_again():
    """
    Ask player if he/she wants to play again.

    RETURNS:
    play_on = True/False
    """
    play_again_ans = input('Do you want to play again? y/n: \n')
    if play_again_ans.lower() == 'y':
        return True
    else:
        print('\nThanks for playing!\n')
        return False


def main():
    previous_guesses = []
    lives = 7
    
    # Pick a random word
    active_word, active_letters, active_underscore = pick_random_word(words)

    play_on = True
    while play_on:
        print('\n')
        print(' '.join(active_underscore))

        player_guess = ask_player(active_word)

        if player_guess == active_word:
            print("""\n\n--- YOU WON! ---""")
            print(f'Answer is: {active_word}\n')

            play_on = play_again()
            # Choose a new word
            active_word, active_letters, active_underscore = pick_random_word(words)

        elif player_guess in active_letters:
            # Update the list with the player's guess
            active_underscore = update_active(
                active_letters, active_underscore, player_guess)
            # print(active_word, active_underscore)

            if active_underscore == active_letters:
                print("""\n\n--- YOU WON! ---""")
                print(f'Answer is: {active_word}\n')

                play_on = play_again()
                # Choose a new word
                active_word, active_letters, active_underscore = pick_random_word(words)

        else:
            print('\nLetter not found.')
            # Add guess to list of previous guesses
            previous_guesses.append(player_guess)
            print(f'\nYour previous guesses: {previous_guesses}')

            # Update player's lives
            lives -= 1
            if lives == 0:
                print('\n--- GAME OVER! ---')
                print(f'Answer is: {active_word}\n')
                play_on = play_again()
                active_word, active_letters, active_underscore = pick_random_word(words)
            else:
                print(f'You have {lives} lives left.\n')
                continue


if __name__ == '__main__':
    main()
