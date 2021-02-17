# Zadanie 7
# Napisz konwerter walut.
# Program poprosi użytkownika o kwotę pieniędzy, jaką wezmą na wakacje
# a następnie przeliczy tę kwotę w euro oraz w dolarach.
# Zignoruj wszelkie centy, które mogą wyniknąć z konwersji.
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

zlote=int(input("Jaka kwotę w złotówkach chcesz przeznaczyć na wakacje?: "))

kurs_euro=float(input("Podaj kurs euro (separator \".\"): "))
kurs_dolar=float(input("Podaj kurs dolara (separator \".\"): "))

print("\nChcesz wziąć: ", int(zlote*kurs_euro),"euro lub", int(zlote*kurs_dolar),"dolarów")