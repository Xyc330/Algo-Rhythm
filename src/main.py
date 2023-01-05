import discord
import json
from wiki import *
from translate import *
from ice_breaker import *
from encryption import *
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



async def check_encryption(message):
          
    # ENCRYPTION
    if message.content.startswith('$set_key'):
        key = message.content[9:]
        set_key(key)
        
        await message.channel.send("Key set!")
    
    
    return ""
        
        
    

@client.event
async def on_message(message):

    if message.author == client.user or message.author.bot:
        return
    
    print(f"{message.author.name}: {message.content}")

    enc = await check_encryption(message)
    if enc != "":
        await message.channel.send(enc)


    if message.content.startswith('$ping'):
        await message.channel.send('PoNg!')
    elif message.content.startswith('$bing'):
        await message.channel.send('chilling')

    # WIKI WHO IS
    elif message.content.startswith('$whois'):
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


    # HOT TAKE
    elif message.content == "$hottake":
        await message.channel.send(get_random_hot_take())
    elif message.content == "$icebreaker":
        await message.channel.send(get_random_ice_breaker())
        

        


if __name__ == '__main__':
    f = open('/Users/yichengxia/Desktop/Programs/Python/Algo-rhythm/secret.json')
    TOKEN = json.load(f)['TOKEN']
    client.run(TOKEN)
