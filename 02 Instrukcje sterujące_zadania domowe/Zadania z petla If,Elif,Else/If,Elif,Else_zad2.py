#Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”

l1 = int(input("Podaj pierwszą liczbę całkowitą: "))
l2 = int(input("Podaj drugą liczbę całkowitą: "))

if l1+l2>100:
    print("Suma z podanych liczb wynosi: {}".format(l1+l2))
else:
    print("Koniec")
