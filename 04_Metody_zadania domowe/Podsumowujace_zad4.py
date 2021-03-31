#4▹ Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

def is_in_range(scope1,scope2,number):
    if scope1 <= number <= scope2:
        return f'Tak, liczba {number} znajduję się w podanym zakresie'
    else:
        return f'Nie, liczba {number} nie znajduje się w podanym zakresie'



print('Podaj zakres licz całkowitych w którym chcesz szukać liczby')
lower_limit = int(input('od: '))
upper_limit = int(input('do: '))

searched = int(input('Podaj liczbę całkowitą której szukasz: '))

print(is_in_range(lower_limit,upper_limit,searched))

