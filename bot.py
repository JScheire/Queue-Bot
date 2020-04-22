import discord
import random
from discord.ext import commands

key = open('key.txt', 'r')
TOKEN = key.read()

client = commands.Bot(command_prefix = '!')

queue = []

@client.command()
async def party(ctx):

    if not queue:
        await ctx.send('Party is empty!')
    else:
        getqueue = ', '.join(map(str, queue))

        await ctx.send('Party: ' + getqueue)
    

@client.command()
async def add(ctx, player):
    valorant = discord.utils.get(ctx.guild.roles, name='Valorant')
    if(len(queue) < 5):
        if player.lower() == 'me' and ctx.author.name not in queue:
            queue.append(ctx.author.name)
        else:
            queue.append(player)
        
        if ((5 - len(queue) == 1)):
            message = f'{valorant.mention} We need ' + str(5 - len(queue)) + ' more for 5!'
        else: 
            message = 'We need ' + str(5 - len(queue)) + ' more for 5!'

    else:
        message = 'Party is full! Type !clear if you would like to start a new party.'


    
    
    await ctx.send(message)
        

@client.command()
async def remove(ctx, player):
    if player.lower() == 'me':
        queue.remove(ctx.author.name)
        message = f'Successfully removed {ctx.author.name} from the party.'
    else:
        queue.remove(player)
        message = f'Successfully removed {player} from the party.'
    
    await ctx.send(message)

@client.command()
async def clear(ctx):
    global queue
    queue = []

    await ctx.send('Party emptied.')

@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error: Type !help')


client.run(TOKEN)
