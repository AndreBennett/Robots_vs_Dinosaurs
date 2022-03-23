from Weapon import weapon

class robot:
    def __init__(self, name, health):
        self.name = name
        self.health = int(100)
        self.weapon = weapon 

R2D2_name = robot("R2D2", int)
print(R2D2_name.name,)

