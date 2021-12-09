class Robot:
    MAX_ENERGY = 100

    def __init__(self,name="Robot",age=0):
        self.name = name
        self.age = age
        self.energy = Robot.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f"Robot(name={self.name},age={self.age},energy={self.energy})"

    def __str__(self):
        return f"My name is {self.name} and i am {self.age} years old and i have {self.energy} energy "

    def grow(self):
        self.age += 1

    def move(self, distance):
        robot_energy = self.energy - distance
        if(robot_energy<0):
            self.energy=0
            return self.energy - robot_energy
        else:
            self.energy = robot_energy
            return 0

    def eat(self, amount):
        robot_energy = self.energy + amount
        if(robot_energy>Robot.MAX_ENERGY):
            self.energy = Robot.MAX_ENERGY
            return robot_energy - self.energy
        else:
            self.energy = robot_energy
            return 0


if (__name__ == "__main__"):
  robot = Robot()
  robot.display()
  print(repr(robot))
  print(str(robot))
  robot.move(40)
  print(repr(robot))
  robot.eat(25)
  print(repr(robot))