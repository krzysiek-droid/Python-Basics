import csv
import random

quote = []
filename = 'quotes.csv'
with open(filename, 'r') as qr:
    quotes_read = csv.DictReader(qr)
    words = list(quotes_read)
    start = ''
    while start == '':
        start = words[random.randint(0, len(words))]["starts"]
        quote.append(start)

    middle = ''
    while middle == '':
        middle = words[random.randint(0, len(words))]["middles"]
        quote.append(middle)

    qualifier = ''
    while qualifier == '':
        qualifier = words[random.randint(0, len(words))]["qualifiers"]
        quote.append(qualifier)

    finish = ''
    while finish == '':
        finish = words[random.randint(0, len(words))]["finishes"]
        quote.append(finish)

    random_quote = ''.join(quote)
    print(f'\nThe random quote for today is: \n',
          '*'*70, '\n',
          f'{random_quote}'.center(70), '\n',
          '*'*70)




