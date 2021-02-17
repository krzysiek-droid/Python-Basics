#https://docs.python.org/3/library/stdtypes.html#string-methods
#Jak sprawdzic czy ciąg znaków składa się tylko z cyfr?
ciag="dsa345"
print(ciag.isdigit())

#Jak wyświetlić wyśrodkowany tekst o zadanej szerokości i dodatkowo puste miejsca wypełnić np. gwiazdką
txt='banana'
print(txt.center(15,'*'))

#Jaka metoda usunie znaki tylko z prawej strony
#print(txt.rstrip("siek"))
print(txt.rstrip("*"))
print(len(txt))

#jak sprawdzic czy ciag ma co najmniej jedna dużą literę
print(str.isupper(txt))

#ile cos występuje w danym ciągu znaków
print(txt.count('na'))