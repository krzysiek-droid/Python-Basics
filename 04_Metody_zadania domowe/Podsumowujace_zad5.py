#5▹ Napisz grę ciepło - zimno tak, aby korzystać z funkcji.
hidden_number = 135

def check_closeness(number):
    distance = abs(hidden_number-number)
    if distance == 0:
        return f'Brawo! Udało Ci się trafić'
    elif distance <= 5:
        return f'Gorąco!'
    elif distance > 5 and distance < 10:
        return f'Ciepło!'
    elif distance >= 10 and distance < 15:
        return f'Zimno'
    elif distance >= 15:
        return f'Totalny chłód'


repeats = int(input('Ile razy chcesz spróbować?: '))
for i in range(repeats):
    user_hit = int(input('Podaj swoją liczbę całkowitą: '))
    print(check_closeness(user_hit))
