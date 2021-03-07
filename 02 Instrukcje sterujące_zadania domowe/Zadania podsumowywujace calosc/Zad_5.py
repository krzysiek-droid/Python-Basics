# #5▹ Stwórz grę ciepło zimno.
# Komputer losuje liczbę z zakresu od 1 do 100.
# Użytkownik podaje swój traf.
# Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# Jeśli użytkownik zgadnie wygrywa gracz.
# Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.
import random

comp_num = random.randrange(0,100,1)

for i in range(6):
    user_num = int(input("Podaj swój traf: "))
    if comp_num == user_num:
        print("Brawo! Udało ci się trafić :)")
        break
    elif abs(comp_num - user_num) < 5:
        print("Ciepleeej")

    elif abs(comp_num - user_num)<10:
        print("Ciepłoooo")
    else:
        print("Zimnooo")
print(f"Komputer wygrał, a liczbą którą wylosował było {comp_num}")