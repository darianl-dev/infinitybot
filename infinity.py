import discord
import youtube_dl
from discord.ext import commands
from discord.ext.commands import Bot
import random
import asyncio
import os
import pickle
from itertools import cycle

TOKEN = 'NTA4MTI1ODEyMDU5Mjc1Mjkz.Dr6tHg.W50_mUUX2AEx0PjfW5eOQebSVz0'

client = commands.Bot(command_prefix = 'i.')
client.remove_command('help')

players = {}
queues = {}

def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='i.help'))
    print('Logged in as: ')
    print(client.user.name)

@client.event
async def on_member_join(member):
    print("The user, " + member.name + " has joined the server!")
    await client.send_message(member, "Hello and welcome, to the server {0}.".format(member.name))

    role = discord.utils.get(member.server.roles, name='Newbie')
    await client.add_roles(member, role)


@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@client.command(pass_context=True)
async def queue(ctx, url):
    server = ctx.message.server 
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))

    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
    await client.say('Video has been successfully queued :thumbsup:') 

@client.command()
async def team():
    test = discord.Embed(
        title = 'Infinity Team',
        colour = discord.Colour.orange()
    )

    test.set_thumbnail(url='https://gluonhq.com/wp-content/uploads/2015/05/amber_devices_2-300x300.png')
    test.add_field(name='ViPz#6284', value='ViPz is the sole creator of Infinity, and also made the website, for the InfinityBot.')
    test.add_field(name='seeobombers#8390', value='Seeo has helped mantain and host the bot, and he has also been very helpful for coming up with some, creative and amazing ideas.')

    await client.say(embed=test)

@client.command()
async def ping():
    await client.say("Pong! :ping_pong:")

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

@client.command(pass_context=True)
async def help(ctx):

    author = ctx.message.author
    noti = ctx.message.channel


    embed = discord.Embed(
        title = "Infinity's General Purpose and Music Commands",
        colour = discord.Colour.orange()
    )

    embed.add_field(name='i.team', value="Shows the team, and creators of Infinity Bot.", inline=False)
    embed.add_field(name='i.flipcoin', value="Randomly flips a coin.", inline=False)
    embed.add_field(name='i.echo', value="Prints out text, that you've specified.", inline=False)
    embed.add_field(name='i.ping', value="Pings you back, with the word pong.", inline=False)
    embed.add_field(name='i.square', value="Squares a number, that you've specified.", inline=False)
    embed.add_field(name='i.8ball', value="After the prefix, ask a question, and it'll randomise a answer.", inline=False)
    embed.add_field(name='i.join', value="Puts the bot, into the same voice channel as you.", inline=False)
    embed.add_field(name='i.leave', value="Kicks the bot, out of your voice channel.", inline=False)
    embed.add_field(name='i.play', value="Plays music, that you've specified. (YouTube Only)", inline=False)
    embed.add_field(name='i.pause', value="Pauses the music, you've specified.", inline=False)
    embed.add_field(name='i.resume', value="Resumes the music, you've specified.", inline=False)
    embed.add_field(name='i.stop', value="Stops the music, you've specified.", inline=False)
    embed.add_field(name='i.queue', value="Queues music, that you've specified.", inline=False)
    await client.send_message(noti, "Check your DM's :bell:")

    await client.send_message(author, embed=embed)

@client.command()
async def square(number):
    squared_value = int(number) + int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

@client.command(name='8ball')
async def eight_ball():
    possible_responses = [
        "That is a complete no.", 
        "No, not really.", 
        "I can't tell.",
        "Most likely.", 
        "Of course.",

    ]

    await client.say(random.choice(possible_responses))

client.run(TOKEN)