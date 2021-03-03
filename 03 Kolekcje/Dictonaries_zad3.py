#3▹ Utwórz dowolną tablicę n x n zawierającą dowolny znak,
# a następnie wyświetl jej elementy w formie tabeli n x n. Elementy powinny być oddzielone spacją

n = 5
array = [['+']*n]*n

for i in range(n):
    print(" ".join(array[i]))