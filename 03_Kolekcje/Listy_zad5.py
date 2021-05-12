#5▹ Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób,
# natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:
# Dorota, Wellman, dziennikarka
# Adam, Małysz, sportowiec
# Robert, Lewandowski, piłkarz
# Krystyna, Janda, aktorka
# Wyświetl w sposób przyjazny dla użytkownika

array = [
    ['dorota','wellman','dziennikarka'],
    ['adam','malysz','sportowiec'],
    ['robert','lewandowski','piłkarz'],
    ['krystyna','janda','aktorka']
    ]

for i in range(len(array)):
    print("{}.".format(i+1),' - '.join(array[i]))
