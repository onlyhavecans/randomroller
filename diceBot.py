#!/usr/bin/env python3

import discord
import asyncio
import logging
from discord.ext import commands
from randomroller import Dice

description = """
I'm a hardware RNG based die roller bot!
"""

discord_logger = logging.getLogger('discord')
discord_logger.setLevel(logging.DEBUG)
log = logging.getLogger()
log.setLevel(logging.DEBUG)
#handler = logging.FileHandler(filename='rollBot.log', encoding='utf-8', mode='w')
#log.addHandler(handler)

prefix = '!'
client = commands.Bot(command_prefix=prefix, description=description)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command(pass_context=True, description="Rolls dice.\nExamples: 100 Roll 100d6\n3d10 Roll three d10")
@asyncio.coroutine
async def roll(ctx, user_roll : str):
    author = ctx.message.author
    channel = ctx.message.channel
    r = {"sides": 6, "die": 0}

    if is_int(user_roll):
        r["die"] = int(user_roll)
    elif user_roll.find('d') != -1:
        r["die"], r["sides"] = map(int, user_roll.split('d'))

    for facet in r:
        if r[facet] > 100:
            await client.send_message(channel, "Sorry {}, only 100 {} at a time".format(author, facet))
            r[facet] = 100

    try:
        d = Dice(r["die"], r["sides"])
        rolls = d.rolls()
        await client.send_message(channel, "{} rolled {} and got {} for a total of {}".format(
            author, d, ", ".join(map(str, rolls)), sum(rolls)
        ))
    except ValueError as e:
        await client.send_message(channel, "Sorry {}, I can't !roll {} because {}".format(author, user_roll, e))


@client.command(pass_context=True, description='Deletes all rolls and bot messages')
@asyncio.coroutine
async def purge(ctx):
    channel = ctx.message.channel
    deleted = await client.purge_from(channel, limit=500, check=message_is_mine_or_a_roll)
    await client.send_message(channel, 'Deleted {} message(s)'.format(len(deleted)))


def is_int(s : str):
    try:
        int(s)
        return True
    except ValueError:
        return False


def message_is_mine_or_a_roll(message):
    """
    Message checker for the purge command, used in purge_from
    :param message:
    :return: bool
    """
    if message.author == client.user:
        return True
    elif message.content.startswith(prefix):
        return True
    else:
        return False


def load_credentials():
    with open('token', 'r') as f:
        return f.readline()

if __name__ == '__main__':
    token = load_credentials()
    client.run(token)
    handlers = log.handlers[:]
    for log_handler in handlers:
        log_handler.close()
        log.removeHandler(log_handler)
