import os
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']

loop = True
is_running = False
base_interval_stand_by = 0
shorter_time_stand_by = 0
dead_time_stand_by = 0

# タイマーのセット
@bot.command()
async def settk(ctx, *args):
    if ctx.author.bot:
        return
    global base_interval_stand_by, shorter_time_stand_by, dead_time_stand_by
    base_interval_stand_by = int(args[0])
    shorter_time_stand_by = int(args[1])
    dead_time_stand_by = int(args[2])
    # 内容確認用表示
    await ctx.send(f'base_interval = {base_interval_stand_by} shorter_time = {shorter_time_stand_by} dead_time = {dead_time_stand_by}')

# タイマーのスタート
@bot.command()
async def starttk(ctx):
    if ctx.author.bot:
        return
    global loop, base_interval, shorter_time, dead_time, is_running
    base_interval = base_interval_stand_by * 60
    shorter_time = shorter_time_stand_by * 60
    dead_time = dead_time_stand_by * 60
    loop = True
    timer_count = 0
    is_running = True
    while loop:
        if timer_count >= dead_time * 3:
            await ctx.send(f'**{int(timer_count / 60)}**')
            loop = False
            break
        elif timer_count == dead_time:
            await ctx.send(f'**{int(timer_count / 60)}**')
        elif timer_count >= shorter_time and timer_count % 60 == 0:
            await ctx.send(f'{int(timer_count / 60)}')
        elif timer_count == 0:
            await ctx.send('タイマースタート')
        elif timer_count % base_interval == 0:
           await ctx.send(f'{int(timer_count // 60)}')
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
