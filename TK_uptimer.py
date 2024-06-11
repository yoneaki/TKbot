import os
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']

loop = True
is_running = False

# タイマーのスタート
@bot.command()
async def starttk(ctx ,*args):
    if ctx.author.bot:
        return
    global loop,is_running
    base_interval_min = int(args[0])
    shorter_time_min = int(args[1])
    dead_time_min = int(args[2])
    base_interval_sec = base_interval_min * 60
    shorter_time_sec = shorter_time_min * 60
    dead_time_sec = dead_time_min * 60
    loop = True
    timer_count = 0
    is_running = True
    await ctx.send(f'base_interval = {base_interval_min} shorter_time = {shorter_time_min} dead_time = {dead_time_min}')
    while loop:
        if timer_count == 0:
            await ctx.send('タイマースタート')
        elif timer_count >= dead_time_sec * 4:
            await ctx.send(f'**{int(timer_count / 60)}**')
            loop = False
            break
        elif timer_count == dead_time_sec:
            await ctx.send(f'**{int(timer_count / 60)}**')
        elif timer_count >= shorter_time_sec and timer_count % 60 == 0:
            await ctx.send(f'{int(timer_count / 60)}')
        elif timer_count % base_interval_sec == 0:
           await ctx.send(f'{int(timer_count / 60)}')
        await asyncio.sleep(1)
        timer_count += 1
    is_running = False
    await ctx.send('タイマーストップ')

# タイマーのストップ
@bot.command()
async def endtk(ctx):
    if ctx.author.bot:
        return
    global loop
    loop = False

# タイマーの生存確認
@bot.command()
async def isrunning(ctx):
    if ctx.author.bot:
        return
    await ctx.send('I\'m ready!')

bot.run(token)
