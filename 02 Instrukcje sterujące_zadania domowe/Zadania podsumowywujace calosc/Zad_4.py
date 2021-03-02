#▹ Napisz grę - kamień (k) / papier (p) / nożyce (n).
# Użytkownik podaje jedną z 3 figur.
# Komputer losuje jedną z 3 figur.
# Sprawdź kto wygrał tę rundę.
# Zmień kod tak, by użytkownik mógł podac liczbę rund.
# Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
# Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

import random

user_choice = input("Podaj jedna z figur: kamień (k), papier (p) czy nożyce (n)?: ")
program_choice = "kpn"
variable = random.randrange(0,2,1)

if user_choice == program_choice[variable]:
    print("brawo")
    print("Program wylosował {}".format(program_choice[variable]))
else:
    print("sprobuj ponownie")
    print("Program wylosował {}".format(program_choice[variable]))