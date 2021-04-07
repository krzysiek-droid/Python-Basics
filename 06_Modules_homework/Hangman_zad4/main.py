# main Code for Hangman game

import random
import hangman_module as hm

rounds = 1  # number of rounds handler

avaiable_words = open('hangman_words_database', 'r') #Opens the hangman words database in order to choose a word
avaiable_words = list(avaiable_words)
chosen_word = random.choice(avaiable_words)[:-1]

hangman = '_ ' * len(chosen_word)

print("*" * 30)
print('Let\'s play the HANGMAN!'.center(30))
print("*" * 30)
print(f'Your random word has {len(chosen_word)} letters:\t', hangman)
print("*" * 30)

# Main function of the game
while not hangman.find("_") == -1:
    print(f'ROUND {rounds}'.upper().center(30))
    print("*" * 30)
    print(f'Hangman word: {hangman}'.center(30))
    user_letter = input('Give me Yours guess letter: ')
    if hm.is_in_word(user_letter, chosen_word):
        print(f'Bang! The letter {user_letter} is actually in the guessed word')
        hangman = hm.word_with_letter(chosen_word, user_letter, hangman)
        print('\n', hangman.center(30), '\n')
    else:
        print(f'Your letter doesn\'t match any in guessed word.\n')
    rounds += 1
else:
    print("*" * 90)
    print(f"You have guessed the word {hangman.upper()} in {rounds} rounds! Good Job mate :)".center(90))
    print("*" * 90)
