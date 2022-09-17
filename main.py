
import torch
import discord
from discord.ext import commands
import nest_asyncio
import json
import os
import re
import random
import keep_alive
import gif
import godtone
import draw
import rapping
import torchvision.transforms as transforms
from torch import nn
from PIL import Image
import requests
import typing

nest_asyncio.apply()
import numpy as np
intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)





@client.command(aliases=["675"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def 安安(ctx):
    await ctx.send(f" {ctx.author.name}")

@client.command(aliases=["675尻尻"])
async def 尻尻(ctx):
    await ctx.send(" ╭[◕ ͜🔴◕]ﻝﮞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ✊̶͞ ̶͞ ̶D💦")  

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def 指令(ctx):
    await ctx.send(
        '!675, !675gif, !godtonegif, !偷 @成員, !丟炸彈'    )
  
@client.command(aliases=["大鼻子說唱","說唱"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def rap(ctx):
      embed = discord.Embed(title=f"大鼻子說唱", description=f'{random.choice(rapping.lyrics)}')
    #embed.set_image(url=random.choice(draw.url))
      await ctx.send(embed=embed)


@client.command(aliases=["675畫畫","draw"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def 畫畫(ctx):

    embed = discord.Embed(title=f"大鼻子賭場畫的畫", description=f"")
    embed.set_image(url=random.choice(draw.url))

    await ctx.send(embed=embed)  

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def 丟炸彈(ctx):
    user = ctx.author
    target = random.choice(ctx.guild.members)

    await ctx.send(
        f"{ctx.author} 丟出了炸彈💣! 💥炸到了 {target.mention}!")

@client.command()
@commands.cooldown(1, 3, commands.BucketType.channel)
async def 偷(ctx, member: discord.Member):
    user = ctx.author
    roll = random.randrange(100)
    earnings = random.randrange(1, 100)+ 2**roll
    if roll %2 == 0:
      url = "https://media.discordapp.net/attachments/960384629204987915/989795234332442654/Webp.net-gifmaker_12.gif "
      embed = discord.Embed(title=f"{ctx.author}想偷 {member}🤚...，偷錢成功! 從{member}身上偷到{earnings}元!",    description=f"")

      embed.set_image(url=url)

      await ctx.send(embed=embed)  
    else:
     url = "https://media.discordapp.net/attachments/960384629204987915/989793746126274570/Webp.net-gifmaker_12.gif "
     embed = discord.Embed(title=f"{ctx.author}想偷 {member}🤚...，可是被{member}打而被反拿{earnings}元!" , description=f"")
     embed.set_image(url=url)

     await ctx.send(embed=embed)  

@client.command()
@commands.cooldown(1, 3, commands.BucketType.channel)
async def 猜拳(ctx, fist):
    user = ctx.author
    result = random.randrange(1, 5)
    if fist == "剪刀" and result == 1:  
      url = "https://media.discordapp.net/attachments/987690983493869578/1018735687257817088/pss9.gif "
      embed = discord.Embed(title=f"{ctx.author}出了剪刀✌️，機器人出了剪刀✌️，平手╭◕ ͟🔴◕╮！",    description=f"")
      embed.set_image(url=url)
      await ctx.send(embed=embed)  
    if fist == "剪刀" and result == 2:  
      url = "https://media.discordapp.net/attachments/987690983493869578/1018735687773736961/pss11.gif "
      embed = discord.Embed(title=f"{ctx.author}出了剪刀✌️，機器人出了石頭✊，機器人贏了╭[◕ ͜🔴◕]👍🏼！",    description=f"")
      embed.set_image(url=url)
      await ctx.send(embed=embed)  
    if fist == "剪刀" and result == 3:  
      url = "https://media.discordapp.net/attachments/987690983493869578/1018735687530463242/pss10.gif "
      embed = discord.Embed(title=f"{ctx.author}出了剪刀✌️，機器人出了布🖐，{ctx.author.name}贏了༼ ͝💧 ͟🔴 ͝💧 ༽！",    description=f"")
      embed.set_image(url=url)
      await ctx.send(embed=embed)  
    if fist == "剪刀" and result == 4:  
      url = "https://media.discordapp.net/attachments/987690983493869578/1018735688016998400/pss12.gif "
      embed = discord.Embed(title=f"{ctx.author}出了剪刀✌️，直接把機器人剪掉✂️💥ﻝﮞ ̶̶͞͞ ̶͞ ̶D，{ctx.author.name}贏了༼ ͝💧 ͟🔴 ͝💧 ༽！",    description=f"")
      embed.set_image(url=url)
      await ctx.send(embed=embed) 
    if fist == "石頭" and result == 1:  
      url = "https://media.discordapp.net/attachments/987690983493869578/1018735686553174046/pss6.gif "
      embed = discord.Embed(title=f"{ctx.author}出了石頭✊，機器人出了剪刀✌️，{ctx.author.name}贏了༼ ͝💧 ͟🔴 ͝💧 ༽！",    description=f"")
      embed.set_image(url=url)
      await ctx.send(embed=embed)  
    if fist == "石頭" and result == 2:  
      url = "https://media.discordapp.net/attachments/987690983493869578/1018735686301536346/pss5.gif "
      embed = discord.Embed(title=f"{ctx.author}出了石頭✊，機器人出了石頭✊，平手╭◕ ͟🔴◕╮！",    description=f"")
      embed.set_image(url=url)
      await ctx.send(embed=embed)  
    if fist == "石頭" and result == 3:  
      url = "https://media.discordapp.net/attachments/987690983493869578/1018735686767099944/pss7.gif"
      embed = discord.Embed(title=f"{ctx.author}出了石頭✊，機器人出了布🖐，機器人贏了╭[◕ ͜🔴◕]👍🏼！",    description=f"")
      embed.set_image(url=url)
      await ctx.send(embed=embed)  
    if fist == "石頭" and result == 4:  
      url = "https://media.discordapp.net/attachments/987690983493869578/1018735686985207828/pss8.gif"
      embed = discord.Embed(title=f"{ctx.author}出了石頭✊，直接揍機器人一拳✊💥，{ctx.author.name}贏了༼ ͝💧 ͟🔴 ͝💧 ༽！",    description=f"")
      embed.set_image(url=url)
      await ctx.send(embed=embed) 
    if fist == "布" and result == 1:  
      url = "https://media.discordapp.net/attachments/987690983493869578/1018533967676321872/pss3.gif "
      embed = discord.Embed(title=f"{ctx.author}出了布🖐，機器人出了剪刀✌️，機器人贏了╭[◕ ͜🔴◕]👍🏼！",    description=f"")
      embed.set_image(url=url)
      await ctx.send(embed=embed)  
    if fist == "布" and result == 2:  
      url = "https://media.discordapp.net/attachments/987690983493869578/1018533967437242408/pss2.gif "
      embed = discord.Embed(title=f"{ctx.author}出了布🖐，機器人出了石頭✊，{ctx.author.name}贏了༼ ͝💧 ͟🔴 ͝💧 ༽！",    description=f"")
      embed.set_image(url=url)
      await ctx.send(embed=embed)  
    if fist == "布" and result == 3:  
      url = "https://media.discordapp.net/attachments/987690983493869578/1018533967076544573/pss1.gif"
      embed = discord.Embed(title=f"{ctx.author}出了布🖐，機器人出了布🖐，平手╭◕ ͟🔴◕╮！",    description=f"")
      embed.set_image(url=url)
      await ctx.send(embed=embed)  
    if fist == "布" and result == 4:  
      url = "https://media.discordapp.net/attachments/987690983493869578/1018533967999275188/pss4.gif"
      embed = discord.Embed(title=f"{ctx.author}出了布🖐，直接打了機器人一巴掌🖐💥，{ctx.author.name}贏了༼ ͝💧 ͟🔴 ͝💧 ༽！",    description=f"")
      embed.set_image(url=url)
      await ctx.send(embed=embed) 






  
@client.command(aliases=["675gif"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def 大鼻子gif(ctx):

    embed = discord.Embed(title=f"╭[◕ ͜🔴◕]👍🏼", description=f"")
    embed.set_image(url=random.choice(gif.url))

    await ctx.send(embed=embed)

@client.command(aliases=["godtonegif"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def 統神gif(ctx):

    embed = discord.Embed(title=f"╭[◕ ͜🔴◕]👍🏼", description=f"")
    embed.set_image(url=random.choice(godtone.url))

    await ctx.send(embed=embed)  

class ConvAutoencoder(nn.Module):
    def __init__(self):
        super(ConvAutoencoder, self).__init__()

        self.cnn_layers = nn.Sequential(
            nn.Conv2d(3, 16, 3, 2, 1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2, 0),

            nn.Conv2d(16, 32, 3, 2, 1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2, 0),

        )
        self.fc_layers = nn.Sequential(
            nn.Linear(2048, 256),
            nn.ReLU(),
            nn.Linear(256, 64),
            nn.ReLU(),            
            nn.Linear(64, 1)
        )

    def forward(self, x):
        x = self.cnn_layers(x)
        x = x.flatten(1)
        x = self.fc_layers(x)
        return x


device = "cuda" if torch.cuda.is_available() else "cpu"
model = ConvAutoencoder().cpu()
checkpoint_path = 'sexmodel_{}.pt'
model = torch.load(checkpoint_path,map_location=torch.device('cpu')).cpu()

train_tfm = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Lambda(lambda x: x[:3,:,:]),
    transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5)),

])


@client.command(aliases=["射精評分"])
@commands.cooldown(1, 3, commands.BucketType.channel)
async def ca(ctx, image: typing.Union[discord.Member, str] = None):
        if not image:
            if len(ctx.message.attachments) >= 1:
                image = ctx.message.attachments[0].url
                
            else:
                image = str(ctx.author.avatar_url_as(format='png'))
        response = requests.get(url=image, stream=True).raw
        imag = Image.open(response).convert('RGBA')
        
        A = train_tfm(imag).to(device)
        A = torch.unsqueeze(A,0)
        output = model(A).cpu()
        output = np.int(output+9)
        if  output > 100:
            output == 100
        if  output >= 90:
            six ="我已經沒了!l╭[◕ ͜🔴◕] ﻝﮞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶✊̶͞ ̶͞ ̶D💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦"
        elif 90> output >= 80:
             six ="我的床濕了!l╭[◕ ͜🔴◕] ﻝﮞ ̶͞ ̶͞ ̶͞ ̶✊̶͞ ̶͞ ̶D💦💦💦💦💦💦"
        elif    80> output >= 70:
            six ="我大爆射了!l╭[◕ ͜🔴◕] ﻝﮞ ̶͞ ̶✊̶͞ ̶͞ ̶D💦💦💦"
        elif    70> output >= 50  :
            six ="我射了!l╭[◕ ͜🔴◕] ﻝﮞ ̶͞✊̶͞ ̶͞ ̶D💦"
        elif    50> output >= 40  :
            six = "我快射了!l╭[◕ ͜🔴◕]ﻝﮞ ̶͞ ̶͞D"
        elif    40> output >= 30  :    
            six = "我沒射!l╭◕ ͟🔴◕╮ﻝﮞD"
        elif    30> output >= 20  :    
            six = "我沒射!╭◕ ͟🔴◕╮"
        elif    20> output :   
            output = output- random.randrange(10)
            six = "我褲子穿上了!╭◕ ͟🔴◕╮👖"
        e= discord.Embed(title=f"這張圖的射精評分為.... {output}分!" ,description=f"{six}")
        #e.set_image(url="response")
       # await ctx.send(embed=e)
        await ctx.reply(embed=e, mention_author=True)
        #await ctx.send(file=discord.File('test.png'))
        #await ctx.send(imag) 

keep_alive.keep_alive()
try:
    client.run(token)
except:
    os.system("kill 1")

client.run(token)