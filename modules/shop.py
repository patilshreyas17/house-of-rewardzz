import discord
import asyncio
from discord.utils import get
from discord.ext import commands
import fileinput
import sys
import os
import sqlite3


class Shop(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command = True)
    async def shop(self, ctx):
        server = ctx.guild.id
        dbserver = sqlite3.connect(f"{server}.sqlite")
        cursor_server = dbserver.cursor()
        cursor_server.execute(f"SELECT * FROM shop")
        result_server = cursor_server.fetchall()
        print(result_server)
        embed=discord.Embed(title="House of Rewardzz", url="https://www.asianwarhouse.com/", description= "Available items in Shop for now are:- " , color=0x044efb)
        embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        for item in result_server:
            
            item_name = item[1]
            item_price = item[2]
            item_quantity = item[3]
            meathod = item[4]
            embed.add_field(name=item_name, value= f"Price = {item_price} Quantity remianing {item_quantity}\n buy meathod = {meathod}", inline= False)


        await ctx.send(embed=embed)



        

        
        







def setup(client):
	client.add_cog(Shop(client))