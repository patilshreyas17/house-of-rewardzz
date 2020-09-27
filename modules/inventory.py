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




class inventory(commands.Cog):
    def __init__(self, client):
        self.client = client




    @commands.command(aliases=['inv'])
    async def inventory(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        dbuserdata = sqlite3.connect("userdata.sqlite")
        cursor_userdata = dbuserdata.cursor()
        cursor_userdata.execute(f"SELECT * FROM bal WHERE id = {member.id}")
        result_userdata = cursor_userdata.fetchone()
        if result_userdata is None:
            await ctx.send(member.name+",  need an account to see your inventory"+'\n'+"Type `?start` to start your account")


        else:
            nitro_count = int(result_userdata[3])
            nitro_classic_count = int(result_userdata[4])
            cp_count = int(result_userdata[5])
            embed=discord.Embed(title="House of Rewardzz", url="https://www.asianwarhouse.com/", description= f"INEVENTORY" , color=0x044efb)
            embed.set_thumbnail(url=f"{member.avatar_url}")
            embed.set_author(name = member.name, icon_url = member.avatar_url)
            embed.add_field(name= "Nitro" , value= f"{nitro_count}", inline= False)
            embed.add_field(name="Nitro classic", value= f"{nitro_classic_count}", inline= False)
            embed.add_field(name= "Cp", value= f"{cp_count}", inline= False)
            await ctx.send(embed= embed)










def setup(client):
	client.add_cog(inventory(client))