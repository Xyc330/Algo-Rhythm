import discord
import os
import random
import json

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    game = discord.Game("$")
    await client.change_presence(status=discord.Status.idle, activity=game)
    print('SYS | I\'m in')



async def send_dm(id, msg):
    user = await client.fetch_user(id)
    await user.send(msg)


# async def bg():
#     await client.wait_until_ready()
#     msg = ''
#     channel = client.get_channel(901277480898412555)  # replace with channel_id
#     while not client.is_closed():
#         msg = input()
#         await channel.send(msg)
#         await asyncio.sleep(1.5)  # task runs every 60 seconds


@client.event
async def on_message(message):
    print(f"{message.author.name}: {message.content}")
    if message.author == client.user:
        return

    if message.content.startswith('$ping'):
        await message.channel.send('PoNg!')
    elif message.content.startswith('$bing'):
        await message.channel.send('chilling')

    if "allez les bleu" in message.content.lower() or "la coupe" in message.content.lower():
        dms = ["I wish you step on lego in the middle of the night", "I hope your pillow is hot on both sides",
               "I wish you stub your toe on concrete", "You are a disappointment"]
        rand_dm = random.choice(dms)
        await send_dm(message.author.id, rand_dm)
        print(f"SYS | Dm sent: {rand_dm}")


f = open('secret.json')
TOKEN = json.load(f)['TOKEN']
client.run(TOKEN)
