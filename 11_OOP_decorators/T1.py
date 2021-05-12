def uppercase_decorator(func):
    def wrapper():
        return func().upper()
    return wrapper


@uppercase_decorator
def lorem_ipsum():
    return 'lorem ipsum'


print(lorem_ipsum())