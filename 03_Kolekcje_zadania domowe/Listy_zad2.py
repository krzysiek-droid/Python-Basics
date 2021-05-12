#2▹ Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

print("Podaj kolejno 10 liczb\n")
array = []
array_odd = []

for i in range(10):
    array.append(int(input(f"Podaj {i}-ą liczbę: ")))

i = 0
for i in range(10):
    if array[i]%2 == 0:
        array_odd.append(array[i])
        id =+ 1

print(f"Liczbami nieparzystymi z podanych są liczby: {array_odd}")