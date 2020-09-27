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



    @commands.group(invoke_without_command = True)
    async def use(self, ctx):
        dbuserdata = sqlite3.connect("userdata.sqlite")
        cursor_userdata = dbuserdata.cursor()
        cursor_userdata.execute(f"SELECT * FROM bal WHERE id = {ctx.author.id}")
        result_userdata = cursor_userdata.fetchone()
        if result_userdata is None:
            await ctx.send(ctx.author.mention+", You need an account use or buy an item"+'\n'+"Type `?start` to start your account")

        elif result_userdata is not None:
            server = ctx.guild.id
            dbserver = sqlite3.connect(f"{server}.sqlite")
            cursor_server = dbserver.cursor()
            cursor_server.execute(f"SELECT * FROM shop")
            result_server = cursor_server.fetchall()
            embed=discord.Embed(title="House of Rewardzz", url="https://www.asianwarhouse.com/", description= "Available item's use meathods in Shop for now are:- " , color=0x044efb)
            embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            for item in result_server:
                item_name = item[1]
                meathod = item[5]
                embed.add_field(name=item_name, value= f"Use meathod = {meathod}", inline= False)

            await ctx.send(embed= embed)



    @use.command()
    async def nitro(self, ctx):
        dbuserdata = sqlite3.connect("userdata.sqlite")
        cursor_userdata = dbuserdata.cursor()
        cursor_userdata.execute(f"SELECT * FROM bal WHERE id = {ctx.author.id}")
        result_userdata = cursor_userdata.fetchone()
        print(result_userdata)
        curent_nitro_count = int(result_userdata[3])
        channel = self.client.get_guild(729266685629956098).get_channel(759453993033400350)
        if curent_nitro_count > 0:
            new_nitro_count = curent_nitro_count - 1

            cursor_userdata.execute(f"UPDATE bal SET nitro={new_nitro_count} WHERE id={ctx.author.id}")
            dbuserdata.commit()
            await ctx.send("Successfully used one nitro from your inventry, respective admins will contact you within 24hrs")
            xyz = f"{ctx.author.name}#{ctx.author.discriminator}"
            now = datetime.datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            
            embed=discord.Embed(title="House of Rewardzz", url="https://www.asianwarhouse.com/", description= "Nitro was claimed!!" , color=0x044efb)
            embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            embed.add_field(name= "Name" , value= xyz, inline= False)
            embed.add_field(name= "Claim Time", value= dt_string, inline= True)
            embed.add_field(name="Amount", value= "1", inline= True)
            embed.add_field(name= "Server", value= f"{ctx.message.guild.name}", inline= False)
            embed.add_field(name="Server id", value= f"{ctx.message.guild.id}", inline=False)
            await channel.send(embed= embed)
            

    @use.command()
    async def nitroclassic(self, ctx):
        dbuserdata = sqlite3.connect("userdata.sqlite")
        cursor_userdata = dbuserdata.cursor()
        cursor_userdata.execute(f"SELECT * FROM bal WHERE id = {ctx.author.id}")
        result_userdata = cursor_userdata.fetchone()
        print(result_userdata)
        curent_nitroclassic_count = int(result_userdata[4])
        channel = self.client.get_guild(729266685629956098).get_channel(759454128799219712)
        if curent_nitroclassic_count > 0:
            new_nitroclassic_count = curent_nitroclassic_count - 1

            cursor_userdata.execute(f"UPDATE bal SET nitroclassic={new_nitroclassic_count} WHERE id={ctx.author.id}")
            await ctx.send("Successfully used one nitroclassic from your inventry, respective admins will contact you within 24hrs")
            xyz = f"{ctx.author.name}#{ctx.author.discriminator}"
            now = datetime.datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            
            embed=discord.Embed(title="House of Rewardzz", url="https://www.asianwarhouse.com/", description="Nitro classic was clamied!!" , color=0x044efb)
            embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            embed.add_field(name= "Name" , value= xyz, inline= False)
            embed.add_field(name= "Claim Time", value= dt_string, inline= True)
            embed.add_field(name="Amount", value= "1", inline= True)
            embed.add_field(name= "Server", value= f"{ctx.message.guild.name}", inline= False)
            embed.add_field(name="Server id", value= f"{ctx.message.guild.id}", inline=False)
            await channel.send(embed= embed)
            dbuserdata.commit()
            

    @use.command()
    async def cp(self, ctx, ammount: int):
        dbuserdata = sqlite3.connect("userdata.sqlite")
        cursor_userdata = dbuserdata.cursor()
        cursor_userdata.execute(f"SELECT * FROM bal WHERE id = {ctx.author.id}")
        result_userdata = cursor_userdata.fetchone()
        print(result_userdata)
        curent_cp_count = int(result_userdata[5])
        channel = self.client.get_guild(729266685629956098).get_channel(759454188819841046)
        if ammount > 100:
            new_cp_count = curent_cp_count - ammount
            cursor_userdata.execute(f"UPDATE bal SET cp={new_cp_count} WHERE id={ctx.author.id}")
            await ctx.send("Successfully used "+str(ammount)+" CP from your inventry, respective admins will contact you within 24hrs")
            xyz = f"{ctx.author.name}#{ctx.author.discriminator}"
            now = datetime.datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            
            embed=discord.Embed(title="House of Rewardzz", url="https://www.asianwarhouse.com/", description="CP was claimed!!" , color=0x044efb)
            embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            embed.add_field(name= "Name" , value= xyz, inline= False)
            embed.add_field(name= "Claim Time", value= dt_string, inline= True)
            embed.add_field(name="Amount", value= f"{ammount}", inline= True)
            embed.add_field(name= "Server", value= f"{ctx.message.guild.name}", inline= False)
            embed.add_field(name="Server id", value= f"{ctx.message.guild.id}", inline=False)
            await channel.send(embed= embed)
            dbuserdata.commit()
        else:
            await ctx.send("The minimum use limit of cp is 100 at a time")


    @cp.error
    async def cp_error(self , ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Amount was not specified!!, use `?use` to know how to use your items from inventory")









def setup(client):
	client.add_cog(claim(client))