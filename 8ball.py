#Imports 
from main import random
from main import client 
import discord

#Cf Command
@client.command(aliases=['cf', 'coin','toss']) 
async def coinflip(ctx): 
  cfresponses = [ "Heads", "Tails"]
  await ctx.send(f'{random.choice(cfresponses)}') 


#Cf Command
@client.command(aliases=['8ball', 'predict','fortune']) 
async def ball(ctx): 
  cfresponses = [ "● It is certain", "● It is decidedly so.", "● Without a doubt.", "● Yes definitely.", "● You may rely on it.", "● As I see it, yes.", "● Most likely.", "● Outlook good.", "● Yes.", "● Signs point to yes.", "● Reply hazy, try again.", "● Ask again later.", "● Better not tell you now.", "● Cannot predict now.", "● Concentrate and ask again.", "● Don't count on it.", "● My reply is no.", "● My sources say no.", "● Outlook not so good.", "● Very doubtful."]
  await ctx.send(f'{random.choice(cfresponses)}') 


