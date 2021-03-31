#1▹ Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.
#2▹ Napisać funkcję, która sprawdza czy liczba jest parzysta.
#3▹ Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.
#4▹ Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)

def circle_area(radius):
    area = radius**2*3.14
    return (area)

def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False

def sum_of_list_elems(array):
    array_sum = 0
    for element in array:
        array_sum = array_sum + element
    return array_sum

def evens_in_list(array):
    evens_list = []
    for element in array:
        if is_even(element) == True:
            evens_list.append(element)
    return f'{evens_list}'

print(circle_area(5))
print(is_even(5))
print(sum_of_list_elems([1, 2, 3, 45, 5, 6, 7, 8]))
print(evens_in_list([1,23, 3, 4, 5, 6, 7, 4, 56, 43, 23, 52]))
