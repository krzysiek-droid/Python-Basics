def fibonacci(n):
    i = 1
    f1, f2, temp = 0, 1, 0

    while i < n:
        temp = f1 + f2
        f1 = f2
        f2 = temp
        i += 1

    return f2

