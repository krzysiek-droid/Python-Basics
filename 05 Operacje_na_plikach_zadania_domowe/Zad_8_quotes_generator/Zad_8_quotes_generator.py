import csv
import random


filename = 'quotes.csv'
with open(filename, 'r') as qr:
    quotes_read = csv.DictReader(qr)
    words = list(quotes_read)
    print(words[0])
    start = ''
    middle = ''
    qualifier = ''
    finish = ''



