#Utwórz plik na pulpicie zawierający listę ok. 20 cytatów.
# Każdy cytat powinen się znaleźć w nowej linii. Utwórz funkcję,
# która losuje i wyświetla w sposób ciekawy cytat na dziś. Np. można wyświetlić tak:
# edit: 3▹ Wyświetl tylko 5 pierwszych linii
import random
def first_five(quotes):
    for quote in quotes[0:5]:
        print(quote.capitalize())

with open('quotes.txt', encoding='utf-8') as q:
    quotes = q.readlines()
    rand_quote = random.choice(quotes).split('-')
    print("*******************QUOTE FOR TODAY*********************")
    print(f'{rand_quote[0]}')
    print(f'Autor: {rand_quote[1].strip()}')
    print("*******************QUOTE FOR TODAY*********************")
    print('\n')
    first_five(quotes)


