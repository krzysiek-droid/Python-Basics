#Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry.
# Wyświetl nazwę właśnie spakowanego przedmiotu, po ostatnim przedmiocie pokaż informację: “Great, we are ready!”

things_for_mountains_trip = ["Apteczka","Prowiant","Woda","Kompas"]
for item in things_for_mountains_trip:
    print(item)

for i in range(4):
    print("Pod namiot zabiore: ", things_for_mountains_trip[i])

print("Great! We're ready!")