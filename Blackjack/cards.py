import random

class Card:
  """ Karta do gry. """
  RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  SUITS = ["c", "d", "h", "s"]

  def __init__(self, rank, suit):
      self.rank = rank
      self.suit = suit

  def __str__(self):
      rep = self.rank + self.suit
      return rep


class Hand:
  """ Ręka - karty do gry w ręku gracza. """
  def __init__(self):
      self.cards = []

  def __str__(self):
      if self.cards:
          rep = ""
          for card in self.cards:
              rep += str(card) + " "
      else:
          rep = "<pusta>"
      return rep

  def clear(self):
      self.cards = []

  def add(self, card):
      self.cards.append(card)

  def give(self, card, other_hand):
      self.cards.remove(card)
      other_hand.add(card)


class Deck(Hand):
    """ Talia kart do gry. """
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))  # !

    def shuffle(self):
        random.shuffle(self.cards)


    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Nie mogę dalej rozdawać. Zabrakło kart!")


class Unprintable_Card(Card):
  """ Karta, której ranga i kolor nie są ujawniane przy jej wyświetleniu. """
  def __str__(self):
        return "<utajniona>"

class Positionable_Card(Card):
    """ Karta, która może być odkryta lub zakryta. """
    def __init__(self, rank, suit, face_up = True):
        super().__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
      if self.is_face_up:
          rep = super().__str__()
      else:
          rep = "XX"
      return rep

    def flip(self):
      self.is_face_up = not self.is_face_up

if __name__ == "__main__":
    print("To moduł zawierający klasy do gry w karty.")
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
