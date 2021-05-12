import random

gifts = [('Perfumy', 'Dauglas'),
        ('Gry', 'Media Markt'),
        ('Książka', 'Księgarnia'),
        ('Słuchawki', 'Media Expert'),
        ('Zabawki', 'Smyk')
        ]

persons_dates = {'brat': (10, 25),
         'tata': (8, 24),
         'mama': (2, 2),
         'siostra': (5, 3),
         'dziewczyna_uro': (6, 6),
         'dziewczyna_walentynki': (14, 2),
         'dziewczyna_rocznica': (4, 9)
         }

def date_digit(date): #Funkcja zmienia date podaną jako string na 2el. listę int
    date_asdigit = []
    for text in date:
        text.replace('0', '')
        date_asdigit.append(int(text))
    return date_asdigit

def random_gift(): #Funkcja zwraca losowy prezent z listy 'gifts'
    gift = random.choice(gifts)
    return gift[0]

def occasion(date): #Funkcja zwraca tablicę 2-el. [0] Osoba, [1] Prezent losowy
    gifted = []
    for person in persons_dates:
        if persons_dates[person][0] == date[0] and persons_dates[person][1] == date[1]:
            gifted.append(person)
            gifted.append(random_gift())
    return gifted

def gift_place(gift):
    for g in range(len(gifts)):
        if gifts[g][0] == gift:
            return gifts[g][1]

#********************************MAIN PROGRAM**********************************

date = input("Podaj datę [format liczbowy, oddzielony \'.\']: ").split('.')
date = date_digit(date)

gifted = occasion(date)

print(f'Prezent dla: {gifted[0].capitalize()}, to: {gifted[1].capitalize()}')
print(f'Wylosowany prezent możesz znaleźc w : {gift_place(gifted[1]).capitalize()}')