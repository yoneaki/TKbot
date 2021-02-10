import discord
import asyncio
import time
# from threading import (Event, Thread)
import threading

TOKEN = 'TOKEN'  # TOKENを入力
client = discord.Client()

base_interval = 0
shorter_time = 0
dead_time = 0


@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理


@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    elif message.content.startswith('!settk'):
        # メッセージを空白ごとに要素分けし、base_interval、shorter_time、dead_timeのそれぞれに代入
        msg = message.content
        a = msg.split()
        base_interval = int(a[1])
        shorter_time = int(a[2])
        dead_time = int(a[3])
        # 内容確認用表示
        await message.channel.send('base_interval = %d shorter_time = %d dead_time = %d' % (base_interval, shorter_time, dead_time))
        # スレッド作成&開始
        endtk = threading.Event()
        print('endtkセット')
        th = threading.Thread(target=up_timer, args=(endtk, message))
        th.start()
        print('スレッド開始')
    # スレッド終了処理
    elif message.content.startswith('!endtk'):
        endtk.set()

# カウントアップタイマー処理


async def up_timer(endtk, message):
    i = 0
    while True:
        if i == dead_time:
            await message.channel.send('**%d**' % (i))
        elif i >= shorter_time:
            await message.channel.send('%d' % (i))
        elif i % base_interval == 0:
            await message.channel.send('%d' % (i))
        i += 1
        if endtk.wait(timeout=1):
            await print('イベント発生')
            break
        elif i > dead_time*3:
            break


client.run(TOKEN)
