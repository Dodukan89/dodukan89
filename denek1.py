import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def ismin_ne(ctx):
    await ctx.send("Denek 1!")

@bot.command()
async def joined(ctx, member: discord.Member):
    """Hoşgeldin!"""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

bot.run("O sihirli token burdaydı :(")
