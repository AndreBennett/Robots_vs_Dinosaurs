from Robot import robot


class dinosaur:
    def __init__(self, name, attack_power, health):
        self.name = name
        self.attack_power = int(attack_power)
        self.health = int(health)

R2D2 = robot("R2D2")
print(R2D2.name)