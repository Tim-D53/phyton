# 1
"""
class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population


    def add(self, country1):
        name = self.name + " " + country1.name
        add_population = country1.population + self.population
        return Country(name, add_population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)
"""
# 2
"""
class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population


    def __add__(self, country1):
        name = self.name + " " + country1.name
        add_population = country1.population + self.population
        return Country(name, add_population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)
"""
# 3
"""
class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
    
    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed = max(0, self.speed - 5)

    def display_speed(self):
        print(f"The current speed of {self.brand} {self.model} ({self.year}) is {self.speed} km/h.")
"""