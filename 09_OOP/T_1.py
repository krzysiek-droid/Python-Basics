class Dog:
    def __init__(self, name, color, bred, age):
        self.name = name
        self.color = color
        self.bred = bred
        self.age = age

    def bark(self):
        return 'Hau' * self.age

    def tail_wave(self):
        return f'{self.name} is waving its tail!'

Atos = Dog('Atos', 'gray', 'Malamute', 1)
Portos = Dog('Portos', 'Black', 'Labrador', 4)
Aramis = Dog('Aramis', 'Golden', 'Golden retriever', 5)

print(Atos.name)