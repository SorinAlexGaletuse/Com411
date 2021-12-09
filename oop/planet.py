from human import Human
from robot import Robot

class Planet:

    def __init__(self):
        self.population = {"humans" : [],"robots" : []}

    def add_human(self,human):
        self.population["humans"].append(human)

    def remove_human(self,human):
        self.population["humans"].remove(human)

    def add_robot(self,robot):
        self.population["robots"].append(robot)

    def remove_robot(self,robot):
        self.population["robots"].remove(robot)

    def __repr__(self):
        return f"planet(human={self.population['humans']}, robots={self.population['robots']})"

    def __str__(self):
        return f"This planet has {len(self.population['humans'])} humans and {len(self.population['robots'])} robots!"

if(__name__ == "__main__"):
    planet = Planet()
    print(repr(planet))
    salah = Human("Salah")
    planet.add_human(salah)
    mane = Human("Mane")
    planet.add_human(mane)
    firmino = Robot("Firmino")
    planet.add_robot(firmino)
    print(repr(planet))
    print(planet)