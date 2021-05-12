#Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
# która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość

waga=float(input("\nPodaj swoją wagę w kilogramach:\t"))
wzrost=int(input("Podaj swój wzrost w cm:\t"))/100
BMI=round(waga/(wzrost**2),2)


if BMI<18.5:
    print("Twoje BMI wynosi {} i masz niedowagę.".format(BMI))
elif BMI<=25:
    print("Twoje BMI wynosi {} i jest w normie! Tak trzymać!".format(BMI))
elif BMI>25 and BMI<=30:
    print("Twoje BMI wynosi {} i masz nadwagę. Weź się do roboty i idź poćwiczyć".format(BMI))
elif BMI>30:
    print("Twoje BMI wynosi {} i oznacza otyłośc. Zgłoś się do lekarza po pomoc.".format(BMI))

