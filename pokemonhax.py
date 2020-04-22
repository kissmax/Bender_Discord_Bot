import discord
import pokemonSearch as ps
import time
import random

secretFile = open("Secret.txt","r")
TOKEN = secretFile.read().strip()

client = discord.Client()
dm_list = []
help_cmd = '\n b!online to check bot status \n b!mode (dm,channel,silent) to change how I give hints \n b!dm to be added to the dm hints list \n b!remove to removed from the hints mailer'
global mode
mode = 'channel'

@client.event
async def on_message(message):
    global mode
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('b!help'):
        msg = '{0.author.mention} I slid in those dms with a list of my commands'.format(message)
        await client.send_message(message.channel, msg)
        msg = help_cmd
        await client.send_message(message.author, msg)
        return

    if message.content.startswith('b!remove'):
        if message.author in dm_list:
            msg = '{0.author.mention} Sad to see you go NOT'.format(message)
            dm_list.remove(message.author)
            await client.send_message(message.channel, msg)
            return
        if message.author not in dm_list:
            msg = '{0.author.mention} I dont even dm you'.format(message)
            await client.send_message(message.channel, msg)
            return

    if message.content.startswith('b!setting'):
        msg = 'I am in ' + mode +' mode'.format(message)
        await client.send_message(message.channel, msg)
        return

    if message.content.startswith('b!mode dm'):
        mode = 'dm'
        msg = 'SHHHH pokemon hints are now secret. use !dm to be added to the list'.format(message)
        await client.send_message(message.channel, msg)
        return

    if message.content.startswith('b!mode silent'):
        mode = 'silent'
        msg = 'I wont give any hints now :('.format(message)
        await client.send_message(message.channel, msg)
        return

    if message.content.startswith('b!mode channel'):
        mode = 'channel'
        msg = 'OOOH boi, everyone gets to see my hints'.format(message)
        await client.send_message(message.channel, msg)
        return

    if message.content.startswith('b!dm'):
        if message.author not in dm_list:
            dm_list.append(message.author)
            msg = '{0.author.mention} added to the dm list'.format(message)
            await client.send_message(message.channel, msg)
            return
        if message.author in dm_list:
            msg = '{0.author.mention} you are already on the list, message !remove to be taken off the list'.format(message)
            await client.send_message(message.channel, msg)
            return

    if message.content.startswith('b!online'):
        msg = 'I am still working!'.format(message)
        await client.send_message(message.channel, msg)
        return

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
