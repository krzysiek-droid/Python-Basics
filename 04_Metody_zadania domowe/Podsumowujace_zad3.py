#3▹ Nie korzystając z funkcji wbudowanej max(), napisz funkcję
# znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

def maximum_number(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c


print(maximum_number(56,105,55))