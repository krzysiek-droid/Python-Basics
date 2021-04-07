# 3▹ Stwórz listę 10 elementową (różne typy!).
# Pozwól użytkownikowi podać dowolny index. Podziel 1 przez liczbę pod indexem wybranym przez użytkownika.
# Obsłuż błędy.

bad_array = [13, 'string', 2.34, 0, 'e', True, False, [], {'key': 3}, ()]

try:
    user_index = int(input('Insert choice of the index: '))
    result = 1 / bad_array[user_index]
    print(result)
except TypeError as terr:
    result = 'exception triggered'
    print(f'You have triggered an TypeError exception of:', terr)
except ValueError as verr:
    result = 'exception triggered'
    print(f'You have triggered an ValueError exception of:', verr)
except IndexError as ierr:
    result = 'exception triggered'
    print(f'You have triggered an IndexError exception of: {ierr} which means that you\'ve inserted an '
          'index bigger than the list of elements')
except ZeroDivisionError as ZDE:
    result = 'exception triggered'
    print(f'You can not divide by zero, come on! {ZDE}')