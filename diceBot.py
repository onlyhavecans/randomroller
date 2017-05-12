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


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command(pass_context=True, description='Deletes all rolls and bot messages')
@asyncio.coroutine
async def purge(ctx):
    channel = ctx.message.channel
    deleted = await client.purge_from(channel, limit=500, check=message_is_mine_or_a_roll)
    await client.send_message(channel, 'Deleted {} message(s)'.format(len(deleted)))


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
