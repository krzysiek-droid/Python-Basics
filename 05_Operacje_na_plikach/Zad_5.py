#Wykorzystaj plik zawierający fragment Pana Tadeusza. Znajdź najdłuższe słowo występujące w zadanym fragmencie.

def read_from(file):
    with open(file, encoding='utf-8') as fp:
        content = fp.read().replace('.', '').replace(',', '').replace(';', '').replace('!', '')
        content.split()
    return content

inwokacja = read_from('Pan_Tadeusz_Inwokacja.txt').split()
longest = ''
for word in inwokacja:
    if len(word) > len(longest):
        longest = word
print(f'\nThe longest word is: "{longest}", and has {len(longest)} letters.')