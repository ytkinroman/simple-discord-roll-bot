import random
import discord

from discord.ext import commands

client = commands.Bot(command_prefix='$')
client.remove_command('help')


@client.command()
async def roll(ctx, num=100):
    res = random.randint(1, num)
    await ctx.send(f'_You rolled {res} out of {num}._')


@client.command()
async def help(ctx):
    await ctx.send('_GitHub: <https://github.com/ytkinroman/simple-discord-roll-bot>_')


client.run('TOKEN')
