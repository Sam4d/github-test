import discord
from discord.ext import commands 

#importing discord via developer portal & discord.py

client = commands.Bot(command_prefix = '^')

#setting up the basic prefix for bot commands.

@client.event
async def on_ready():
	print('the bot is ready')

#initial event to ensure there are no errors in starting a bot, prints on success.

@client.event
async def on_member_join(member):
	print(f'(member) has joined the server, Okaeri!')

#member joining the server event

@client.event
async def on_member_remove(member):
	print(f'(member has left the server, Itterasshai~')

#member leaving the server event

@client.command()
async def ping(ctx):
	await ctx.send('owo!')

client.run('Nzc3NzYxODQ3NTM3MzAzNTU0.X7IJKg.5KbSgsvM-Q-kW91k7rYPDgmpQIA')
#the original token which is generated from discord's developer portal (developers/appications/bot)
