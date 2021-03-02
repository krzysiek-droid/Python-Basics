#Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

text = input("Podaj dowolny tekst: ")

print("Przy użyciu pętli for: ")
for i in range(1,len(text),2):
    print("{}".format(text[i]),end="")
print("\nPrzy użyciu string slicing: ")
print("{}".format(text[1:len(text):2]))
