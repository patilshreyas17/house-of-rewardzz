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


class start(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def start(self, ctx):
        db = sqlite3.connect("userdata.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM bal where id = {ctx.author.id}")
        result = cursor.fetchone()
        if result is None:
            sql = """INSERT INTO bal(id, bal, spent, nitro, nitroclassic, cp) VALUES(?, ?, ?, ?, ?, ?)"""
            val = (ctx.author.id, 0, 0, 0, 0, 0)
            cursor.execute(sql, val)
            db.commit()
            await ctx.send(ctx.author.mention+", Your account has been created!!")
        else:
            await ctx.send("You already have an account")
 





def setup(client):
	client.add_cog(start(client))