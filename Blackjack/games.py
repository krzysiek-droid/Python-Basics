# games.py
# Demonstruje tworzenie modułu

class Player(object):
    """ Uczestnik gry. """
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

def ask_yes_no(question):
    """Zadaj pytanie, na które można odpowiedzieć tak lub nie."""
    response = None
    while response not in ("t", "n"):
        try:
            response = input(question).lower()
            if response not in ('t', 'n'):
                raise ValueError
        except ValueError:
            print("Musisz się zdecydować, tak (T) czy nie (N)?")
    return response

def ask_number(question, low, high):
    """Poproś o podanie liczby z określonego zakresu."""
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question))
        except ValueError:
            print("Podaj liczbę zamiast litery bądź znaku. ")
    return response


if __name__ == "__main__":
    print("Uruchomiłeś ten moduł bezpośrednio (zamiast go zaimportować).")
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")