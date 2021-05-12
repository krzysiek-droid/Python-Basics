# 4▹ Oblicz średnią arymetyczną z kilku liczb. Liczby będą podane przez użytkownika po przecinku.
# Napisz funkcję, która przyjmie wartości i wyświetli średnią.
# Program powinen być odporny na błędy użytkownika. Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.

def average(numbers_list):
    result = 0
    for number in numbers_list:
        result += number
    result /= len(numbers_list)
    print(f'The average of inserted number is: {result}')


# main program

user_numbers = []

for i in range(4):
    try:
        user_num = float(input('Insert your number: '))
        user_numbers.append(user_num)
    except (ValueError, TypeError) as VERR:
        with open('zad_4_errors', 'w') as errors:
            handler = errors.write(f'{VERR}')

average(user_numbers)