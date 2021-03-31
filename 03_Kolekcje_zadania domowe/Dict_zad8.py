#8▹ Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich.
# Zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.
# Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.

names = {
    'Grait Britain':['Olivia','Amelia','Isla','Ava','Emily','Isabella','Mia','Poppy','Ella','Lily'],
    'Austria': ['Anna',	'Hannah','Sophia','Emma','Marie','Lena','Sarah','Sophie','Laura','Mia'],
    'Belgium': ['Emma',	'Louise','Olivia','Elise','Alice','Juliette','Mila','Lucie','Marie','Camille'],
    'Netherlands': ['Anna', 'Emma','Tess',	'Sophie','Julia','Zoë',	'Evi','Mila','Sara','Eva'],
    'Ireland': ['Emily','Sophie','Emma','Grace','Lily','Sarah','Lucy','Ava','Chloe','Katie'],
    'Germany': ['Mia',	'Emma',	'Hannah','Sofia','Anna','Emilia','Lina','Marie','Lena',	'Mila'],
    'Scotland': ['Olivia','Emily','Isla','Sophie','Amelia','Jessica','Ava','Ella','Charlotte','Aria'],
    'Switzerland': ['Emma','Mia','Sofia','Lina','Lena','Lea','Lara','Emilia','Nina','Anna'],
    'Sweden': ['Alice',	'Maja',	'Lilly','Ella',	'Wilma','Ebba',	'Olivia','Astrid','Alma','Elsa'],
    'Croatia': ['Mia','Lucija','Sara','Ana','Ema','Petra','Lana','Nika','Marta','Elena']
}

names_list = list(names['Grait Britain']+names['Austria']+names['Belgium']+names['Netherlands']+names['Ireland']+
              names['Germany']+names['Scotland']+names['Switzerland']+names['Sweden']+names['Croatia'])

print(len(names_list))
print("Imiona które występujące w conajmniej 3 krajach:")
names_set = set(names_list)
names_unique_list = list(names_set)

for i in range (len(names_unique_list)):
    name = names_unique_list[i]
    if names_list.count(name) >= 3:
        print(f"{name}, ",end="")