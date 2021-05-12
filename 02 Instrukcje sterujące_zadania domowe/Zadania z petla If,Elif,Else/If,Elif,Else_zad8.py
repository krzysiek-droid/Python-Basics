#Sortowanie.
# Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

num1 = float(input("Podaj pierwszą liczbę: "))
num2 = float(input("Podaj drugą liczbę: "))
num3 = float(input("Podaj trzecią liczbę: "))

if num1 > num2:
    if num1 > num3:
        if num3>num2:
            print("Największą liczbą jest liczba {}".format(num1))
            print("Liczby w kolejności {} - {} - {}}".format(num1,num3,num2))
        else:
            print("Największą liczbą jest liczba {}".format(num1))
            print("Liczby w kolejności {} - {} - {}".format(num1,num2,num3))
    else:
        print("Największą liczbą jest liczba {}".format(num3))
        print("Liczby w kolejności {} - {} - {}".format(num3, num1, num2))
else:
    if num2>num3:
        if num3>num1:
            print("Największą liczbą jest liczba {}".format(num2))
            print("Liczby w kolejności {} - {} - {}".format(num2, num3, num1))
        else:
            print("Największą liczbą jest liczba {}".format(num2))
            print("Liczby w kolejności {} - {} - {}".format(num2, num1, num3))
    else:
        print("Największą liczbą jest liczba {}".format(num3))
        print("Liczby w kolejności {} - {} - {}".format(num3, num2, num1))
