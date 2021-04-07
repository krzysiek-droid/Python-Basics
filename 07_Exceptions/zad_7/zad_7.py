# 7▹ Wróć do pierwszego zadania z lekcji o plikach, zmodyfikuj go tak, aby to użytkownik podawał nazwę pliku z cytatami.
# Pamiętaj, by użytkownik po wykonaniu błędnej akcji (np. literówki w nazwie pliku) miał możliwość poprawić swój błąd.

import random


def first_five(array):
    for quote in array[0:5]:
        print(quote.capitalize())


if __name__ == '__main__':
    while True:
        try:
            filename = input('Insert file name for the file with quotes (w/o .txt): ') + '.txt'
            with open(filename, encoding='utf-8') as q:
                quotes = q.readlines()
                rand_quote = random.choice(quotes).split('-')
                print("*******************QUOTE FOR TODAY*********************")
                print(f'{rand_quote[0]}')
                print(f'Autor: {rand_quote[1].strip()}')
                print("*******************QUOTE FOR TODAY*********************")
                print('\n')
                print("*******************First five quotes*********************")
                first_five(quotes)
        except FileExistsError as fee:
            print("there is no such file, check spelling")
            continue
        except FileNotFoundError as fnferr:
            print("there is no such file, check spelling")
            continue
        break
else:
    print('It is not a main Code')
