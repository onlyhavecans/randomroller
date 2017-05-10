import random


class Die:

    def __init__(self, sides):
        """
        A digital die construct
        :param sides: Number of sides as an int
        """
        assert isinstance(sides, int)
        self.sides = sides

    def __str__(self):
        return 'd{}'.format(self.sides)

    def __repr__(self):
        return 'Die({})'.format(self.sides)

    def roll(self):
        """
        Simulate a die roll, returning a random number
        :return: Int between 1 and the number of sides inclusive
        """
        random.seed()
        return random.randint(1, self.sides)
