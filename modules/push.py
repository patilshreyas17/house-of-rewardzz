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


class push(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def push(self, ctx, value: int):
        id = [458223030947282955]
        if ctx.author.id in id:
            f = open("pushcodes.txt","r")
            lists = f.readlines()
            f.close()
            count = 0
            for x in lists:
                t = ctx.guild.id
        
                db1 = sqlite3.connect(f"{t}.sqlite")
                cursor = db1.cursor()
                sql = """INSERT INTO codes(token, value, status, claimed_by, claimed_by_id, claimed_at) VALUES(?, ?, ?, ?, ?, ?)"""
                val = (x , value, 0, 0, 0, 0)
                cursor.execute(sql, val)
                db1.commit()
                count += 1
            f = open("pushcodes.txt","w+")
            f.truncate(0)

        
            await ctx.send("Pushed up "+str(count)+" codes of value equal to "+str(value))
        













def setup(client):
	client.add_cog(push(client))