#Stwórz zmienną password. Hasło powinno składać z liter i cyfr!,
# zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
# Wyświetl różne komunikaty w zależności od rodzaju błędu.

password = input("Podaj hasło. Hasło powinno zawierać conajmniej 1 dużą literę i mieć długość 8 znaków: ")

if len(password) < 8:
    print("Twoje hasło jest za krótkie")
if password.islower(): #islower dlatego, że ta funkcja sprawdcza czy w obiekcie są TYLKO małe (lub duże w przyp. isupper) litery!
    print("Twoje haslo musi zawierać conajmniej 1 dużą literę")
if password.isdigit() or password.isalpha():
    print("Twoje haslo musi składać się z liter i liczb!")




