import random


def at_least_2_chars(text):
    for i in range(len(text) - 1):
        if text[i] == text[i+1]:
            return text[i]
    return 0


def raw_instance(characters):
    instance = []
    while len(instance) < random.randint(5, 35):
        instance.append(random.choice(characters))
    text = ''.join(instance)
    return text

def instance_generator():
    length = int(input('How many characters You want to pass? : '))

    user_chars = []

    for i in range(length):
        user_chars.append(input(f'Insert the {i+1}. character for instance generator: '))

    characters = set(user_chars)
    characters = list(characters)

    print(f'Chosen characters: {characters}')
    instance = raw_instance(characters)
    while at_least_2_chars(instance) == 0:
        instance = raw_instance(characters)
    return instance

