# 7▹ Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
# Co wiemy o tych numerach tych kart?
# All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
# MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
# American Express card numbers start with 34 or 37 and have 15 digits.

def is_visa(number):
    number = str(number)
    if number[0] == '4':
        if len(number) == 13:
            return True
        elif len(number) == 16:
            return True
        else:
            return False
    else:
        return False

def is_mastercard(number):
    number = str(number)
    first_two = int(number[0:2])
    first_four = int(number[0:4])
    if len(number) == 16:
        if 51 <= first_two <= 55 or 2221 <= first_four <= 2720:
            return True
        else:
            return False
    else:
        return False

def is_americanexpress(number):
    number = str(number)
    first_two = int(number[0:2])
    if len(number) == 15:
        if first_two == 34 or first_two == 37:
            return True
    else:
        return False

##################### MAIN PROGRAM #######################

card_number = str(input('Give the card number to check: ')).replace(' ','')

print(card_number)

print(f'Czy jest Visa?: {is_visa(card_number)}')
print(f'Czy jest MasterCard?: {is_mastercard(card_number)}')
print(f'Czy jest AmericanExpress?: {is_americanexpress(card_number)}')
