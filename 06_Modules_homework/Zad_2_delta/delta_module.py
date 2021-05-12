import math

def square_eq(a,b,c):
    delta = b**2 - 4*a*c
    x1 = 0
    x2 = 0
    if delta < 0:
        return 'Given parameters have no solution, D<0'
    elif delta == 0:
        x1 = -b / (2*a)
        return f'The single solution (delta=0) is: {x1}'
    elif delta > 0:
        x1 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        solution = [x1, x2]
        return f'Quadratic equation of given arguments have two solutions: {round(x1, 3)} and {round(x2, 3)}'