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

