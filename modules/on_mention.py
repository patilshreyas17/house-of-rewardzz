from discord.ext import commands
import sqlite3

class onMessage(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_message(self, message):
		if self.client.user in message.mentions:
			db = sqlite3.connect("setup.sqlite")
			cursor = db.cursor()
			cursor.execute(f"SELECT prefix FROM prefixes WHERE guildid = {message.guild.id}")
			result = cursor.fetchone()
			if result is None:
				await message.channel.send(f'{message.author.mention} The current prefix for this server is `.`.')
			else:
				await message.channel.send(f'{message.author.mention} The current prefix for this server is `{result[0]}`.')

def setup(client):
	client.add_cog(onMessage(client))