# Random Roller

A not very interesting die & dice rolling simulator.
This is mostly so I can play with different of randoms

## Requirements

Currently requires a TrueRNG device plugged into the machine

## Library

in randomroller there is Die (a single die),
and Dice (a group of die all with the same side)

```python
from randomroller import Die
d = Die(100)
print(d.roll())

from randomroller import Dice
d2 = Dice(2, 20)
print(d2.roll())
print('Show me each die roll instead of the total: ', d2.rolls())
```

## Cli

THis adds the `rr` command that takes two arguments

* dice count
* number of sides for the dice

ex: `rr 1 6` rolls 1d6
