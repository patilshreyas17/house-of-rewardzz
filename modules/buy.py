import discord , datetime, time
import asyncio
from discord.utils import get
from discord.ext import commands
import fileinput
import sys
import os
import sqlite3
import time


class buy(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.group(invoke_without_command = True)
    async def buy(self, ctx):
        dbuserdata = sqlite3.connect("userdata.sqlite")
        cursor_userdata = dbuserdata.cursor()
        cursor_userdata.execute(f"SELECT * FROM bal where id = {ctx.author.id}")
        result_userdata = cursor_userdata.fetchone()
        if result_userdata is None:
            await ctx.send(ctx.author.mention+", You need an account to buy"+'\n'+"Type `?start` to start your account")

        else:
            await ctx.send("Pls  use `?shop` to know the items available in the server")
            await ctx.send("`?buy <item name>` \nwith out <> to buy an item!! ")


    @buy.command()
    async def nitro(self, ctx, amount: int):

        dbuserdata = sqlite3.connect("userdata.sqlite")
        cursor_userdata = dbuserdata.cursor()
        cursor_userdata.execute(f"SELECT * FROM bal where id = {ctx.author.id}")
        result_userdata = cursor_userdata.fetchone()
        if result_userdata is None:
            await ctx.send(ctx.author.mention+", You need an account to buy "+'\n'+"Type `?start` to start your account")

        else:
            server = ctx.guild.id
            dbserver = sqlite3.connect(f"{server}.sqlite")
            cursor_server = dbserver.cursor()
            cursor_server.execute(f"SELECT * FROM shop where item_name = 'nitro'")
            result_server = cursor_server.fetchone()
            item_price = int(result_server[2])
            item_quantity = int(result_server[3])
            acc_bal = int(result_userdata[1])
            spent_bal = int(result_userdata[2])
            amount_item_price = item_price*amount   
            if item_quantity > amount:
                if acc_bal >= amount_item_price:
                    item_quantity_new = item_quantity - amount
                    spent_bal_new = spent_bal + amount_item_price
                    nitro_old = int(result_userdata[3])
                    nirto_new = nitro_old + amount
                    acc_balafter = acc_bal - amount_item_price
                    cursor_userdata.execute(f"UPDATE bal SET bal={acc_balafter} WHERE id={ctx.author.id}")
                    cursor_userdata.execute(f"UPDATE bal SET nitro={nirto_new} WHERE id={ctx.author.id}")
                    cursor_server.execute(f"UPDATE shop SET quantity={item_quantity_new} WHERE item_name = 'nitro' ")
                    cursor_userdata.execute(f"UPDATE bal SET spent={spent_bal_new} WHERE id={ctx.author.id}")
                    dbserver.commit()
                    dbuserdata.commit()
                    await ctx.send(ctx.author.mention+" ***, SUCCESSFULLY BOUGHT "+str(amount)+" NITRO!!!!***")
                    xyz = f"{ctx.author.name}#{ctx.author.discriminator}"
                    now = datetime.datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    embed=discord.Embed(title="House of Rewardzz", url="https://www.asianwarhouse.com/", description= "Nitro was bought!!" , color=0x044efb)
                    embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
                    embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                    embed.add_field(name= "Name" , value= xyz, inline= False)
                    embed.add_field(name= "Claim Time", value= dt_string, inline= True)
                    embed.add_field(name="Amount", value= f"{amount}", inline= True)
                    dbsetup = sqlite3.connect("setup.sqlite")
                    cursor = dbsetup.cursor()
                    cursor.execute(f"SELECT log_channel FROM prefixes WHERE guildid = {ctx.guild.id}")
                    result = cursor.fetchone()
                    chanid = int(result[0])
                    channel = self.client.get_guild(server).get_channel(chanid)
                    await channel.send(embed= embed)
                    
                else:
                    await ctx.send(ctx.author.mention+" , it seems you are bit low on balance!")

            else:
                await ctx.send("Server ran out of nitros!!!!"+f" amount of nitro available to buy = {item_quantity} for now")
    
    @nitro.error
    async def nitro_error(self , ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Amount was not specified!!, use `?shop` to know how to buy items")
            


    @buy.command()
    async def nitroclassic(self, ctx, amount: int):
        dbuserdata = sqlite3.connect("userdata.sqlite")
        cursor_userdata = dbuserdata.cursor()
        cursor_userdata.execute(f"SELECT * FROM bal where id = {ctx.author.id}")
        result_userdata = cursor_userdata.fetchone()
        if result_userdata is None:
            await ctx.send(ctx.author.mention+", You need an account to buy "+'\n'+"Type `?start` to start your account")

        else:
            server = ctx.guild.id
            dbserver = sqlite3.connect(f"{server}.sqlite")
            cursor_server = dbserver.cursor()
            cursor_server.execute(f"SELECT * FROM shop where item_name = 'nitroclassic'")
            result_server = cursor_server.fetchone()
            item_price = int(result_server[2])
            item_quantity = int(result_server[3])
            acc_bal = int(result_userdata[1])
            spent_bal = int(result_userdata[2])
            amount_item_price = item_price*amount  
            if item_quantity > amount:
                if acc_bal >= amount_item_price:
                    item_quantity_new = item_quantity - amount
                    spent_bal_new = spent_bal + amount_item_price
                    nitro_old_classic = int(result_userdata[3])
                    nirto_classic_new = nitro_old_classic + amount
                    acc_balafter = acc_bal - amount_item_price
                    cursor_userdata.execute(f"UPDATE bal SET bal={acc_balafter} WHERE id={ctx.author.id}")
                    cursor_userdata.execute(f"UPDATE bal SET nitroclassic={nirto_classic_new} WHERE id={ctx.author.id}")
                    cursor_userdata.execute(f"UPDATE bal SET spent={spent_bal_new} WHERE id={ctx.author.id}")
                    cursor_server.execute(f"UPDATE shop SET quantity={item_quantity_new} WHERE item_name = 'nitroclassic' ")
                    dbserver.commit()
                    dbuserdata.commit()
                    await ctx.send(ctx.author.mention+" ***, SUCCESSFULLY BOUGHT "+str(amount)+" NITRO CLASSIC!!!!***")
                    xyz = f"{ctx.author.name}#{ctx.author.discriminator}"
                    now = datetime.datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    embed=discord.Embed(title="House of Rewardzz", url="https://www.asianwarhouse.com/", description= "Nitro classic was bought!!" , color=0x044efb)
                    embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
                    embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                    embed.add_field(name= "Name" , value= xyz, inline= False)
                    embed.add_field(name= "Claim Time", value= dt_string, inline= True)
                    embed.add_field(name="Amount", value= f"{amount}", inline= True)
                    dbsetup = sqlite3.connect("setup.sqlite")
                    cursor = dbsetup.cursor()
                    cursor.execute(f"SELECT log_channel FROM prefixes WHERE guildid = {ctx.guild.id}")
                    result = cursor.fetchone()
                    chanid = int(result[0])
                    channel = self.client.get_guild(server).get_channel(chanid)
                    await channel.send(embed= embed)
                    
                else:
                    await ctx.send(ctx.author.mention+" , it seems you are bit low on balance!")

            else:
                await ctx.send("Server ran out of nitro classics!!!!"+f"amount of Nitroclassicc available buy = {item_quantity} for now")
    
    @nitroclassic.error
    async def nitroclassic_error(self , ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Amount was not specified!!, use `?shop` to know how to buy items")

    @buy.command()
    async def cp(self, ctx, amount: int):
        dbuserdata = sqlite3.connect("userdata.sqlite")
        cursor_userdata = dbuserdata.cursor()
        cursor_userdata.execute(f"SELECT * FROM bal where id = {ctx.author.id}")
        result_userdata = cursor_userdata.fetchone()
        if result_userdata is None:
            await ctx.send(ctx.author.mention+", You need an account to buy "+'\n'+"Type `?start` to start your account")

        else:
            server = ctx.guild.id
            dbserver = sqlite3.connect(f"{server}.sqlite")
            cursor_server = dbserver.cursor()
            cursor_server.execute(f"SELECT * FROM shop where item_name = 'cp'")
            result_server = cursor_server.fetchone()
            item_quantity = int(result_server[3])
            acc_bal = int(result_userdata[1])
            spent_bal = int(result_userdata[2])
            multi_item_price = amount*100  
            if item_quantity >= amount:
                if acc_bal >= multi_item_price:
                    item_quantity_new = item_quantity - amount
                    spent_bal_new = spent_bal + multi_item_price
                    cp_old = int(result_userdata[3])
                    cp_new = cp_old + amount
                    acc_balafter = acc_bal - multi_item_price
                    cursor_userdata.execute(f"UPDATE bal SET bal={acc_balafter} WHERE id={ctx.author.id}")
                    cursor_userdata.execute(f"UPDATE bal SET cp={cp_new} WHERE id={ctx.author.id}")
                    cursor_userdata.execute(f"UPDATE bal SET spent={spent_bal_new} WHERE id={ctx.author.id}")
                    cursor_server.execute(f"UPDATE shop SET quantity={item_quantity_new} WHERE item_name = 'cp' ")
                    dbserver.commit()
                    dbuserdata.commit()
                    await ctx.send(ctx.author.mention+" ***, SUCCESSFULLY BOUGHT "+str(amount)+" CP!!!!***")
                    xyz = f"{ctx.author.name}#{ctx.author.discriminator}"
                    now = datetime.datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    embed=discord.Embed(title="House of Rewardzz", url="https://www.asianwarhouse.com/", description= "CP was bought!!" , color=0x044efb)
                    embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
                    embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                    embed.add_field(name= "Name" , value= xyz, inline= False)
                    embed.add_field(name= "Claim Time", value= dt_string, inline= True)
                    embed.add_field(name="Amount", value= f"{amount}", inline= True)
                    dbsetup = sqlite3.connect("setup.sqlite")
                    cursor = dbsetup.cursor()
                    cursor.execute(f"SELECT log_channel FROM prefixes WHERE guildid = {ctx.guild.id}")
                    result = cursor.fetchone()
                    chanid = int(result[0])
                    channel = self.client.get_guild(server).get_channel(chanid)
                    print(server)
                    print(chanid)
                    await channel.send(embed= embed)
                    
                else:
                    await ctx.send(ctx.author.mention+" , it seems you are bit low on balance!")


            elif amount > item_quantity:
                await ctx.send("The server doesn't have that much cp for the current moment \n for now amount of cp available is = "+str(item_quantity))

            else:
                await ctx.send("Server ran out of CPs!!!!")

    @cp.error
    async def cp_error(self , ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Amount was not specified!!, use `?shop` to know how to buy items")





 

def setup(client):
	client.add_cog(buy(client))