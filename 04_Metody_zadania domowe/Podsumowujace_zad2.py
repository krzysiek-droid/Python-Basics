#2▹ Nie korzystając z funkcji wbudowanej min(), napisz
# funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).

def minium(a,b,c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c




print(minium(4, 24, 5))
