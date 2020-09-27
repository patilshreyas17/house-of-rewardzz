import discord , datetime, time
import asyncio
from discord.utils import get
from discord.ext import commands
import fileinput
import sys
import os
import sqlite3
import time


class admin(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.users = [458223030947282955]




    @commands.group(invoke_without_command = False)
    async def set(self, ctx):
        if ctx.message.author.id in self.users:
            embed=discord.Embed(title="House of Rewardzz", url= "https://www.asianwarhouse.com/", description= "Have look and apply them in server" , color=0x044efb)
            embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            embed.add_field(name="bal",value= "?set bal <id> <new bal>", inline=False)
            embed.add_field(name="nitro",value= "?set nitro <id> <new nitro>", inline=False)
            embed.add_field(name="nitroclassic",value= "?set nitroclassic <id> <new nitroclassic>", inline=False)
            embed.add_field(name="cp",value= "?set cp <id> <new cp>", inline=False)
            embed.add_field(name="servernitro",value= "?set servernitro <server id> <new nitro>", inline=False)     
            embed.add_field(name="servernitroclassic",value= "?set servernitroclassic <server id> <new nitroclassic>", inline=False)    
            embed.add_field(name="servercp",value= "?set servercp <server id> <new cp>", inline=False)    
            await ctx.author.send(embed= embed)
            await ctx.send("pls head over to your dms")

        else:
            await ctx.send("its authorized personnel command only, sorry")













def setup(client):
	client.add_cog(admin(client))