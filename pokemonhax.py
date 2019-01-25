import discord
import pokemonSearch as ps
import time
import random

TOKEN = 'MzM2MDU5NzEzODQ4NDc1NjQ4.DyG8nA.Rn8dxlnDUPSPCPYAtYnnf2qwdDE'

client = discord.Client()
zach = [' you suck', ' has a hot mom', ' Sarah said no, sorry', ' Go home', ' *heavy breathing*', ' Sugar juice?', ' try again later', ' Voted worst white kid in this Discord 3 years running', ' has sweaty hands', ' "I hit him for 5 shots!!"']
dm_list = []
help_cmd = '\n !online to check bot status \n !mode (dm,channel,silent) to change how I give hints \n !dm to be added to the dm hints list \n !remove to removed from the hints mailer'
global mode
mode = 'channel'

@client.event
async def on_message(message):
    global mode
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        msg = '{0.author.mention} I slid in those dms with a list of my commands'.format(message)
        await client.send_message(message.channel, msg)
        msg = help_cmd
        await client.send_message(message.author, msg)
        return

    if message.content.startswith('!remove'):
        if message.author in dm_list:
            msg = '{0.author.mention} Sad to see you go NOT'.format(message)
            dm_list.remove(message.author)
            await client.send_message(message.channel, msg)
            return
        if message.author not in dm_list:
            msg = '{0.author.mention} I dont even dm you, you dumb as hell'.format(message)
            await client.send_message(message.channel, msg)
            return

    if message.content.startswith('!setting'):
        msg = 'I am in ' + mode +' mode'.format(message)
        await client.send_message(message.channel, msg)
        return

    if message.content.startswith('!mode dm'):
        mode = 'dm'
        msg = 'SHHHH pokemon hints are now secret. use !dm to be added to the list'.format(message)
        await client.send_message(message.channel, msg)
        return

    if message.content.startswith('!mode silent'):
        mode = 'silent'
        msg = 'I wont give any hints now :('.format(message)
        await client.send_message(message.channel, msg)
        return

    if message.content.startswith('!mode channel'):
        mode = 'channel'
        msg = 'OOOH boi, everyone gets to see my hints'.format(message)
        await client.send_message(message.channel, msg)
        return

    if message.content.startswith('!dm'):
        if message.author not in dm_list:
            dm_list.append(message.author)
            msg = '{0.author.mention} added to the dm list'.format(message)
            await client.send_message(message.channel, msg)
            return
        if message.author in dm_list:
            msg = '{0.author.mention} stooopid you are already on the list, message !remove to be taken off the list'.format(message)
            await client.send_message(message.channel, msg)
            return

    if message.content.startswith('!online'):
        msg = 'I am still working!'.format(message)
        await client.send_message(message.channel, msg)
        return

    """if ((message.author.id == '201196011534680064') & (random.randrange(10) == 3)):
        msg = message.author.mention + random.choice(zach)
        await client.send_message(message.channel, msg)
        return"""
    
    if (message.author.id == '365975655608745985'):
        if mode != 'silent':
            try:
                link = dict(message.embeds[0])
                if ('A wild' in link['title']):
                    str_link = link['image']
                    img_link = str_link['url']
                    ans = ps.getPoke(img_link)
                    msg = 'I think that is ' + ans
                    server = message.server
                    if mode == 'channel':
                        await client.send_message(message.channel,msg)
                        return
                    if mode == 'dm':
                        for i in dm_list:
                            await client.send_message(i,msg)
                        return
            except IndexError:
                print("message has no contents")
                return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
