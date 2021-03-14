import discord
import os
import requests
import json
from server import uptime

client = discord.Client()

#quote request and return
def get_quote():
  res = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(res.text)
  quote = json_data[0]['q'] + ' -' + json_data[0]['a']
  return quote

#advice request and return
def get_advice():
  res = requests.get('	https://api.adviceslip.com/advice')
  json_data = json.loads(res.text)
  advice = json_data['slip']['advice']
  return advice

#joke request and return
def get_joke():
  res = requests.get('https://v2.jokeapi.dev/joke/Any?type=twopart')
  json_data = json.loads(res.text)
  setup = json_data['setup']
  delivery = json_data['delivery']
  joke = setup +' \n'+ delivery
  return joke

#shell indication of bot being online
@client.event
async def on_ready():
  print('Connected as {0.user}'.format(client))

#client event to trigger bot
@client.event
async def on_message(message):
  #if the message was from bot itself it doesnt activate
  if message.author == client.user:
    return

  #if the message is $quote runs fn quote()
  if message.content.startswith('$quote'):
    quote = get_quote()
    await message.channel.send(quote)

  #if the message is $advice runs fn advice()
  if message.content.startswith('$advice'):
    advice = get_advice()
    await message.channel.send(advice)
  
  #if the message is $joke runs fn joke()
  if message.content.startswith('$joke'):
    joke = get_joke()
    await message.channel.send(joke)

#keeping the bot online
uptime()

client.run(os.getenv('TOKEN'))