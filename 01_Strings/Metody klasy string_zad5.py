# zad. 5
# Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej
# np.: Kobyła ma mały bok.
# Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.


zdanie=input("\n\n\n\nWprowadz zdanie: ")
zdanie = zdanie.replace(" ","")
zdanie = zdanie.lower()
print(zdanie[::-1])
if zdanie[::-1]==zdanie:
    print("twoje zdanie jest palindromem")
else:
    print("twoje zdanie nie jest palindromem")