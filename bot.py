import os

import discord
from dotenv import load_dotenv
from search_api import google_search


load_dotenv()
TOKEN = open("token.txt").read()
GOOGLE = "!google"
RECENT = "!recent"
DB_PATH = "local_db.log"
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hi':
        await message.channel.send("Hey")

    if message.content.startswith(GOOGLE):
        keyword = message.content.split(GOOGLE, 1)[-1].strip()
        if len(message.content.split(GOOGLE, 1)) > 1:
            print("searching google for keyword {}".format(keyword))
            with open(DB_PATH, 'a') as f:
                f.write(keyword)
                f.write("\n")
            result_urls = google_search(keyword)
            await message.channel.send("\n".join(result_urls))

    if message.content.startswith(RECENT):
        keyword = message.content.split(RECENT, -1)[-1].strip()
        if len(message.content.split(RECENT, 1)) > 1:
            print("searching local db for keyword {}".format(keyword))
            search_history = open(DB_PATH, 'r').read()
            result_search = filter(lambda x: keyword in x, search_history.split("\n"))
            await message.channel.send("\n".join(result_search))

client.run(TOKEN)
