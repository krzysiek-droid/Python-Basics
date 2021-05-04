class country:
    def __init__(self, name,  area_km2, population, off_language, capital_city):
        self.name = name
        self.area = area_km2
        self.population = population
        self.off_language = off_language
        self.capital_city = capital_city
    pass




if __name__ == "__main__":
    poland = country("Poland", 312000, "38 Millions", "Polish", "Warsaw")
    great_britain = country("Great Britain", 245000, "67 Millions", "English", "London")
    germany = country("Germany", 358000, "83 Millions", "German", "Berlin")

    countries = [poland, great_britain, germany]
    for country in countries:
        print(f"Country {country.name} has {country.population} of citizens living on the area of {country.area} square kilometers")



