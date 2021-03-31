#Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.
# input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
# output:
# [4, 3, 2, 1]
# [14, 13, 12, 11]
# [24, 23, 22, 21]

rand_list = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
length = len(rand_list)
list_1 = []
list_2 = []
list_3 = []
multiplier = length//3
print(multiplier)
for i in range(len(rand_list)):
    if i<multiplier:
        list_1.append(rand_list[i])
    elif i>=multiplier and i<2*multiplier:
        list_2.append(rand_list[i])
    else:
        list_3.append(rand_list[i])

list_1.reverse()
list_2.reverse()
list_3.reverse()

print(f" {list_1} \n {list_2} \n {list_3}")



