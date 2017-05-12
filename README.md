# Random Roller

A not very interesting die & dice rolling simulator.
This is mostly so I can play with different of randoms

## Requirements
Currently requires a TrueRNG device plugged into the machine

## Library
in randomroller there is Die (a single die), and Dice (a group of die all with the same side)


```python
from randomroller import Die
d = Die(100)
print(d.roll())

from randomroller import Dice
d2 = Dice(2, 20)
print(d2.roll())
print('Show me each die roll instead of the total: ', d2.rolls())
```

## Discord bot
The whole reason I wrote this was for doing tabletop over discord. I've decided to blat it up with a script o do this.

### Instructions
1. Generate your bot, botuser, and add it to your server using [these instructions here](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token)
1. place your token in a file called `token` in this directory
1. run `python3 rollBoy.py` or however you choose to run rollBot.py
1. Create a role for your bot in discord, giving it the following permissions
    - Manage Messages
    - Read Message History
1. Assign the role to the bot
1. roll away!

### Commands
#### !purge
purge all rolls and replies from the bot. Nice for cleaning up afterwards


## Cli
THis adds the `rr` command that takes two arguments

* dice count
* number of sides for the dice

ex: `rr 1 6` rolls 1d6