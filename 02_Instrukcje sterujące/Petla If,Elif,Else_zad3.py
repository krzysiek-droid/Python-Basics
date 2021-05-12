#Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce.
#W zależności od wyniku dodaj komunikaty.
#Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

rate1 = int(input("Podaj ocenę w skali od 1 do 10: "))
rate2 = int(input("Podaj ocenę w skali od 1 do 10: "))
rate3 = int(input("Podaj ocenę w skali od 1 do 10: "))

rate = float((opinia1 + opinia2 + opinia3) / 3)

if opinia > 7:
    print("\nKsiążka była bardzo dobra. Średnia ocena {}/10".format(rate))
elif opinia<7 and opinia>5:
    print("\nKsiążka była przeciętna. Średnia ocena {}/10".format(rate))
else:
    print("\nKsiązka nie jest warta uwagi. Średnia ocena {}/10".format(rate))
