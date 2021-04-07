# 6▹ Wywołaj błąd związany z otwarciem pliku.
# Spróbuj odczytać plik, który nie istnieje.
# Spróbuj odczytać wartość z pliku otwartym w trybie w
# Spróbuj utworzyć plik, który już istnieje w trybie x
# Obsłuż w dowolny sposób każdy z powyższych błędów.

# try:
#     with open('nonexistingtext.txt', 'r') as fopen:
#         handler = fopen.read()
# except FileNotFoundError as fnfe:
#     print('Your file doesnt exist.')

try:
    with open('nonexistingtext.txt', 'w') as fopen:
        handler = fopen.read()
except FileNotFoundError as fnfe:
    print('Your file doesnt exist.')