#Utwórz zmienną przechowującą dowolny ciąg znaków.
#Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
#Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

sign_series = "bhjfasb4392basdbfjzsasdfa"

if len(sign_series)>5 and sign_series.find("a"):
    sign_series = sign_series.replace("a","z")
    print(sign_series)
