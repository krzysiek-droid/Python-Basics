#5▹ W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
#Zadbaj o sposób wyświetlania np.:
# szybko : 5
# zbudź : 1

#"""Szybko, zbudź się, szybko, wstawaj
# Szybko, szybko, stygnie kawa
# Szybko, zęby myj i ręce"""

poem = list("Szybko, zbudź się, szybko, wstawaj, Szybko, szybko, stygnie kawa, Szybko, zęby myj i ręce".replace(",","").split())

poem_dict = {}
for word in poem:
    if word in poem_dict:
        poem_dict[word] += 1
    else:
        poem_dict[word] = 1

for key, value in poem_dict.items():
    print(key,":",value)
