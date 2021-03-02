# Zadanie 8
#Ulepsz program z zadania 7, tak aby zwrócił ile banknotów
# 50, 20, 10 i 5 euro otrzyma użytkownik.

zlote=int(input("Jaka kwotę w złotówkach chcesz przeznaczyć na wakacje?: "))

op=input("Chcesz przeliczyć euro czy dolary ? Podaj walutę (euro/dolar): ")

while op=="euro":
    kurs_euro = float(input("Podaj kurs euro (separator \".\"): "))
    suma_euro = zlote * kurs_euro
    print("\nW sumie chcesz zabrać: ",int(suma_euro),"euro o nominałach:")
    nominal_50 = suma_euro // 50
    reszta_50 = (suma_euro - (nominal_50 * 50))
    if reszta_50 >= 20:
        nominal_20 = reszta_50 // 20
        reszta_20 = reszta_50 % 20
        if reszta_20 >= 10:
            n_10 = reszta_20 // 10
            r_10 = reszta_20 % 10
        elif reszta_20 >= 5:
            n_5 = r_10 // 5
            r_5 = r_10 % 5
        else:
            print("\n\t", int(nominal_50), "x nominał 50\n\t", int(nominal_20), "x nominał 20 \ni\t", float(reszta_20),
                  "euro reszty")

    elif reszta_50 >= 10:
        n_10 = reszta_50 // 10
        r_10 = reszta_50 % 10
        if r_10 >= 5:
            n_5 = r_10 // 5
            r_5 = r_10 % 5
            print("\n\t", int(nominal_50), "x nominał 50\n\t", int(n_10), "x nominał 10\n\t",
                  int(n_5), "x nominał 5 \ni\t", float(r_5), "reszty")
        else:
            print("\n\t", int(nominal_50), "x nominał 50\n\t", int(n_10), "x nominał 10\ni\t", float(r_10), "reszty")

    elif reszta_50 >= 5:
        n_5 = reszta_50 // 5
        r_5 = reszta_50 % 5
        print("\n\t", int(nominal_50), "x nominał 50\n\t", int(n_5), "x nominał 5\ni\t", float(r_5), "reszty")

    else:
        print("\n\t", int(nominal_50), "x nominał 50 \ni\t", round(float(reszta_50),2), "euro reszty")
    op="koniec"
    print("\nNie ma za co:)")

while op=="dolar":
    kurs_dolar = float(input("Podaj kurs dolara (separator \".\"): "))
    suma_dolar = zlote * kurs_dolar
    print("\nW sumie chcesz zabrać: ",int(suma_dolar),"dolarów o nominałach:")
    nominal_50 = suma_dolar // 50
    reszta_50 = (suma_dolar - (nominal_50 * 50))
    if reszta_50 >= 20:
        nominal_20 = reszta_50 // 20
        reszta_20 = reszta_50 % 20
        if reszta_20 >= 10:
            n_10 = reszta_20 // 10
            r_10 = reszta_20 % 10
        elif reszta_20 >= 5:
            n_5 = r_10 // 5
            r_5 = r_10 % 5
        else:
            print("\n\t", int(nominal_50), "x nominał 50\n\t", int(nominal_20), "x nominał 20 \ni\t", round(float(reszta_20),2),
                  "euro reszty")

    elif reszta_50 >= 10:
        n_10 = reszta_50 // 10
        r_10 = reszta_50 % 10
        if r_10 >= 5:
            n_5 = r_10 // 5
            r_5 = r_10 % 5
            print("\n\t", int(nominal_50), "x nominał 50\n\t", int(n_10), "x nominał 10\n\t",
                  int(n_5), "x nominał 5 \ni\t", float(r_5), "reszty")
        else:
            print("\n\t", int(nominal_50), "x nominał 50\n\t", int(n_10), "x nominał 10\ni\t", float(r_10), "reszty")

    elif reszta_50 >= 5:
        n_5 = reszta_50 // 5
        r_5 = reszta_50 % 5
        print("\n\t", int(nominal_50), "x nominał 50\n\t", int(n_5), "x nominał 5\ni\t", float(r_5), "reszty")

    else:
        print("\n\t", int(nominal_50), "x nominał 50\ni\t", round(float(reszta_50),2), "dolarów reszty")
    op="koniec"
    print("\nNie ma za co:)")