#Hangman_module keeps the functions crucial for running Hangman programme

#Checks if given letter is in given word, returns Boolean
def is_in_word(letter, word):
    for i in range(len(word)):
        if word[i] == letter:
            return True
    else:
        return False


#returns the String containing letters and blank spaces
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

