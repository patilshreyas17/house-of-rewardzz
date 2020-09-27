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




class claim(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def claim(self, ctx, code):
        await ctx.message.delete()
        server = ctx.guild.id
        dbuserdata = sqlite3.connect("userdata.sqlite")
        cursor_userdata = dbuserdata.cursor()
        cursor_userdata.execute(f"SELECT * FROM bal where id = {ctx.author.id}")
        result_userdata = cursor_userdata.fetchone()
        if result_userdata is None:
            await ctx.send(ctx.author.mention+" , To redeem/claim you need to have an account"+'\n'+"Type `?start` to make an account!!")

        else:
            acc_bal = int(result_userdata[1])
            dbserver = sqlite3.connect(f"{server}.sqlite")
            cursor_server = dbserver.cursor()
            cursor_server.execute(f"SELECT * FROM codes where token = {code}")
            result_server = cursor_server.fetchone()
            if result_server is None:
               await ctx.send(ctx.author.mention+", The which you are trying to redeem doesn't exist!")
        
            else:
                token_value = int(result_server[1])
                token_status = int(result_server[2])
                if token_status == 0:
                    new_bal = acc_bal + token_value
                    sqluserdata = """UPDATE bal SET bal=? WHERE id=?"""
                    valuserdata = (new_bal, ctx.author.id)
                    cursor_userdata.execute(sqluserdata, valuserdata)
                    dbuserdata.commit()
                    xyz = f"{ctx.author.name}#{ctx.author.discriminator}"
                    cursor_server.execute(f"UPDATE codes SET status=1 WHERE token= {code}")
                    sqlserver = """UPDATE codes SET claimed_by=? WHERE token=?"""
                    valserver = (xyz, code)
                    cursor_server.execute(sqlserver, valserver)
                    now = datetime.datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    cursor_server.execute(f"UPDATE codes SET claimed_by_id={ctx.author.id} WHERE token= {code}")
                    sql1 = """UPDATE codes SET claimed_at=? WHERE token=?"""
                    val1 = (dt_string, code)
                    cursor_server.execute(sql1, val1)
                
                    dbserver.commit()
                    await ctx.send(ctx.author.mention+" , Successfully claimed the code!!, type `?bal` to check !!")


                else:
                    await ctx.send("The code ur tryin to redeem is already used!!")







def setup(client):
	client.add_cog(claim(client))