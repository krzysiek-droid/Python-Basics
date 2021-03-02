# #Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
# Połącz dane w jeden ciąg book za pomocą spacji
# Policz liczbę wszystkich znaków w napisie book;

tytul = input("Podaj tytuł książki: ")
autor_nazwisko = input("Podaj nazwisko autora: ")
l_stron = input ("Podaj liczbę stron: ")

#rozdzielny = tytul.find(" ")
#print(rozdzielny)
#if rozdzielny != -1:

print("\n",tytul.isalpha() and autor_nazwisko.isalpha() and l_stron.isdigit())

tytul = tytul.capitalize()
autor_nazwisko = autor_nazwisko.capitalize()

book = tytul + " " + autor_nazwisko + " " + l_stron
print("Ciąg znaków book: ",book)
book_liczba_znakow = len(book)
print("Liczba znaków w ciągu \'book\': ",book_liczba_znakow)
