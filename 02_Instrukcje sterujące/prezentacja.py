pa = ""
magic = "hokuspokus"
for num in range(2, 10, 2):
    pa = pa + str(num) + magic[num]
    print(pa)

cookies = 5
while cookies > 0:
    print('Zjedz ciastko')
    cookies = cookies - 1
    print('Zostało jeszcze ', cookies)
    print('---------------------------')

print('\nNo nie, znowu trzeba kupić ciastka!')