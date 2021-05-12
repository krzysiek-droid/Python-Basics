#7▹ Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
copied_list = example_list.copy()
length = len(example_list)
list_to_tuple = []
for i in range(len(example_list)):
    checked_number = example_list[i]
    if not example_list.count(checked_number) > 1:
        list_to_tuple.append(example_list[i])
i=0
example_tuple = tuple(list_to_tuple)

min_value = min(example_tuple)
max_value = max(example_tuple)

print(f"Krotka bez duplikatu: {example_tuple} \n"
      f"Minimalna wartośc w krotce: {min_value} \n"
      f"Maksymalna wartośc w krotce: {max_value}")

