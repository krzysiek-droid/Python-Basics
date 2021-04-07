# 5▹ W kodzie BMI ufamy, że użytkownik podaje wartość w kilogramach lub w metrach i rzutujemy do float.
# Co jeśli użytkownik poda wartość 60 kg ? Zmodyfikuj kod z ostatnich zajęć tak, aby wykluczyć powyższy przypadek.

def BMI_result(weigth, heigth):
    return round(weigth / (heigth ** 2), 2)


def BMI_comment(BMI):
    if BMI < 18.5:
        print(f"Your BMI is {BMI} and you are underweight.")
    elif BMI <= 25:
        print(f"Your BMI is {BMI} and it is normal! Keep it up!")
    elif BMI > 25 and BMI <= 30:
        print(f"Your BMI is {BMI} and you are overweight. Get to work and go exercise")
    elif BMI > 30:
        print(f"Your BMI is {BMI} and it is obese. See a doctor for help.")


def try_values(weight, height):
    if weight < 45 or weight > 180:
        print(f'You can not weight {weight}. Give a proper mass')
    elif height < 0.5 or height > 2.3:
        print(f'You can be as low as {height}. Give a proper height.')

try:
    weight = float(input("Insert Yours weigth in kg:\t"))
    height = float(input("Insert Yours heigth in cm:\t")) / 100
    try_values(weight, height)

except ValueError as verr:
    print('Wrong value inserted. Insert value in kilograms or cm without any additional text.')
except NameError as nerr:
    print('Wrong value inserted. Insert value in kilograms or cm. Use \'.\' operator instead of \',\'.')

BMI_comment(BMI_result(weight, height))