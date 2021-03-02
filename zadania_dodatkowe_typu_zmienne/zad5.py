# Zadanie 5
# Napisz program, który pyta użytkownika o 2 liczby
# a następnie dzieli jedna przez drugą.
# Pokaż ile razy pierwsza liczba mieści się w drugiej
# oraz jaka jest reszta tego dzielenia. 

l1=int(input("Podaj pierwszą liczbę (Licznik): "))
l2=int(input("Podaj drugą liczbę (Mianownik): "))

print("\nWynik dzielenia podanych liczb: ",round(l1/l2,3))
print("Pierwsza liczba mieści się w drugiej: ",l1//l2,"razy")
print("Reszta z dzielenia podanych liczb: ",l1%l2)