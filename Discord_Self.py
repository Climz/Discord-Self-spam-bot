import discord
from discord.ext import commands
from random import choice
from string import ascii_uppercase
import random
from time import sleep

client = commands.Bot(command_prefix='.', self_bot=True)

"""
    -m + сообщение
    -g будут гифки
    -t время до отправки
    -q количество
"""

@client.event
async def on_redy():
    print('log')


@client.command()
async def say(ctx, *, text):
    terminal = text.split()
    print(terminal)
    stroka = ""
    ti = 0
    qu = 0
    if "-q" in terminal:
        flag = terminal.index("-q")
        if terminal[flag + 1] != "-m" and terminal[flag + 1] != "-g" and terminal[flag + 1] != "-t":
            qu = 0
        else:
            qu = 1
    else:
        qu = 0

    g = False

    for i in terminal:
        if i == "-m":
            m = True
            t = False
            q = False
            continue
        elif i == "-g":
            g = True
            continue
        elif i == "-t":
            t = True
            m = False
            q = False
            continue
        elif i == "-q":
            q = True
            t = False
            m = False
            continue

        if m:
            stroka += i + " "
        elif t:
            ti += int(i)
        elif q:
            qu += int(i)

    if ti > 0:
        for i in range(0, ti):
            await ctx.send(embed=discord.Embed(description=str(ti - i)))  # выделленный техт
            if ti - i == 1:
                await ctx.send(embed=discord.Embed(description="Начинаем Вакханалию"))  # выделленный техт
                await ctx.send(embed=discord.Embed().set_image(url="https://i.gifer.com/7RQq.gif"))  # Скинуть gif по url
            sleep(1)

    for i in range(0, qu):
        lines = open('gifer').read().splitlines()
        myline = random.choice(lines)
        if g == True and stroka == "":
            await ctx.send(embed=discord.Embed().set_image(url=myline))  # Скинуть gif по url
        elif g == True and stroka != "":
            await ctx.send(embed=discord.Embed(description=stroka))  # выделленный техт
            await ctx.send(embed=discord.Embed().set_image(url=myline))  # Скинуть gif по url

    await ctx.send(embed=discord.Embed(description="Всё пиздец"))  # выделленный техт
    await ctx.send(file=discord.File('pizdec.gif'))  # Локально скинуть gif
    await ctx.send(file=discord.File('giphy.gif'))  # Локально скинуть gif


client.run("NDEyNjQ2MDExMDk4NDk3MDI0.YAmP7w.33KsMNPYLyQw_5mKozO1Y9aZxuQ", bot=False)
