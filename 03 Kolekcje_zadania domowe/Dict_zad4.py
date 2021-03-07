#4▹ Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami mnożenia wiersz × kolumna.

columns = 10
rows = 10
array = [[0]*columns]*rows

for i in range(1,columns):    #wyświetlanie
    print("\n")
    for n in range (1,rows):
        array[i][n] = i*n
        print(f" {array[i][n]}", end="")