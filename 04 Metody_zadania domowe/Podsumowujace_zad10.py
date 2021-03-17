'''10▹ Stwórz grę wisielec “bez wisielca”.
Komputer losuje wyraz z dostępnej w programie listy wyrazów.
Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)
Użykownik podaje literę.
Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:
“Trafione!” oraz napis ze znanymi literami.
W przeciwnym wpadku pokaż komunikat:
“Nie trafione, spróbuj jeszcze raz!”.
Możesz ograniczyć liczbę prób do np. 10.'''
import random

def is_in_word(letter, word):
    for i in range(len(word)):
        if word[i] == letter:
            return True
    else:
        return False

def word_with_letter(word, letter,hangman_word):
    hangman_word = hangman_word.replace(' ', '')
    new_hangman = list(hangman_word)
    new_word = ''
    for i in range(len(word)):
        if word[i] == letter:
            new_hangman[i] = letter
        else:
            new_hangman[i] = hangman_word[i]

    return new_word.join(new_hangman)


avaiable_words = ['drzewo', 'samochód', 'kubek', 'książka', 'komputer']
chosen_word = random.choice(avaiable_words)
print('Zagrajmy w wisielca!\n')
hangman = '_ '*len(chosen_word)
print(f'Wylosowano słow na {len(chosen_word)} liter:\t',hangman)
rounds = 10

for i in range(10):
    user_letter = input('Podaj swoją literę: ')
    if is_in_word(user_letter, chosen_word):
        print(f'Trafione!')
        hangman = word_with_letter(chosen_word,user_letter,hangman)
        print(hangman)
    else:
        print(f'Nie trafione. Spróbuj jeszcze raz.')
