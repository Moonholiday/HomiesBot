import discord
import os
import requests
import json
from server import keep_alive

client = discord.Client()

def get_quote():
  res = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(res.text)
  quote = json_data[0]['q'] + ' -' + json_data[0]['a']
  return quote

@client.event
async def on_ready():
  print('Connected as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$quote'):
    quote = get_quote()
    await message.channel.send(quote) 

keep_alive()

client.run(os.getenv('TOKEN'))