import configparser
import os
import threading

import discord
import asyncio

from flask import g

configuration = configparser.ConfigParser()
configuration.read("config.ini")

TOKEN = configuration["notifs"]["discordtoken"]

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

        channelid = int(configuration["notifs"]["discordchannelid"])
        guildid = int(configuration["notifs"]["discordguildid"])
        self.guild = self.get_guild(guildid)
        self.channel = self.guild.get_channel(channelid)
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

    async def sendTestMessage(self, message : str):
        for channel in self.get_all_channels():
            print(channel)

        self.channel.send("hello")


def getDiscordChatBot():
    client = getattr(g, '_discord', None)
    if client == None:
        startDiscordBot()
        client = getattr(g, '_discord', None)
    return client


def startDiscordBot():
    client = g._discord = MyClient()
    loop = asyncio.get_event_loop()
    loop.create_task(client.start(TOKEN))
    clientThread = g._discordThread = threading.Thread(target=loop.run_forever)
    clientThread.start()