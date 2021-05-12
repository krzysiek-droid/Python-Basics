#Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_num = 57
user_num = 0

while user_num != secret_num:
    user_num = int(input("Podaj zgadywaną liczbę: "))

print("Udało ci się! Ukryta liczba to {}".format(secret_num))
