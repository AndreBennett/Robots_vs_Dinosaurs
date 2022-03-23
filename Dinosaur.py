from Robot import robot


class dinosaur:
    def __init__(self, name, attack_power, health):
        self.name = name
        self.attack_power = int(attack_power)
        self.health = int(health)

Raptor = dinosaur("Blue")
print(Raptor.name)