    #serverchannel = member.server.welcome_channel
    #msg = "Bye Bye {0}".format(member.mention)


import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from discord.utils import get

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

chat_filter = ["PINEAPPLE", "APPLE", "CHROME"]
bypass_list = []
list_of_messages = []

@client.event
async def on_ready():
    print("Bot is online and connected to Discord!")



@client.event
async def on_message(message):
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('!SAY'):
        if message.author.id == "218895918416658432":
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "Insufficient permissions!")
    if message.content.upper().startswith('!AMIADMIN'):
        if "517064875134943262" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, "You are an admin!")
        else:
            await client.send_message(message.channel, "You are not an admin")
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Hey!** Ne smijes koristiti ovu rijec!")
                except discord.errors.NotFound:
                     return
                    
    if message.author == client.user:
        return
    if message.content.upper().startswith('!ROLE ADMIN'):
        role = get(message.server.roles, id="517064875134943262")
        userID = message.author.id
        if not "343249790047485952" in [role.id for role in message.author.roles]:
            return
        #await client.send_message(message.channel, 'Insufficient permissions <@%s>' % (userID))
        elif "517064875134943262" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, 'You are already an admin <@%s>' % (userID))
        else:
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, 'Admin given to <@%s>' % (userID))
    if message.content.upper().startswith('!POKE'):
        userID = message.author.id
        await client.send_message(userID, 'Hi!')


    #serverchannel = client.get_channel('517111492819156996')
    #msg = "Get the fuck out of {1}, {0}".format(member.mention, member.server.name)
    

    #message.content.upper().startswith('!IMG'):
        #await client.send_file(message.channel, 'meme.png')

            #if "517064875134943262" in [role.id for role in message.author.roles]:
            #await client.send_message(message.channel, 'You are already an admin <@%s>' % (userID))
        #else:
           #return

@client.command(pass_context=True)
async def poke(ctx, message):
    await client.send_message(ctx.message.author, 'boop')



@client.event
async def on_member_remove(member):
    serverchannel = client.get_channel('517111492819156996')
    msg = "Get the fuck out of {1}, {0}".format(member.mention, member.server.name)
    await client.send_message(serverchannel, msg)


@client.event
async def on_member_join(member):
    serverchannel = client.get_channel('517111492819156996')
    msg = "Welcome to {1}, {0}".format(member.mention, member.server.name)
    role = discord.utils.get(member.server.roles, id="517736657022353428")
    await client.send_message(serverchannel, msg)
    await client.add_roles(member, role)


            






client.run("NTE3MDU2ODY0NDg4MzkwNjY2.Dt8r5w.dA5Sh2Cf5vdtD6pVIrPJYm0hyQE")
