# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
	# Wenn die Verbindung zum Server steht
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):

 	# Damit der Bot nicht auf Sich selbst reagiert!
 	if message.author == client.user:
    	return
    
    # Wenn jemand LOL in den Chat schreibt
    if 'lol' in message.content.lower():
        await message.channel.send('lol, HA HA HA! :D ')

client.run(TOKEN)