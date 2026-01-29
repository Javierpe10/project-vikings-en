import unittest
from vikingsClasses import WarriorMonk, Saxon, Soldier
from inspect import signature


class TestWarriorMonk(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.health = 90
        cls.strength = 60
        cls.monk = WarriorMonk(cls.health, cls.strength)

    def testConstructorSignature(self):
        self.assertEqual(len(signature(WarriorMonk).parameters), 2)

    def testIsSaxon(self):
        self.assertTrue(isinstance(self.monk, Saxon))

    def testIsSoldier(self):
        self.assertTrue(isinstance(self.monk, Soldier))

    def testHealth(self):
        self.assertEqual(self.monk.health, self.health)

    def testStrength(self):
        self.assertEqual(self.monk.strength, self.strength)

    def testAttackShouldBeFunction(self):
        self.assertTrue(callable(self.monk.attack))

    def testAttackHasNoParams(self):
        self.assertEqual(len(signature(self.monk.attack).parameters), 0)

    def testAttackReturnsNumber(self):
        damage = self.monk.attack()
        self.assertTrue(isinstance(damage, int))

    def testReceiveDamageShouldBeFunction(self):
        self.assertTrue(callable(self.monk.receiveDamage))

    def testReceiveDamageHasParams(self):
        self.assertEqual(
            len(signature(self.monk.receiveDamage).parameters), 1
        )

    def testCanReceiveDamage(self):
        self.monk.receiveDamage(20)
        self.assertEqual(self.monk.health, self.health - 20)


if __name__ == '__main__':
    unittest.main()
