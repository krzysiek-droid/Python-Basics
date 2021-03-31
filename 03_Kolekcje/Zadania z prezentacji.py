#metoda która otworzy kopię listy?
#copy zachowuja związek z pierwowzorem
#deepcopy staje sie nowym obiektem
lista = list(range(5))
lista_1 = lista.copy()
print(lista_1)

#Metoda która posortuje elementy na liście
print(lista.sort())

#Jaka metoda usunie wszystkie elementy z listy
lista.clear()

#Policzy wystąpienia takiego samego elementu na liście
lista.count(2)

#Zsumuje liczby na liście
sum(list)
