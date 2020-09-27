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


class cog_loader(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.load_cogs()

    

    def load_cogs(self):
        def delay_print(s):
            for c in s:
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.1)
        for path, subdirs, files in os.walk("modules"):
            for name in files:
                if name.endswith(".py"):
                    name = os.path.join(name)[:-3]
                    path = os.path.join(path).replace("/", ".")
                    cog = path + "." + name
                    try:
                        self.client.load_extension(cog) 

                        delay_print(cog + "  was loaded!\n")
                        time.sleep(0.5)
                    except Exception as e:
                        print(e)
                else:
                    continue
        delay_print("\nThe bot is ready!\n")
        print(subdirs)

def setup(client):
	client.add_cog(cog_loader(client))