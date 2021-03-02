#1) Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
#C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
#Napisz rozwiązanie zarówno z użyciem pętli while jak i for.

Farenheit=0
while Farenheit<201:
    Celcius = int((5/9)*(Farenheit-32))
    print(Farenheit,"Farenheit'a to",Celcius,"stopni Celcjusza")
    Farenheit=Farenheit+20

# for Farenheit in range(0, 201, 20):
#     Celcius = int((5 / 9) * (Farenheit - 32))
#     print(Farenheit,"Farenheit'a to", Celcius, "stopni Celcjusza")