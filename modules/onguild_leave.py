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




class join_leave(commands.Cog):
    def __init__(self, client):
        self.client = client











def setup(client):
	client.add_cog(join_leave(client))