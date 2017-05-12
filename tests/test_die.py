import unittest
from randomroller import Die


class TestDie(unittest.TestCase):

    def setUp(self):
        self.oneSided = Die(1)
        self.sixSided = Die()
        self.tenSided = Die(10)

    def testSingleSided(self):
        self.assertEqual(1, self.oneSided.roll())

    def testDefault6(self):
        self.assertEqual(self.sixSided.sides, 6)

    def textSidesGreaterThanZero(self):
        with self.assertRaises(ValueError):
            Die(0)
        with self.assertRaises(ValueError):
            Die(-6)

    def testDistro(self):
        roll_dict = {i: 0 for i in range(1, 11)}
        for _ in range(500):
            roll_dict[self.tenSided.roll()] += 1
        for key in roll_dict:
            self.assertGreaterEqual(roll_dict[key], 1)

    def testInit(self):
        with self.assertRaises(AssertionError):
            Die("1d6")

    def testToString(self):
        self.assertEqual(str(self.oneSided), "d1")
        self.assertEqual(str(self.sixSided), "d6")
        self.assertEqual(str(self.tenSided), "d10")

if __name__ == '__main__':
    unittest.main()
