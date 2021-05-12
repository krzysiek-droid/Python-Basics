#1▹ Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi).
# Następnie rozpakuj tę krotkę na pojedyńcze zmienne.
# Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie np.
# “Mój pies, rasy border collie wabi się Dyzio”

pet = ("pies","malamut","Atos")
(pet_type,pet_race,pet_name) = pet

print("Mój {} rasy {} wabi się {}".format(pet_type,pet_race,pet_name))
print(f"Mój {pet_type} rasy {pet_race} wabi się {pet_name}")