from random import *


class Gladiator:
    def __init__(self, name, health, rage, power, attack_low, attack_high):
        self.name = name
        self.health = health
        self.rage = rage
        self.power = power
        self.attack_high = attack_high
        self.attack_low = attack_low

    def __str__(self):
        return "{}:\nHealth: {} ||| Rage: {} ||| Power: {}\n".format(
            self.name, self.health, self.rage, self.power)

    def __repr__(self):
        return "Gladiator({},{},{},{},{},{})".format(
            self.name, self.health, self.rage, self.power, self.attack_low,
            self.attack_high)

    def attack(self, other):
        crit_damage = other.health - (
            randint(self.attack_low, self.attack_high) * 2)
        damage = other.health - randint(self.attack_low, self.attack_high)
        critical = randrange(1, 101)

        if critical <= self.rage:
            other.health = crit_damage
            self.rage = 0
            return other
        elif self.rage < critical:
            other.health = damage
            self.rage += 15
            self.power += 15
            return other

    def heal(self):
        if self.power < 10:
            return None
        elif self.power <= 0:
            self.power = 0
            return self.power
        elif self.health > 0:
            self.power -= 10
            self.health += 10
            return self.health

    def is_dead(self):
        if self.health <= 0:
            self.health = 0
            return True
        else:
            return False


class Warrior(Gladiator):
    def __init__(self, name, health, rage, power, attack_low, attack_high):
        super().__init__(name, health, rage, power, attack_low, attack_high)

    def special(self, other):
        if self.power >= 45:
            other.health -= 50
            self.power -= 45
            return
        elif self.power <= 0:
            self.power = 0
        else:
            return None
