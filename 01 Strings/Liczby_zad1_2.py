#https://python2021.netlify.app/python_types.html
#1. Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
#Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.
#2. Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.

dystans=float(input("Podaj dystans w km: "))
spalanie=float(input("Podaj spalanie na 100 km [separator \".\"]: "))
cena=float(input("Podaj cenę benzyny w zł [separator \".\"]: "))

koszt= (dystans/100)*spalanie*cena
print("\nPaliwo na wycieczkę wyniesie Cię: ",round(koszt,2),"zł")
