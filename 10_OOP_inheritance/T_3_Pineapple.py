class Pen:
    def __init__(self):
        print("Pen", end=' ')


class Apple:
    def scream_apple(self):
        print("Apple", end=' ')


class Pineapple:
    def scream(self):
        print("Pineapple", end=' ')


class PenPineapple(Pen, Pineapple, Apple):
    def __init__(self):
        print('----')
        super().__init__()
        super().scream()
        super().scream_apple()
        super().__init__()


s = PenPineapple()
