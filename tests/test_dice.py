import unittest
from randomroller import Dice


class TestDice(unittest.TestCase):
    def setUp(self):
        self.oneDOne = Dice(1, 1)
        self.fiveDFive = Dice(5, 5)
        self.hundredDSix = Dice(100)

    def testGreaterThanZero(self):
        with self.assertRaises(ValueError):
            Dice(-1,6)
        with self.assertRaises(ValueError):
            Dice(1,-6)
        with self.assertRaises(ValueError):
            Dice(0,6)
        with self.assertRaises(ValueError):
            Dice(1,0)

    def testIntArguments(self):
        with self.assertRaises(AssertionError):
            Dice("cats",0)

    def testSring(self):
        self.assertEqual(str(self.oneDOne), "1d1")
        self.assertEqual(str(self.hundredDSix), "100d6")

    def testRange(self):
        for _ in range(500):
            self.assertGreaterEqual(self.fiveDFive.roll(), 5)
            self.assertLessEqual(self.fiveDFive.roll(), 25)

    def testRollsCount(self):
        self.assertEqual(len(self.hundredDSix.rolls()), 100)
        self.assertEqual(len(self.oneDOne.rolls()), 1)
