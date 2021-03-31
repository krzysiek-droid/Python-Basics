#3▹ Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym
# indeksie z pierwszej krotki, a oraz nieparzystych elementów z drugiej. Przekształć powstałą listę w set.

first_tuple = (12,32,3,112,43,23,12,4,35,13,12)
second_tuple = (53,531,234,3,14,253,41,324,51,2)

list_1 = list(first_tuple[0::2]+second_tuple[1::2])
list_1 = set(list_1)

print(list_1)