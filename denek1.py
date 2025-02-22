import discord
import random
import os
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True
miimler = ["mem1","mem2","mem3"]
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
    print(os.listdir('images'))
    for command in bot.commands:
        print(f"  • {command.name}")
#Hello
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
#Heh bomber
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
#Denek adı
@bot.command()
async def ismin_ne(ctx):
    await ctx.send("Denek 1!")
#Kim ne zaman girdi?
@bot.command()
async def joined(ctx, member: discord.Member):
    """Hoşgeldin!"""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def mem(ctx):
    miim = random.choice(miimler)
    await ctx.send(file=discord.File(f'images/{miim}.png'))

def imgflip_miim():
    url = 'https://api.imgflip.com/get_memes'
    res = requests.get(url)
    data = res.json()

    if data.get("success"):  # API'nin başarılı olup olmadığını kontrol et
        memes = data.get("data", {}).get("memes", [])  # Memeleri al
        if memes:
            random_meme = random.choice(memes)  # Rastgele bir meme seç
            return random_meme.get("name", "Bilinmeyen Meme"), random_meme.get("url", None)

    return None, None  # Eğer hata varsa boş döndür

@bot.command()
async def global_meme(ctx):
    """Rastgele bir meme gönderir"""
    meme_name, meme_url = imgflip_miim()
    if meme_url:
        embed = discord.Embed(title=meme_name, color=discord.Color.blue())  
        embed.set_image(url=meme_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Meme bulunamadı. 😢")

# Reddit Miimleri
def humor_but_dark():
    url = "https://www.reddit.com/r/shitposting/top.json?limit=50"
    headers = {"User-Agent": "Denek1Bot/1.0"}  

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()  # HTTP hatalarını yakalar
        data = res.json()

        posts = data.get("data", {}).get("children", [])
        if not posts:
            print("Reddit API'den gönderi alınamadı.")
            return None, None

        random_post = random.choice(posts)  # Doğrudan rastgele bir gönderi al
        return random_post["data"]["title"], random_post["data"]["url"]

    except requests.exceptions.RequestException as e:
        print(f"Reddit API isteğinde hata oluştu: {e}")
        return None, None

@bot.command()
async def brainrot_miim(ctx):
    """Rastgele bir brainrot miim gönderir"""
    meme_title, meme_url = humor_but_dark()  # Burada fonksiyon çağrılmalı

    if meme_url:
        embed = discord.Embed(title=meme_title, color=discord.Color.purple())
        embed.set_image(url=meme_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Burası boş gözüküyor :(")


bot.run("Bakmasana :(")
