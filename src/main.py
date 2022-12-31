import discord
import json
from wiki import *
from translate import *


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


async def send_dm(author_id, msg):
    user = await client.fetch_user(author_id)
    await user.send(msg)



@client.event
async def on_message(message):
    print(f"{message.author.name}: {message.content}")
    if message.author == client.user or message.author.id in [704802632660943089, 298822483060981760]:
        return

    if message.content.startswith('$ping'):
        await message.channel.send('PoNg!')
    elif message.content.startswith('$bing'):
        await message.channel.send('chilling')

    # WIKI WHO IS
    if message.content.startswith('$whois'):
        await message.channel.send("Researching...")
        summary = who_is(message.content[6:])
        summary = (summary[:1998] + '..') if len(summary) > 1998 else summary  # Max character limit of 2000
        await message.channel.send(summary)

    # TRANSLATION
    elif message.content.startswith('$tr'):
        if message.content.startswith('$tr_'):
            try:
                dest_lang = message.content[4:6]
                
                if dest_lang == 'zh':
                    dest_lang = 'zh-CN'  # Default to Simplified chinese
                await message.channel.send(translate(message.content[6:], dest=dest_lang))
            except ValueError:
                await message.channel.send("Invalid translation request")
                
        else:
            await message.channel.send(translate(message.content[3:]))
    elif detectLang(message.content) not in ['en', 'fr']:
        translation = translate(message.content, dest='en')
        print(f"SYS | Translated from {detectLang(message.content)}")
        await message.channel.send(f'Translation: {translation}')
        


if __name__ == '__main__':
    f = open('secret.json')
    TOKEN = json.load(f)['TOKEN']
    client.run(TOKEN)