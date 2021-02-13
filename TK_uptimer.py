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
    base_interval = base_interval_stand_by
    shorter_time = shorter_time_stand_by
    dead_time = dead_time_stand_by
    loop = True
    timer_count = 0
    is_running = True
    await ctx.send('タイマースタート')
    while loop:
        timer_count += 1
        if timer_count >= dead_time * 3:
            await ctx.send(f'**{timer_count}**')
            loop = False
            break
        elif timer_count == dead_time:
            await ctx.send(f'**{timer_count}**')
        elif timer_count >= shorter_time:
            await ctx.send(f'{timer_count}')
        elif timer_count % base_interval == 0:
           await ctx.send(f'{timer_count}')
        await asyncio.sleep(1)
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
    global is_running
    if is_running:
        await ctx.send('timer is running!')
    else:
        await ctx.send('timer is not running!')

bot.run(token)
