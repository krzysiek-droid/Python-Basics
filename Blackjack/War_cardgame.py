import cards as crd
import games as gms


class War_card(crd.Positionable_Card):
    ACE_VALUE = 14

    @property
    def value(self):
        if self.is_face_up:
            v = War_card.RANKS.index(self.rank)
            if v == 0:
                v = 14
            elif v == 10:
                v = 11
            elif v == 11:
                v = 12
            elif v == 12:
                v = 13
        else:
            v = None
        return v

class War_hand(crd.Hand):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        rep = self.name + " wyrzuca: " + super().__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
            return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        # zsumuj wartości kart, traktuj każdego asa jako 1
        t = 0
        for card in self.cards:
            t += card.value
        return t

class War_Player(War_hand):
    def __init__(self, name):
        super(War_Player, self).__init__(name)
        self.rounds_won = 0

    def add_round(self):
        self.rounds_won += 1
        return self.rounds_won

class War_Dealer(War_hand):
    pass

class War_Deck(crd.Deck):
    def populate(self):
        for suit in War_card.SUITS:
            for rank in War_card.RANKS:
                self.add(War_card(rank, suit))  # !

class War_game(object):
    """ Gra w wojne. """

    def __init__(self, names):
        self.players = []

        for name in names:
            player = War_Player(name)
            self.players.append(player)

        self.dealer = War_Dealer("Rozdający")
        self.deck = War_Deck()
        self.deck.populate()
        self.deck.shuffle()

    # @property
    # def still_playing(self):
    #     sp = []
    #     for player in self.players:
    #         if not player.is_busted():
    #             sp.append(player)
    #     return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting() == 't':
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def who_wins_round(self):
        tmp_list = []
        for player in self.players:
            tmp_list.append(player.total)
        wins = max(tmp_list)
        winner = None
        for player in self.players:
            if player.total == wins:
                winner = player
        return winner


    def who_wins_game(self):
        tmp_list = []
        for player in self.players:
            tmp_list.append(player.rounds_won)
        wins = max(tmp_list)
        winner = None
        for player in self.players:
            if player.rounds_won == wins:
                winner = player
        return winner


    def score(self):
        for player in self.players:
            print(f"{player.name} has won {player.rounds_won} rounds", end=" | ")


    def clear_player_hands(self):
        for player in self.players:
            player.clear()

    def play(self):
        rounds = 1
        again = gms.ask_yes_no("Czy chcesz rozpocząć gre? (T)/(N)")
        while len(self.deck.cards) >= len(self.players) and again == "t":

            print(f"******************ROUND {rounds}*******************")
            self.score()
            print()
            self.deck.deal(self.players, per_hand=1)
            print(f"Pozostało {len(self.deck.cards)} kart w talii!")
            print()
            for player in self.players:
                print(player, end=" | ")
            print()
            winner = self.who_wins_round()
            print(f"The winner of {rounds} round is {winner.name}")
            winner.add_round()
            self.clear_player_hands()
            rounds += 1
            print()
            again = gms.ask_yes_no("Kontynuować? (T)/(N)")
        winner = self.who_wins_game()
        print("**********************************************************************************")
        print(f"\n\t{winner.name} Wygrał Wojnę! Gratulację!!")
def main():
    print("\t\tWitaj w grze 'Wojna'!\n")
    names = []

    number = gms.ask_number("Podaj liczbę graczy (3 - 7): ", low=1, high=8)

    for i in range(number):
        name = str(input(f"Wprowadź nazwę gracza nr {i + 1}: ")).capitalize()
        try:
            if name[0].isdigit():
                raise ValueError
        except ValueError:
            print("Nazwa nie może zaczynać się od cyfry!")
        names.append(name)
        print()

    game = War_game(names)

    again = None
    while again != "n":
        game.play()
        again = gms.ask_yes_no("\nCzy chcesz zagrać ponownie?: ")


if __name__ == '__main__':
    main()
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")