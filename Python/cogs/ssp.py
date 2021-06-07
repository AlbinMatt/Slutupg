from cogs.streak import streak
import os
import discord
from discord.ext import commands
from random import choice

lista = ["sten", "sax", "påse"]

class ssp(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def ssp(self, ctx):

        streak = self.client.get_cog("streak")
     

        botsvar = choice(lista)
        print(botsvar)
        await ctx.send('Välj sten sax eller påse!')
        def check(m):
            return m.content.lower() in ("sten", "sax", "påse") and m.channel == ctx.channel and m.author == ctx.author #Gör att bara du kan svara på ssp
        msg = await self.client.wait_for('message' , check=check)
        
        
        
        if msg.content == "sten":
            if botsvar == "sten":
                await ctx.send("Lika! \nJag valde sten")
            if botsvar =='sax':
                await ctx.send("Du vann! \nJag valde sax")
                await streak.addStreak(ctx.author)
            if botsvar =='påse':
                await ctx.send("Jag vann! \nJag valde påse")
                await streak.resetStreak(ctx.author)
        if msg.content ==  "sax":
            if botsvar == "sten":
                await ctx.send('Jag vann! \nJag valde sten')
                await streak.resetStreak(ctx.author)
            if botsvar =='sax':
                await ctx.send('Lika! \nJag valde sax')
            if botsvar =='påse':
                await ctx.send('Du vann! \nJag valde påse') 
                await streak.addStreak(ctx.author)
        if  msg.content == "påse":
            if botsvar == "sten":
                await ctx.send('Du vann! \nJag valde sten')
                await streak.addStreak(ctx.author)
            if botsvar =='sax':
                await ctx.send('Jag vann! \nJag valde sax')
                await streak.resetStreak(ctx.author)
            if botsvar =='påse':
                await ctx.send('Lika! \nJag valde påse')


def setup(client):
    client.add_cog(ssp(client))
