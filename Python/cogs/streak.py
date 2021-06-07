import discord
import json
from discord.ext import commands
from discord.ext.commands.converter import MessageConverter 

class streak(commands.Cog):
    def __init__(self, client): 
        self.client = client

    def loadStreak(self): #öppnar filen
        with open("./json/streak.json", "r") as f:
            data = json.load(f)
        return data

    def saveStreak(self, data): #lägger in streak json filen
        with open("./json/streak.json", "w") as f:
            json.dump(data, f, sort_keys=True, indent=2)

    def getStreak(self, member, data=None): #om du inte finns läggs du till i json filen, om du finns kollar den din streak
        if data is None: 
            data = self.loadStreak()
        try:
            memberStreak = data[str(member.id)]
        except:
            if member.bot:
                memberStreak = 0
            else:
                memberStreak = 0
            data[str(member.id)] = memberStreak
            self.saveStreak(data)
        finally:
            return memberStreak

    async def addStreak(self, member): 
        data = self.loadStreak() 
        streak = self.getStreak(member, data=data)
        data[str(member.id)] = int(streak) + 1
        try:
            self.saveStreak(data)
        except:
            raise Exception()

    async def resetStreak(self, member):
        data = self.loadStreak() 
        bal = self.getStreak(member, data=data)
        data[str(member.id)] = 0
        try:
            self.saveStreak(data)
        except:
            raise Exception()

    @commands.command(name="streak", aliases=["s"], help= "Se din streak") #Skriver ut din streak
    async def streak(self, ctx):
        bal = self.getStreak(ctx.author) 
        message = f"<@{ctx.author.id}> Din streak är: {bal}\n"
        if ctx.message.mentions:
            for member in ctx.message.mentions:
                if member == ctx.author: continue
                bal = self.getStreak(member) 
                message = f"{member.name} streak är: {bal}\n"
        await ctx.send(message)

    @commands.command(name="streakall", aliases=["strall"], help= "Ser allas streak") #Skriver ut allas streak
    async def streakall(self, ctx):
        file = json.load(open("./json/streak.json"))
        msg = ""
        for shits in file.items():
            userr = str(f"{shits[0]}")
            user2 = await self.client.fetch_user(userr)
            msg +=  str(user2) + ":   " + f"{shits[1]}\n"
        await ctx.send("Allas streak:\n" + msg)

def setup(client):
    client.add_cog(streak(client))