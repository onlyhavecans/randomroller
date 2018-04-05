#!/usr/bin/env python

import argparse
from randomroller.dice import Dice


def parse_arguments():
    parser = argparse.ArgumentParser(description="Simple but random dice roller")
    parser.add_argument("count", help="Number of dice", type=int)
    parser.add_argument("sides", help="Number of sides on each die", default=6, type=int)
    return parser.parse_args()


def main():
    args = parse_arguments()
    mydice = Dice(args.count, args.sides)
    rolls = mydice.rolls()
    print("Your rolls are:", ", ".join(map(str, rolls)))
    print("Your total is", sum(rolls))


if __name__ == '__main__':
    main()
