# W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.

text = input("Podaj ciąg znaków: ")

lower_cases = 0
upper_cases = 0
digits = 0
marks = 0
space = 0
for i in text:
    if i.islower():
        lower_cases = lower_cases + 1
print("W Twoim ciągu jest {} małych liter".format(lower_cases))

for i in text:
    if i.isupper():
        upper_cases = upper_cases + 1
print("W Twoim ciągu jest {} dużych liter".format(upper_cases))

for i in text:
    if i.isdigit():
        digits = digits + 1
print("W Twoim ciągu jest {} małych liter".format(digits))

for i in text:
    if i.isspace():
        space = space + 1

marks = len(text) - lower_cases - upper_cases - digits - space
print("W Twoim ciągu jest {} znaków specjalnych".format(marks))
