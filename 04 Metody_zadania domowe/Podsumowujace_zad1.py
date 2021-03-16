#1▹ Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika
# oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

def bmi_indicator(mass,heigth):
    bmi = mass / (heigth ** 2)
    return round(bmi, 0)

def bmi_range(bmi):
    if bmi < 17:
        return f'Twoje BMI wynosi {bmi} i oznacza wygłodzenie. Jeśli masz problemy z jedzeniem, zgłoś się do lekarza.'
    elif bmi >= 17 and bmi < 18.5:
        return f'Twoje BMI wynosi {bmi} i masz NIEDOWAGĘ!'
    elif bmi >= 18.5 and bmi < 25:
        return f'Twoje BMI wynosi {bmi} i jest w normie.'
    elif bmi >= 25 and bmi < 30:
        return f'Twoje BMI wynosi {bmi} i masz nadwagę.'
    elif bmi >= 30:
        return f'Twoje BMI wynosi {bmi} i oznacza otyłość. Zgłoś się do lekarza.'

##############################main program#############################

mass = int(input("Podaj masę swojego ciała, [kg]: "))
height = int(input('Podaj swoją wysokość, [cm]: '))/100

print(bmi_range(bmi_indicator(mass,height)))

