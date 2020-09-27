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

class check(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def check(self, ctx, code):
        await ctx.message.delete()
        id = [458223030947282955, 612530423188291615]
        if ctx.author.id in id:
            channelid = self.client.get_channel(ctx.message.channel.id)
            msg = await ctx.send(":mag_right: searching thorugh database")
            msgid = msg.id 
            editmsg = await channelid.fetch_message(msgid)
            serverid = ctx.guild.id 
            dbserver = sqlite3.connect(f"{serverid}.sqlite")
            cursor_server = dbserver.cursor()   
            cursor_server.execute(f"SELECT * FROM codes where token = {code}")
            result_server = cursor_server.fetchone()
            if result_server is None:
                await ctx.author.send("The code `"+str(code)+"` doesn't exist")
                await editmsg.edit(content ="The results for the search are sent to your DM, have a look at it!!")

        
            else:
                token_status = int(result_server[2])
                token_value = int(result_server[1])
                token_claimed_by = result_server[3]
                claimed_at = result_server[5]
                if token_status == 0:
                    await ctx.author.send(str(code)+", this code is fresh code of vaule equal to "+str(token_value)+'\n'+"Be carefull while typing it somewhere!!")
         
                elif token_claimed_by != 0:
                    await ctx.author.send(str(code)+", This is a claimed code.The person who claimed it was "+token_claimed_by+" for value of "+str(token_value)+"\n claimed at time = "+str(claimed_at))

    
                await editmsg.edit(content ="The results for the search are sent to your DM, have a look at it!!")
        else:
            await ctx.send("its authorized personnel command only, sorry")



    @commands.command()
    async def gcheck(self, ctx, code, serverid):
        await ctx.message.delete()
        id = [458223030947282955, 612530423188291615]
        if ctx.author.id in id:
            channelid = self.client.get_channel(ctx.message.channel.id)
            msg = await ctx.send(":mag_right: searching thorugh database")
            msgid = msg.id 
            editmsg = await channelid.fetch_message(msgid)
            serverid = ctx.guild.id 
            dbserver = sqlite3.connect(f"{serverid}.sqlite")
            cursor_server = dbserver.cursor()   
            cursor_server.execute(f"SELECT * FROM codes where token = {code}")
            result_server = cursor_server.fetchone()
            if result_server is None:
                await ctx.author.send("The code `"+str(code)+"` doesn't exist")
        
            else:
                token_status = int(result_server[2])
                token_value = int(result_server[1])
                token_claimed_by = result_server[3]
                claimed_at = result_server[5]
                if token_status == 0:
                    await ctx.author.send(str(code)+", this code is fresh code of vaule equal to"+str(token_value)+'\n'+"Be carefull while typing it somewhere!!")
        
                elif token_claimed_by != 0:
                    await ctx.author.send(str(code)+", This is a claimed code.The person who claimed it was "+token_claimed_by+" for value of "+str(token_value)+"\n claimed at time = "+str(claimed_at))

    
                await editmsg.edit(content ="The results for the search are sent to your DM, have a look at it!!")

        else:
            await ctx.send("its authorized personnel command only, sorry")




def setup(client):
	client.add_cog(check(client))