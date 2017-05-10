#!/usr/bin/env python

import argparse
from randomroller.die import Die
from randomroller.dice import Dice


def parse_arguments():
    parser = argparse.ArgumentParser(description="Simple but random dice roller")
    parser.add_argument("count", help="Number of dice", type=int)
    parser.add_argument("sides", help="Number of sides on each die", type=int)
    parser.add_argument("--rolls", help="Show the rolls instead of the total", action="store_true")
    return parser.parse_args()


def main():
    args = parse_arguments()
    dice = Dice(args.count, args.sides)
    if args.rolls:
        print(dice.rolls())
    else:
        print(dice.roll())


if __name__ == '__main__':
    main()
