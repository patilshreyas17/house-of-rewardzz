import discord
from discord.ext import commands
import os
import sys
import sqlite3
import time
import random
import datetime
import asyncio
import discord
import fileinput


def get_prefix(client, message):
    if isinstance(message.channel, discord.channel.DMChannel):
        return "?"
    else:
        db = sqlite3.connect("setup.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT prefix FROM prefixes WHERE guildid = {message.guild.id}")
        result = cursor.fetchone()
        if result is None:
            return "?"
        elif result is not None:
            return str(result[0])

client = commands.Bot(command_prefix=get_prefix)



def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
@client.event
async def on_connect():

    delay_print("Loading extensions . . .\n")
    time.sleep(0.5)
    client.load_extension("on_boot")
    delay_print('\n We have logged in as {0.user.id}'.format(client))
    time.sleep(0.5)



@client.command()
async def restart(ctx, extension):
    found = False
    if ctx.author.id == 458223030947282955:
        for path, subdirs, files in os.walk("modules"):
            print(subdirs)
            for name in files:
                if name.endswith(".py"):
                    loc = os.path.join(path) + "/" + os.path.join(name)
                    name_ = os.path.join(name)[:-3]
                    path_ = os.path.join(path).replace("/", ".")
                    cog = path_ + "." + name_
                    if name_ == extension:
                        found = True

                        try:
                            client.load_extension(cog)
                            await ctx.send(f"Loaded extension: `{loc}`")
                        except:
                            client.reload_extension(cog)
                            await ctx.send(f"Loaded extension: `{loc}`")
                else:
                    continue

        if found == False:
            await ctx.send("Extension not found.")
    else:
        await ctx.send("its authorized personnel command only, sorry")

@client.command()
async def deactivate(ctx, extension):
    found = False
    if ctx.author.id == 458223030947282955:
        for path, subdirs, files in os.walk("modules"):
            print(subdirs)
            for name in files:
                if name.endswith(".py"):
                    loc = os.path.join(path) + "/" + os.path.join(name)
                    name_ = os.path.join(name)[:-3]
                    path_ = os.path.join(path).replace("/", ".")
                    cog = path_ + "." + name_
                    if name_ == extension:
                        found = True

                        try:
                            client.unload_extension(cog)
                            await ctx.send(f"unLoaded extension: `{loc}`")
                        except:
                            pass
                else:
                    continue

        if found == False:
            await ctx.send("Extension not found.")
    else:
        await ctx.send("its authorized personnel command only, sorry")

@client.command()
async def poweroff(ctx):
    if ctx.message.author.id == 458223030947282955:
        for path, subdirs, files in os.walk("modules"):
            for name in files:
                if name.endswith(".py"):
                    name = os.path.join(name)[:-3]
                    path = os.path.join(path).replace("/",".")
                    cog = path + "." + name
                    try:
                        client.unload_extension(cog)

                    except Exception as e:
                        print(e)

                else:
                    continue
        print(subdirs)
        await ctx.send("AYE AYE CAPTIAN!!")
        channelid = client.get_channel(ctx.message.channel.id)
        msg = await ctx.send("as of now shutting down all the funtions")
        msgid = msg.id
        editmsg = await channelid.fetch_message(msgid)

        await asyncio.sleep(4)
        await editmsg.edit(content = "system shut downed successfully!!! ")

    else:
        await ctx.send("its authorized personnel command only, sorry")

@client.command()
async def poweron(ctx):
    if ctx.message.author.id == 458223030947282955:
        for path, subdirs, files in os.walk("modules"):
            for name in files:
                if name.endswith(".py"):
                    name = os.path.join(name)[:-3]
                    path = os.path.join(path).replace("/",".")
                    cog = path + "." + name
                    try:
                        client.load_extension(cog)

                    except Exception as e:
                        print(e)

                else:
                    continue
        print(subdirs)
        await ctx.send("AYE AYE CAPTIAN!!")
        channelid = client.get_channel(ctx.message.channel.id)
        msg = await ctx.send("as of now booting up all the funtions")
        msgid = msg.id
        editmsg = await channelid.fetch_message(msgid)
        await editmsg.edit(content = "as of now booting up all the funtions......")

        await asyncio.sleep(4)
        await editmsg.edit(content = " SYSTEM booted up all funtions successfully")


    else:
        await ctx.send("its authorized personnel command only, sorry")






client.run("NzUyNzg5NTM2NTg0NzYxMzQ0.X1cv4w.fSxapIvdZ3f19VrfI7yyXAU_KY4")