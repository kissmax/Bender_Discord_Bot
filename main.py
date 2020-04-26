import discord
import pokemonSearch as ps
import time
import random
import json

def getToken():
    settingsFile = open("settings.json","r")
    settings = json.loads(settingsFile.read())
    settingsFile.close()
    return settings["token"]

def checkDM(user):
    settingsFile = open("settings.json","r")
    settings = json.loads(settingsFile.read())
    settingsFile.close()
    list = settings["dmList"]
    if user.id in list:
        return True
    else:
        return False

def addDM(user):
    settingsFile = open("settings.json","r")
    settings = json.loads(settingsFile.read())
    settingsFile.close()
    settings["dmList"].append(user.id)
    settingsFile = open("settings.json","w")
    json.dump(settings, settingsFile)
    settingsFile.close()

def getDMList():
    settingsFile = open("settings.json","r")
    settings = json.loads(settingsFile.read())
    settingsFile.close()
    return settings["dmList"]

def removeDM(user):
    settingsFile = open("settings.json","r")
    settings = json.loads(settingsFile.read())
    settingsFile.close()
    settings["dmList"].remove(user.id)
    settingsFile = open("settings.json","w")
    json.dump(settings, settingsFile)
    settingsFile.close()

def checkMode():
    settingsFile = open("settings.json","r")
    settings = json.loads(settingsFile.read())
    settingsFile.close()
    return settings["mode"]

def changeMode(mode):
    settingsFile = open("settings.json","r")
    settings = json.loads(settingsFile.read())
    settingsFile.close()
    settings["mode"] = mode
    settingsFile = open("settings.json","w")
    json.dump(settings, settingsFile)
    settingsFile.close()


TOKEN = getToken()
client = discord.Client()
help_cmd = '\n b!online to check bot status \n b!mode (dm,channel,silent) to change how I give hints \n b!dm to be added to the dm hints list \n b!remove to removed from the hints mailer'

@client.event
async def on_message(message):
    global mode
    if message.author == client.user:
        return

    if message.content.startswith('b!help'):
        msg = '{0.author.mention} I slid in those dms with a list of my commands'.format(message)
        await client.send_message(message.channel, msg)
        msg = help_cmd
        await client.send_message(message.author, msg)
        return

    if message.content.startswith('b!remove'):
        if checkDM(message.author):
            msg = '{0.author.mention} Sad to see you go NOT'.format(message)
            removeDM(message.author)
            await client.send_message(message.channel, msg)
            return
        else:
            msg = '{0.author.mention} I dont even dm you'.format(message)
            await client.send_message(message.channel, msg)
            return

    if message.content.startswith('b!setting'):
        mode = checkMode()
        msg = 'I am in ' + mode +' mode'.format(message)
        await client.send_message(message.channel, msg)
        return

    if message.content.startswith('b!mode dm'):
        changeMode('dm')
        msg = 'SHHHH pokemon hints are now secret. use b!dm to be added to the list'.format(message)
        await client.send_message(message.channel, msg)
        return

    if message.content.startswith('b!mode silent'):
        changeMode('silent')
        msg = 'I wont give any hints now :('.format(message)
        await client.send_message(message.channel, msg)
        return

    if message.content.startswith('b!mode channel'):
        changeMode('channel')
        msg = 'OOOH boi, everyone gets to see my hints'.format(message)
        await client.send_message(message.channel, msg)
        return

    if message.content.startswith('b!dm'):
        if checkDM(message.author) == False:
            addDM(message.author)
            msg = '{0.author.mention} added to the dm list'.format(message)
            await client.send_message(message.channel, msg)
            return
        else:
            msg = '{0.author.mention} you are already on the list, message !remove to be taken off the list'.format(message)
            await client.send_message(message.channel, msg)
            return

    if message.content.startswith('b!online'):
        msg = 'I am still working!'.format(message)
        await client.send_message(message.channel, msg)
        return

    if (message.author.id == '365975655608745985'):
        mode = checkMode()
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
                        dmList = getDMList()
                        for i in dmList:
                            user = await client.get_user_info(int(i))
                            await client.send_message(user,msg)
                        return
            except IndexError:
                return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
