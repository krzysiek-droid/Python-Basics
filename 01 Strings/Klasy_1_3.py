#https://python2021.netlify.app/python_types.html
#zad 1.
#Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.
#zadania 3.
# Do zmiennej quote przypisz zdanie:
#Honesty is the first chapter in the book of wisdom.”, a następnie:
#Policz wszystkie znaki w napisie
#Nie modyfikując zmiennej wyświetl słowo wisdom
#Wyświetl tylko pierwszą połowę tekstu
#Wyświetl tylko kropkę
#Wyświetl od połowy tylko co trzecią literę cytatu
#Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
#Wyświetl cały cytat odwrotnie
#Zamień wisdom na słowo friendship
#5. Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok.
# Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.
ciag='alaskanmalamute'
dlugosc_wyrazu=len(ciag)
srodek=dlugosc_wyrazu//2
print("\n")
print(ciag[srodek-1:srodek+2])

quote="Honesty is the first chapter in the book of wisdom."
liczba_znakow=len(quote)
print(liczba_znakow)
print(quote[-7:-1])
polowa=liczba_znakow//2
print(quote[0:polowa])
print(quote[liczba_znakow-1])
print(quote[polowa::3])
print(quote[0:liczba_znakow:2])
print(quote[::-1])
print(quote.replace('wisdom','friendship'))

