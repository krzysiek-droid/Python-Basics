#2▹ Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz
# set S_test = {1, 2, 3, 4}. Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?

L_test = [1, 2, 3, 4]
T_test = (1, 2, 3, 4)
S_test = {1, 2, 3, 4}

T_test.append #nie
L_test.append() #tak
S_test.apped #nie

L_test.remove() #tak
T_test.remove   #nie
S_test.remove() #tak

L_test.extend()
T_test.extend #nie
S_test.extend   #nie

L_test.insert()
T_test.insert   #nie
S_test.insert   #nie

L_test.pop()
T_test.pop  #nie
S_test.pop()    #tak

L_test.clear()
T_test.clear    #nie
S_test.clear()  #tak