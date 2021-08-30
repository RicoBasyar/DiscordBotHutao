import discord

def Max_Attack_Bonus(base):
  x = float(base)
  x = x*4
  return x

def Guide_To_Afterlife(max):
  x = float(max)
  x = x / 0.0626
  return x

token = 'NTMyNDU0MjgwOTgwODU2ODMz.XDWcsQ.qgDpflApwjfLem2Y612nj3nbjGw'
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('+base'):
        userInput = message.content[5:]
        MAB = Max_Attack_Bonus(userInput)
        GTA = Guide_To_Afterlife(Max_Attack_Bonus(userInput))
        await message.channel.send("``` Base attack ="+str(userInput)+
                                   "\n Maximal Bonus Attack = "+str(MAB)+
                                   "\n HP For Maximal Bonus (Elemental Skill Lvl 10) = "+str(GTA)+
                                   "```")

client.run(token)