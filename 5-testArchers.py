import unittest
from vikingsClasses import Archer, Soldier
from inspect import signature


class TestArcher(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.health = 100
        cls.strength = 50
        cls.archer = Archer(cls.health, cls.strength)

    def testConstructorSignature(self):
        self.assertEqual(len(signature(Archer).parameters), 2)

    def testIsSoldier(self):
        self.assertTrue(isinstance(self.archer, Soldier))

    def testHealth(self):
        self.assertEqual(self.archer.health, self.health)

    def testStrength(self):
        self.assertEqual(self.archer.strength, self.strength)

    def testShootArrowShouldBeFunction(self):
        self.assertTrue(callable(self.archer.shootArrow))

    def testShootArrowHasNoParams(self):
        self.assertEqual(len(signature(self.archer.shootArrow).parameters), 0)

    def testShootArrowReturnsNumber(self):
        damage = self.archer.shootArrow()
        self.assertTrue(isinstance(damage, int))

    def testReceiveDamageShouldBeFunction(self):
        self.assertTrue(callable(self.archer.receiveDamage))

    def testReceiveDamageHasParams(self):
        self.assertEqual(
            len(signature(self.archer.receiveDamage).parameters), 1
        )

    def testCanReceiveDamage(self):
        self.archer.receiveDamage(30)
        self.assertEqual(self.archer.health, self.health - 30)


if __name__ == '__main__':
    unittest.main()
