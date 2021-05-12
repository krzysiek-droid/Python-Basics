
import BMI_functions as bmi

if __name__ == '__main__'
    weigth = float(input("Insert Yours weigth in kg:\t"))
    heigth = float(input("Insert Yours heigth in cm:\t")) / 100
    bmi.BMI_comment(bmi.BMI_result(weigth, heigth))
else:
    print(f"It is not a main function! {__name__}")

