#6▹ Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.
import random
picks = ['k', 'p', 'n']

def program_pick():
    return random.choice(picks)

def pick_translate(pick):
    if pick == 'k':
        return 'Kamień'
    elif pick == 'p':
        return 'Papier'
    else:
        return 'Nożyce'

def who_won(user_pick, program_pick):
    if user_pick == 'k':
        if program_pick == 'p':
            return f'program'
        elif program_pick == 'n':
            return f'user'
    if user_pick == 'p':
        if program_pick == 'k':
            return f'user'
        elif program_pick == 'n':
            return f'program'
    if user_pick == 'n':
        if program_pick == 'p':
            return f'user'
        elif program_pick == 'k':
            return f'program'

def round_summarize(rounds,user_points,program_points):
    print(f'\nPo rundzie {rounds}, Użytkownik zdobył {user_points} punktów, a program {program_points} punktów')
    if user_points > program_points:
        print('Jak dotąd, wygrywa Użytkownik!')
    elif user_points == program_points:
        print('Jak dotąd jest remis.')
    else:
        print('Jak dotąd wygrywa Program.')

######################### MAIN PROGRAM ##########################

user_points = 0
program_points = 0
draws = 0
total_rounds = 1

op = 'T'
while op == 'T':
    print('#'*8,f'Runda {total_rounds}','#'*8)
    user_pick = input('Podaj swój wybór; kamien [k], papier [p] czy nożyce [n]?: ').lower()
    if picks.count(user_pick) == 0:
        print('Możesz wybrać tylko k - kamień, p - papier lub n - nożyce!')
        continue
    program_choice = program_pick()
    print(f'Program wylosował: {pick_translate(program_choice)}\n')
    if user_pick == program_choice:
        print(f'Program wylosował {pick_translate(program_choice)}. Runda kończy się remisem!')
        draws += 1
    else:
        if who_won(user_pick,program_choice) == 'user':
            print(f'Rundę {total_rounds} wygrał użytkownik!')
            user_points += 1
        else:
            print(f'Rundę {total_rounds} wygrał program.')
            program_points += 1
    round_summarize(total_rounds,user_points,program_points)
    total_rounds += 1
    op = input('\nChcesz zagrać kolejną rundę? T/N: ').capitalize()

