import discord
import random
import os
from discord.ext import commands
from discord import app_commands
import requests
import json
intents = discord.Intents.default()
intents.message_content = True
miimler = ["mem1","mem2","mem3"]
bot = commands.Bot(command_prefix='$', intents=intents)

CEVRE_PUANI_DEPOSU = "cevre_puanlari.json"
cevrelevel = 1
cevre_level_gereksinimi = 500
gunun_sorusu_odulu = 100

def load_json(file_name, default_data={}):
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            json.dump(default_data, f, indent=4)
    with open(file_name, "r") as f:
        return json.load(f)

def save_json(file_name, data):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)


cevre_puani_skorlari = load_json(CEVRE_PUANI_DEPOSU)



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

    if data.get("success"):  
        memes = data.get("data", {}).get("memes", []) 
        if memes:
            random_meme = random.choice(memes) 
            return random_meme.get("name", "Bilinmeyen Meme"), random_meme.get("url", None)

    return None, None 

@bot.command()
async def global_miim(ctx):
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

@bot.command()
async def gununsorusu(ctx):
    global cevrelevel
    global cevre_level_gereksinimi
    global gunun_sorusu_odulu
    sorular = {
            "Küresel ısınmanın en büyük nedeni nedir?": "Aşırı karbon salınımı",
            "Geri dönüşüm neden önemlidir?" : "Doğal kaynakları korumak için",
            "Hangi enerji kaynakları çevre dostudur?" : "Rüzgar ve güneş enerjisi",
            "Hangi enerji kaynakları çevre dostu değildir?" : "Kömür ve petrol",
            "Hangi enerji kaynakları yenilenebilir değildir?" : "Kömür ve petrol",
            "Hangi enerji kaynakları yenilenebilirdir?" : "Rüzgar ve güneş enerjisi",
            "Karbon ayak izi nasıl azaltılabilir?" : "Enerji tasarrufu yaparak",
            "Sıfır atık nedir?" : "Atıkları en aza indirerek çevreyi korumak"
    }      
    soru, dogru_cevap = random.choice(list(sorular.items()))
    await ctx.send(soru)
    await ctx.send("Doğru cevabı yazınız:")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel  

    try:
        msg = await bot.wait_for("message", check=check, timeout=30)
        
        if msg.content.lower() == dogru_cevap.lower():
            await ctx.send("Doğru cevap! ✅")
            await ctx.send("Bugünün sorusundan 100 xp kazandın!")
            user_id = str(ctx.author.id)
            cevre_puani_skorlari[user_id] = cevre_puani_skorlari.get(user_id, 0) + gunun_sorusu_odulu
            save_json(CEVRE_PUANI_DEPOSU, cevre_puani_skorlari)
            if cevre_puani_skorlari[user_id] >= cevre_level_gereksinimi:
                cevrelevel += 1
                await ctx.send(f"Tebrikler! Seviye atladın! Yeni seviyen: {cevrelevel}")
                cevre_level_gereksinimi *= 1.5
                gunun_sorusu_odulu *= 1.4
        else:
            await ctx.send(f"Yanlış cevap!")

    except:
        await ctx.send("Zaman doldu! ⏳")


bot.run("Burda eksik bişeyler var ama bendede yok :(")
