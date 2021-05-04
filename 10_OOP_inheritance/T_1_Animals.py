class Animals:
    def __init__(self):
        print('I AM THE FATHER OF ALL MAMMALS')


class Mammals(Animals):
    def __init__(self):
        print('I am only  mammal')


class Cats(Mammals):
    pass


class Dogs(Mammals):
    pass


class Humans(Mammals):
    pass


kotek = Cats()
print(kotek)
piesek = Dogs()

czlowiek = Humans()
