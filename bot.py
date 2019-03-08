import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welcome to the Anarchy hangout hope you enjoy your stay!')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='Ir1s is the best'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == 'ping':
        await client.send_message(message.channel,'pong')
    if ('nigger') in message.content:
       await client.delete_message(message)
    if ('nigga') in message.content:
       await client.delete_message(message)
    if message.content.startswith('oh holy bot ping me'):
        await client.send_message(message.channel,'you have been pingeed, <@%s>'  %(message.author.id))
    if ('Nigger') in message.content:
       await client.delete_message(message)
    if ('Nigga') in message.content:
       await client.delete_message(message)
    if ('Niggle') in message.content:
       await client.delete_message(message)
    if ('N I G G E R') in message.content:
       await client.delete_message(message)
    if ('N i G g E r') in message.content:
       await client.delete_message(message)
    if ('n I g G e R') in message.content:
       await client.delete_message(message)
    if ('N I G G A') in message.content:
       await client.delete_message(message)
    if ('N i G g A') in message.content:
       await client.delete_message(message)
    if ('n I G g A') in message.content:
       await client.delete_message(message)
    if ('NiGgEr') in message.content:
       await client.delete_message(message)
    if ('nIgGeR') in message.content:
       await client.delete_message(message)
    if message.content.startswith('nigger'):
        await client.send_message(message.channel,'you have been warned, <@%s>'  %(message.author.id))
    if message.content.startswith('nigga'):
        await client.send_message(message.channel,'you have been warned, <@%s>'  %(message.author.id))
    if message.content.startswith('1-10'):
        randomlist = ["1","2","3","4","5","6","7","8","9","10"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('Russian roulette'):
        randomlist = ["live","live","live","die","live","live"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('russian roulette'):
        randomlist = ["live","live","live","die","live","live"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('im gay'):
        await client.send_message(message.channel,'yes everyone knows <@%s> is gay'  %(message.author.id))
    if message.content == 'CAPOW':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/553235931151204355/553339303166476290/Peachy.PNG')
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('heads or tails'):
        randomlist = ["heads","tails"]
        await client.send_message(message.channel,(random.choice(randomlist)))
client.run('NTUzMzIwMDM4MzQ2NTIyNjk3.D2MXGw.-E49S0F2rUR39lBbXqWFUNGFujc')

