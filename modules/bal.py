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




class bal(commands.Cog):
    def __init__(self, client):
        self.client = client




    @commands.command()
    async def bal(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        db = sqlite3.connect("userdata.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM bal where id = {member.id}")
        result = cursor.fetchone()
        if result is None:
            await ctx.send("You need an account to check your balance"+'\n'+"Type `?start` to start your account")
 
        else:
            acc_bal = result[1]
            spent_acc_bal = result[2]
            embed=discord.Embed(title="House of Rewardzz", url="https://www.asianwarhouse.com/", description= f"{member.name}" , color=0x044efb)
            embed.set_thumbnail(url=f"{member.avatar_url}")
            embed.add_field(name="Balance", value= acc_bal, inline= False)
            embed.add_field(name="Spent till now", value= spent_acc_bal, inline= False)
            await ctx.send(embed = embed)











def setup(client):
	client.add_cog(bal(client))