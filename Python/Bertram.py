import os
import discord
from discord.ext import commands
from datetime import datetime, timezone

TOKEN = open("secret.key").read()

help_command = commands.DefaultHelpCommand(no_category = "Commands")
client = commands.Bot(command_prefix=commands.when_mentioned_or("."), case_insensitive=True, help_command=help_command) #prefix för att botten förstår

@client.command(name="Load", aliases=["reload"]) #ladar om cogsen och ger fellmedlanden
async def load(ctx, extension): 
    try:
        client.load_extension(f"cogs.{extension}")
    except:
        try:
            client.unload_extension(f"cogs.{extension}")
            client.load_extension(f"cogs.{extension}")
        except:
            await ctx.message.add_reaction("👎")
        else:
            await ctx.message.add_reaction("🔄")
    else:
        await ctx.message.add_reaction("👍")


# Laddar alla cogs när botten statars
for fileName in os.listdir("./cogs"):
    if fileName.endswith(".py"):
            client.load_extension(f"cogs.{fileName[:-3]}")

client.run(TOKEN)