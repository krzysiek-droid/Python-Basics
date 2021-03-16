# 1▹ Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.
# 2▹ Napisać funkcję, która sprawdza czy liczba jest parzysta.
# 3▹ Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.
# 4▹ Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)
import math


def circle_area(given_radius):
    print(f"The area of circle with {given_radius} radius is: {round((given_radius**2)*math.pi,2)}")

def is_even (number):
    if number%2 == 0:
        print(f"Given number is an even number")
    else:
        print(f"Given number is not an even number")

def sum_of_numbers (numbers):
    numbers_sum = 0
    for number in numbers:
        numbers_sum = numbers_sum + number
    return numbers_sum

circle_area(5)
print(sum_of_numbers([1,2,3,4,5,6]))