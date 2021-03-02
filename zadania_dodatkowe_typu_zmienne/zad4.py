# Zadanie 4
# Napisz skrypt, który zapyta użytkownika o trzy liczby całkowite,
# a następnie pomnóż dwa pierwsze. przed podzieleniem wyniku przez trzecią liczbę. 
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

l1=int(input("Podaj pierwsza liczbę calkowitą l1: "))
l2=int(input("Podaj kolejną liczbę l2: "))
l3=int(input("Podaj ostatnią liczbe l3: "))

iloczyn=l1*l2
iloraz=int(iloczyn/l3)

print("\nWynik operacji (l1*l2)/l3 to: ", iloraz)