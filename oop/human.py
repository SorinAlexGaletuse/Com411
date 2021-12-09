class Human:
    MAX_ENERGY = 100

    def __init__(self,name="Human",age=0):
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f"Human(name={self.name}, age={self.age}, energy={self.energy})"

    def __str__(self):
        return f"My name is {self.name} i am {self.age} of age and my stamina is {self.energy}"

    def grow(self):
        self.age += 1

    def move(self, distance):
        human_energy = self.energy - distance
        if(human_energy<0):
            self.energy=0
            return self.energy - human_energy
        else:
            self.energy = human_energy
            return 0

    def eat(self, amount):
        human_energy = self.energy + amount
        if(human_energy>Human.MAX_ENERGY):
            self.energy = Human.MAX_ENERGY
            return human_energy - self.energy
        else:
            self.energy = human_energy
            return 0


if (__name__ == "__main__"):
  human = Human()
  human.display()
  print(repr(human))
  print(str(human))
  human.move(50)
  print(repr(human))
  human.eat(25)
  print(repr(human))