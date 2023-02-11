import discord
# import re # built-in regex
from wiki import *
from translate import *
from ice_breaker import *
from encryption import *
from parse_int import parse_int
from brainfuck import stringPrinter, evaluate

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


async def send_msg(channel, msg):
    parts = []
    if len(msg) > 2000:  # Split the messages into parts and send
        while len(msg) > 2000:
            parts.append(msg[:2000])
            msg = msg[2000:]
        parts.append(msg)

        for part in parts:
            await channel.send(part)

    else:
        await channel.send(msg)


def isHehe(msg):
    msg = msg.lower()
    for i in range(len(msg)):
        if i % 2 == 0 and msg[i] != "h":
            return False
        if i % 2 == 1 and msg[i] != "e":
            return False

    return len(msg) >= 4 and len(msg) % 2 == 0


async def check_encryption(message):
    # ENCRYPTION
    if message.content.startswith('$set_key'):
        key = message.content[9:]
        set_key(key)
        return "Key set!"
    elif message.content.startswith('$enc'):
        msg = message.content[5:]
        return encrypt(msg, get_key())
    elif message.content.startswith('$dec'):
        msg = message.content[5:]
        print(msg)
        return decrypt(msg, get_key())

    return ""


@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot:
        return

    print(f"{message.author.name}: {message.content}")

    enc = await check_encryption(message)
    if enc != "":
        await message.delete()
        await send_msg(message.channel, enc)
        return

    elif message.content.startswith('$bing'):
        await send_msg(message.channel, 'chilling')

    # WIKI WHO IS
    elif message.content.startswith('$whois'):
        await message.channel.send("Researching...")
        summary = who_is(message.content[6:])
        await send_msg(message.channel, summary)

    

    # HOT TAKE
    elif message.content == "$hottake":
        await send_msg(message.channel, get_random_hot_take())
    elif message.content == "$icebreaker":
        await send_msg(message.channel, get_random_ice_breaker())


    # PARSEINT
    elif message.content.startswith("$parseint"):
        await send_msg(message.channel, parse_int(message.content[10:]))


    # Hehehe
    elif message.content.lower().startswith("he"):
        if isHehe(message.content):
            await send_msg(message.channel, message.content + "he")

    # Brainfuck
    elif message.content.lower().startswith("$bf"):
        code = stringPrinter(message.content[4:])
        await send_msg(message.channel, code)
    elif message.content.lower().startswith("$cp_bf"):
        output = evaluate(message.content[7:])
        await send_msg(message.channel, output)
        
        
        
        
    # TRANSLATION
    elif message.content.startswith('$tr'):
        if message.content.startswith('$tr_'):
            try:
                dest_lang = message.content[4:6]

                if dest_lang == 'zh':
                    dest_lang = 'zh-CN'  # Default to Simplified chinese
                await send_msg(message.channel, translate(message.content[6:], dest=dest_lang))
            except ValueError:
                await send_msg(message.channel, "Invalid translation request")

        else:
            await send_msg(message.channel, translate(message.content[3:]))
    elif detectLang(message.content) not in ['en', 'fr']:
        translation = translate(message.content, dest='en')
        print(f"SYS | Translated from {detectLang(message.content)}")
        await send_msg(message.channel, f'Translation: {translation}')





if __name__ == '__main__':
    f = open('/Users/yichengxia/Desktop/Programs/Python/Algo-rhythm/secret.json')
    TOKEN = json.load(f)['TOKEN']
    client.run(TOKEN)
