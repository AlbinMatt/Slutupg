import discord
import youtube_dl
import os
import time
from discord import FFmpegPCMAudio
from discord.ext import commands



ydl_opts = { #Konveterar en youtube videos ljud till en mp3 fill
                "format": "bestaudio/best",
                "download_archive:": "./låtar/",
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }],
            }

class musik(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, help= "Spela upp en låt")
    async def play(self, ctx, url:str): #Kopiera in en URL länk
        voice_channel = ctx.author.voice.channel
        try: #ansluter till en röstkanal sen laddar ner videon och sen spelar
            voice = await voice_channel.connect()
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, "song.mp3")
            source = FFmpegPCMAudio("song.mp3")
            player = voice.play(source)
            player = player

        except:
            try: #om botten redan ansluten spelas ljudet upp  och raderar filen
                os.remove("song.mp3")
                time.sleep(1)
                voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, "song.mp3")
                source = FFmpegPCMAudio("song.mp3")
                player = voice.play(source)
            except: #spelar bara upp ljudet
                voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, "song.mp3")
                source = FFmpegPCMAudio("song.mp3")
        


    @commands.command(pass_context=True, help= "Återupta musiken")
    async def resume(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("Musiken spelas nu igen!")

    @commands.command(pass_context=True, help= "Pausar musiken")
    async def pause(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("Musiken är nu på puasad skriv, resume för att spela igen!")


    @commands.command(help= "koppla ifrån boten")
    async def kys(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild = ctx.guild)
        try:
            await voice.disconnect()
            await ctx.send("Hejdå :(")
            time.sleep(1)
            os.remove("song.mp3")
        except: #om botten inte är i en röstkanal
            await ctx.send("Jag är redan död :(")
          

def setup(client):
    client.add_cog(musik(client))
