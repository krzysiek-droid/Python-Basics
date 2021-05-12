#https://python2021.netlify.app/python_flow.html
#Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez
#użytkownika jest podzielna przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.

liczba = int(input("Podaj liczbę całkowitą: "))

if liczba%3 == 0:
    print("\nLiczba {} jest podzielna przez 3".format(liczba))
else:
    print("Liczba {} nie jest podzielna przez 3".format(liczba))
