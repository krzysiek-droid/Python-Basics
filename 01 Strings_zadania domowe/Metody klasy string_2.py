#Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.;

s1 = input("Podaj pierwszy wyraz: ")
s2 = input("Podaj drugi wyraz: ")
liczba_znakow_s1 = len(s1)
polowa = liczba_znakow_s1//2
s3 = s1[0:polowa]+s2+s1[polowa::]
print("\n",s3)