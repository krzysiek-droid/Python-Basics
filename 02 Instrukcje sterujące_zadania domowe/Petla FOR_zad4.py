#Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8).

number = int(input("\nPodaj liczbę naturalną,z której chcesz obliczyć silnię, ale NIE WIĘKSZĄ NIŻ 8: "))
number_silnia=1
number_list = range(number+1)
if number>8:
    print("\nBłąd! Podałeś liczbę powyżej 8. Podaj mniejszą liczbę.")
else:
    print("\n{}! =".format(number), end=" ")
    for i in range(1,number+1,1):
        number_silnia = number_silnia * number_list[i]
        if i != number:
            print(" {} *".format(number_list[i]), end=" ")
        else:
            print("{} = {}".format(number_list[i],number_silnia))