#Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę
#ukrytą przez programistę wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.

number_user = int(input("Podaj zgadywaną liczbę (całkowitą): "))
number_programmer = 57

if number_user==number_programmer:
    print("Gratulacje!")
else:
    print("Pudło!")
