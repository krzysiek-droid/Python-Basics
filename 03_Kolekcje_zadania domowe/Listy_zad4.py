#4▹ Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

array = []

n = int(input("Podaj parzystą liczbę elementów tablicy: "))

for i in range(n):
    array.append(int(input(f"Podaj {i}-ą liczbę: ")))
i = 0

print(array[n//2] == array[n//2+1])