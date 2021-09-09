from weapon import Weapon
class Robot:
    def __init__(self):
        self.name = "A.D.E.E.S."
        self.health = 100 #when this hits 0, this Robot is "dead"
        self.weapon = Weapon('laser', 10)

    def attack(self, dinosaur):
       pass      

