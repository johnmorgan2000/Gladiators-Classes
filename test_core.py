import core
import pytest


class TestGladiator:
    def setup(self):
        self.glad = core.Gladiator('John', 1, 2, 45, 4, 5)

    def test_gladiator_str(self):
        assert str(self.glad) == "John:\nHealth: 1 ||| Rage: 2 ||| Power: 45\n"

    def test_gladiator_repr(self):
        assert repr(self.glad) == "Gladiator('John', 1, 2, 45, 4, 5)"

    def test_gladiator_init(self):
        assert self.glad.name == 'John'
        assert self.glad.health == 1
        assert self.glad.rage == 2
        assert self.glad.power == 45
        assert self.glad.attack_low == 4
        assert self.glad.attack_high == 5

    def test_attack(self):
        joe = core.Gladiator('jo', 100, 2, 45, 4, 5)
        assert self.glad.attack(joe) == joe

    def test_heal(self):
        self.bill = core.Gladiator('bill', 1, 2, 0, 4, 5)
        assert self.glad.heal() == 11
        assert self.bill.heal() == None

    def test_is_dead(self):
        self.piper = core.Gladiator('piper', 0, 1, 2, 3, 4)
        assert self.glad.is_dead() == False
        assert self.piper.is_dead() == True
