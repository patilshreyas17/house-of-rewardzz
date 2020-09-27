from discord.ext import commands
import sqlite3



class misc(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_permissions(administrator = True)
	async def setprefix(self, ctx, prefix = None):
		db = sqlite3.connect("setup.sqlite")
		cursor = db.cursor()
		cursor.execute(f"SELECT prefix FROM prefixes WHERE guildid = {ctx.guild.id}")
		result = cursor.fetchone()
		if prefix is None:
			if result is None:
				await ctx.send(f'{ctx.author.mention} The current prefix for this server is `?`')
			else:
				await ctx.send(f'{ctx.author.mention} The current prefix for this server is `{result[1]}`.')
		elif prefix is not None:
			if result is None:
				sql = """INSERT INTO prefixes(prefix,guildid) VALUES(?,?)"""
			elif result is not None:
				sql = """UPDATE prefixes SET prefix=? WHERE guildid=?"""
			
			val = (prefix, ctx.guild.id)
			cursor.execute(sql, val)
			db.commit()

			await ctx.send(f'{ctx.author.mention} The prefix has been successfully set to `{prefix}`')

def setup(client):
    client.add_cog(misc(client))