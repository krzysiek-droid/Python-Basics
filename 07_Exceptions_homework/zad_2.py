#2▹ Utwórz dowolną krotkę zawierającą kilka wartości np. 10.
# Pozwól użytkownikowi podać dowolny index oraz wartość. Spróbuj w krotce podmienić
# wartość na zadanym indeksie. Obsłuż błąd

random_tuple = (1, 'string', 0.2, True, False, 0, 230, [], {})

try:
    user_index = int(input('Insert an index for tuple: '))
    random_tuple[user_index] = 4
except SyntaxError as serr:
    print(f'You have triggered an TypeError exception of:', serr)
except TypeError as terr:
    print(f'You have triggered an TypeError exception of:', terr)
except IndexError as ierr:
    print(f'You have triggered an IndexError exception of: {ierr}')
