from .truerng import TrueRNG


class Die:

    def __init__(self, sides=6):
        """
        A digital die construct
        :param sides: Number of sides as an int. Defaults to 6, a standard die
        """
        assert isinstance(sides, int)
        if sides <= 0:
            raise ValueError("Die must have a number of sides greater than 0")
        self.sides = sides
        self._rng = TrueRNG()

    def __str__(self):
        return 'd{}'.format(self.sides)

    def __repr__(self):
        return 'Die({})'.format(self.sides)

    def roll(self):
        """
        Simulate a die roll, returning a random number
        :return: Int between 1 and the number of sides inclusive
        """
        return self._rng.choice(range(1, self.sides + 1))
