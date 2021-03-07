#2▹ Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

rand_tuple = (1,2,3,5,23,45,234,53,45,32452,2,2,32,3,2,23,4452,223,42,2664,2324,23)

listed_tuple = list(rand_tuple)

print(rand_tuple)
repeated_list = []
repeated_set = {}
for i in range(len(rand_tuple)):
    x = listed_tuple.count(rand_tuple[i])
    if x>1:
        repeated_list.append(rand_tuple[i])
        print(f"Element o wartości {rand_tuple[i]} powtórzył się {x} razy.")
    # else:
    #     print(f"Element {rand_tuple[i]} nie powtórzył się ani razu.")


print(f"Lista elementów powtórzonych w krotce: {repeated_list}")

#nie używałem kolekcji set do wyświetlenia ilości powtórzeń, ponieważ zadanie jest nt. krotek :)