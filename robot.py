from weapon import Weapon
class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon('', 10)

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power
             
weapon_adees = Weapon('laser', 10)
weapon_killbot = Weapon('hammer', 10)
weapon_slapatron = Weapon('giant hand', 10)
