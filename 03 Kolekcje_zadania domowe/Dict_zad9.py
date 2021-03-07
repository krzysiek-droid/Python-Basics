#5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach.
# Wyświetl najpopularniejszy przedmiot.
# (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)

user1_list = []
user2_list = []
user3_list = []
user4_list = []
user5_list = []

for i in range(1,5):
    item = input(f"Użytkownik 1, podaj swój szkolny przedmiot nr. {i}: ").lower()
    user1_list.append(item)
i = 0
for i in range(1,5):
    item = input(f"Użytkownik 2, podaj swój szkolny przedmiot nr. {i}: ").lower()
    user2_list.append(item)
i = 0
for i in range(1,5):
    item = input(f"Użytkownik 3, podaj swój szkolny przedmiot nr. {i}: ").lower()
    user3_list.append(item)
i = 0
for i in range(1,5):
    item = input(f"Użytkownik 4, podaj swój szkolny przedmiot nr. {i}: ").lower()
    user4_list.append(item)
i = 0
for i in range(1,5):
    item = input(f"Użytkownik 5, podaj swój szkolny przedmiot nr. {i}: ").lower()
    user5_list.append(item)
i = 0

items_list = user1_list+user2_list+user3_list+user4_list+user5_list
items_set = set(items_list)
items_unique = list(items_set)
item_popularity = dict()

for i in range (len(items_unique)):
    item = items_unique[i]
    repeat_index = items_list.count(item)
    if repeat_index > 1:
        print(f"{item} powtarza się {repeat_index} razy")
        item_popularity.update({item:repeat_index})
#print(f"Najpopularniejszy przedmiot to: {item_popularity[max(item_popularity.values())]}")
print(item_popularity)
