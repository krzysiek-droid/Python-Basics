data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]

def month_screenout(array):
    print(f'{array[0]}')
    for n in array[1]:
        if n == 0:
            continue
        print(f'{n:02d}', end=' ')
        if n%7 == 0:
            print()
    print('\n')
    return

# *******************************MAIN PROGRAM********************************
for month in data:
    month_screenout(month)