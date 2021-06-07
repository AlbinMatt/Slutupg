from discord.ext import commands
import os
import discord
import random

class memes(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command( help= "memes") #sickar ut meme när man skriver meme
    async def meme (self, ctx): 
        meme=random.choice(os.listdir("./memes"))
        with open(f"./memes/{meme}","rb") as f:
            img=discord.File(f)
            await ctx.send(file=img)
  

def setup(client):
    client.add_cog(memes(client))