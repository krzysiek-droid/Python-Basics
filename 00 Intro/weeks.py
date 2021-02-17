waga=int(input("\npodaj swoją wagę w kilogramach:\t"))
wzrost=int(input("podaj swój wzrost w cm:\t"))/100
BMI=round(waga/(wzrost**2),2)
print("\nTwoje BMI to:",BMI)