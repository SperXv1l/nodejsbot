import discord
import asyncio

client = discord.Client()
game = discord.Game("WATCH ROKA MP")

@client.event
async def on_ready():
    print('Bot Online')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "안녕":
        await message.channel.send("맹호 접속이나 쳐 해 !")

client.run("Nzg0NzYxOTgzODkxMDEzNjQy.X8uAjQ.ljj3akhqljB-4IzplPNLoSbkpJQ")