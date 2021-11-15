import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()



from transformers import pipeline
generator = pipeline('text-generation', model='gpt2-medium')




@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    str2 = message.content
    blah = str(str2)
    if blah.startswith('!'):
        #print(blah)
        inputstr = blah[1:]
        inputstr = inputstr[0].upper() + inputstr[1:]
        inputstrbool = True
        if inputstr.endswith(".") or inputstr.endswith("!") or inputstr.endswith("?"):
            inputstrbool = False
   
        if inputstrbool:
            inputstr = inputstr + "."
        print(inputstr)
        #print(inputstr)
        inputstr2 = f"My name is Bob. My job is to reply to messages. I get a message that says \"{inputstr}\" I write back \""
        num = len(inputstr2)
        text = generator(inputstr2, do_sample=True, max_length=50)
        text1 = str(text[0])
        text2 = text1[:-2]
        text3 = text2[20:]
        text4 = text3[num:]
        thing = "\""
        text5 = text4.split(thing, 1)[0]
        text6 = str(text5)
        text7 = text6[0].upper() + text6[1:]
        await message.channel.send(text7)



client.run(TOKEN)# bot.py