import discord , datetime, time
import asyncio
from discord.utils import get
from discord.ext import commands
import fileinput
import sys
import os
import sqlite3
import time
import random




class join_leave(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        dbsetup = sqlite3.connect("setup.sqlite")
        cursor_setup = dbsetup.cursor()
        cursor_setup.execute(f"SELECT * FROM prefixes WHERE guildid = {guild.id}")
        result_setup = cursor_setup.fetchone()
        if result_setup is None:
            channel = await guild.create_text_channel('reward-logs')
            chanid = channel.id
            sql = """INSERT INTO prefixes(guildid, prefix, log_channel) VALUES(?, ?, ?)"""
            val = (guild.id, "?",chanid  )
            cursor_setup.execute(sql, val)
            dbsetup.commit()
            await channel.send("This will be the channel for my logs, please configure the persmissions accordingly")

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        if channel.name == "reward-logs":
            dbsetup = sqlite3.connect("setup.sqlite")
            cursor_setup = dbsetup.cursor()
            channel = await channel.guild.create_text_channel("reward-logs")
            chanid = channel.id
            cursor_setup.execute(f"UPDATE prefixes SET log_channel={chanid} WHERE guildid = {channel.guild.id}")
            dbsetup.commit()



            await channel.send("reward-log was deleted , so I made it again")
            await channel.send("I will be logging all the commands outputs here , please edit channel permissions to remove everyone from seeing here but make sure u allow dm bot")   







def setup(client):
	client.add_cog(join_leave(client))
