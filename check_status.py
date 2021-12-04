from main import discord
from discord.ext import commands
from main import client

class Check(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Check Status Loaded Succesfully')

@client.command()
async def ping(ctx):
    await ctx.send('Pong :ping_pong:! {0}'.format(round(client.latency, 1)))
    await ctx.message.delete()

    



def setup(client):
    client.add_cog(Check(client))