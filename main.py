import discord
import json
from googletrans import Translator

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True

client = discord.Client(intents=intents)


# TRANSLATOR
def translate(text, dest='ru'):
    translator = Translator()
    return translator.translate(text, dest=dest).text


def detectLang(text):
    # known bug
    if text.lower() == 'ik':
        return 'en'
  

    translator = Translator()
    
    detection = translator.detect(text)
    lang = 'en'
    if detection.confidence >= 0.8:
        lang = detection.lang

    return lang


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
    

    
    # TRANSLATION
    if message.content.startswith('$tr'):
        if message.content.startswith('$tr_'):
            try:
                destLang = message.content[4:6]
                
                if destLang == 'zh':
                    destLang = 'zh-CN'  # Default to Simplified chinese
                await message.channel.send(translate(message.content[6:], dest=destLang))
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
