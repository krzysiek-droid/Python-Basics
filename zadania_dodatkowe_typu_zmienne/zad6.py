# Zadanie 6
# Zarówno lodówka, jak i winda mają wysokość, szerokość i głębokość. 
# Dowiedz się, ile miejsca pozostało w windzie, gdy lodówka jest w środku.
# Załóżmy, że wymiary lodówki zawsze będą mniejsze niż windy (jest to prawdopodobne)
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.


d_l=int(input("Podaj długość lodówki [mm]: "))
s_l=int(input("Podaj szerokość lodówki [mm]: "))
w_l=int(input("Podaj wysokośc lodówki [mm]: "))
V_l=int(d_l*s_l*w_l)


d_w=int(input("Podaj długość windy [mm]: "))
s_w=int(input("Podaj szerokość windy [mm]: "))
w_w=int(input("Podaj wysokośc windy [mm]: "))
V_w=int(d_w*s_w*w_w)


if w_l>w_w:
    print("Lodówka jest za wysoka!")
else:
    print("\nPo umieszczeniu lodówki w windzie, pozostanie ", d_w-d_l, "mm na", s_w-s_l, "mm wolnej powierzchni o wysokości ",
          w_w, "mm tj.", V_w-V_l, "mm3")