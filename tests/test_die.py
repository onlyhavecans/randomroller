import unittest
from randomroller import Die


class TestDie(unittest.TestCase):

    def setUp(self):
        self.oneSided = Die(1)
        self.sixSided = Die()
        self.hundredSided = Die(100)

    def testSingleSided(self):
        self.assertEqual(1, self.oneSided.roll())

    def testDefault6(self):
        self.assertEqual(self.sixSided.sides, 6)

    def textZeroSides(self):
        with self.assertRaises(TypeError):
            Die(0)

    def textNegitiveSides(self):
        with self.assertRaises(TypeError):
            Die(-6)

    def testDistro(self):
        roll_dict = {i: 0 for i in range(1, 101)}
        for _ in range(1_000):
            roll_dict[self.hundredSided.roll()] += 1
        for key in roll_dict:
            self.assertGreaterEqual(roll_dict[key], 1)

    def testInit(self):
        with self.assertRaises(AssertionError):
            Die("1d6")

    def testToString(self):
        self.assertEqual(str(self.oneSided), "d1")
        self.assertEqual(str(self.sixSided), "d6")
        self.assertEqual(str(self.hundredSided), "d100")

if __name__ == '__main__':
    unittest.main()
