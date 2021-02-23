import discord
from discord.ext import commands

client = commands.Bot(command_prefix="your prefix", case_insensitive = True)

@client.event
async def on_ready():
    print("Bot is ready")
    print(f"Logged in as {client.user}") # Will say the bots full name like testbot#6754

@client.command()
async def hi(ctx):
    ctx.send("hi")

@client.command()
@commands.is_owner() # Makes the command accessable to the owner of the bot or the person who made it.
async def say(ctx, say = None):
    if say == None:
        ctx.send("You gave me nothing to send.")
    else:
        ctx.send(say)



client.run('token')