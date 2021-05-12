#▹ Napisz grę - kamień (k) / papier (p) / nożyce (n).
# Użytkownik podaje jedną z 3 figur.
# Komputer losuje jedną z 3 figur.
# Sprawdź kto wygrał tę rundę.
# Zmień kod tak, by użytkownik mógł podac liczbę rund.
# Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
# Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

import random

program_choice = "kpn"
variable = random.randrange(0,2,1)
program_points = 0
user_points = 0

rounds = int(input("Podaj liczbę rund: "))

for i in range(rounds):
    user_choice = input("\nPodaj jedna z figur: kamień (k), papier (p) czy nożyce (n)?: ")
    if user_choice == program_choice[variable]:
        user_points = user_points + 1
        print("Punkt dla Ciebie!")
        print("Program wylosował ({})".format(program_choice[variable]))
    else:
        program_points = program_points + 1
        print("Komputer Cię pokonał!")
        print("Program wylosował ({})".format(program_choice[variable]))
    end = input("Jeśli chcesz zakończyć, wpisz \'koniec\', jeśli nie wcisnij enter :")
    if end == "koniec":
        break
    print("Stan gry:\n\tUżytkownik wygrał {} rund \tKomputer wygrał {} rund".format(user_points,program_points))
