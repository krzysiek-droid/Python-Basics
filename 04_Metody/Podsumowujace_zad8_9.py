'''8▹ Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
Program zacznie ze stworzonym słownikiem o trzech kluczach:
marka (str)
model (str)
rocznik (int)
Wypisze ten słownik na ekran (bez żadnego formatowania)
Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
“Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
Jeśli nie spełnia powyższego warunku, wypisze komunikat:
“Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć,
czy progam również zmienia swoje zachowanie.'''
'''9▹ Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części. 
W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
ponownie wyświetl zmieniony słownik
Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności. 
Dopisz odpowiednie komunikaty.'''

def is_25y_old(year):
    if 2021 - year >= 25:
        return True
    else:
        return False


car = {'brand': 'Aston Martin',
       'model': 'DB9',
       'year': 1999,
       'original': True}
print(car)
if is_25y_old(car['year']):
    if car['original'] == True:
        print(f'Gratulacje! Twój samochód {car["brand"]} może być zarejestrowany jako zabytek.')
    else:
        print(f'Twój samochód {car["brand"]} ma zbyt mało oryginalnych części...')
else:
    print(f'Twój samochód {car["brand"]} jest jeszcze zbyt młody.')
