from .die import Die


class Dice:
    def __init__(self, count=1, sides=6):
        """
        A set of die all with the same number od sides.
         IE. four six-sided dice
        :param count: Int number of dice
        :param sides: Int number of sides the dice have
        """
        assert isinstance(count, int)
        if count <= 0:
            raise ValueError("You cannot have less than one die")
        self.count = count
        self.die = Die(sides)

    def __str__(self):
        return '{}{}'.format(self.count, self.die)

    def __repr__(self):
        return 'Dice({}, {}'.format(self.count, self.die.sides)

    def roll(self):
        """
        Return the sum of all the dice rolls
        :return: Int
        """
        return sum(self._roller())

    def rolls(self):
        """
        Return an array of all the dice outcome
        :return: Array of Ints
        """
        return self._roller()

    def _roller(self):
        return [self.die.roll() for _ in range(self.count)]
