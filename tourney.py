import discord
import asyncio
from discord.utils import get
from discord.ext import commands




client = commands.Bot(command_prefix="?")




@client.event
async def on_ready():
    print('We have logged in as {0.user.id}'.format(client))


@client.command()
async def start(ctx, roleid: int):
    guild = ctx.message.guild
    channelid = client.get_channel(ctx.message.channel.id)
    await ctx.send("Type the event name in 10 secs")
    
    
    def check(m):
        return m.author.id in [458223030947282955, 612530423188291615]

    msg1 = await client.wait_for('message', check=check)
    input1 = msg1.content
    category = await guild.create_category(input1)
    await ctx.send("Creating tournament realated channels"+'\n'+"Type confirm to proceed")

    overwrites = {
    guild.default_role: discord.PermissionOverwrite(send_messages=False, read_messages=True, read_message_history=True),
    guild.get_member(612530423188291615): discord.PermissionOverwrite(read_messages=True, send_messages=True, read_message_history=True, attach_files=True),
    guild.get_role(roleid): discord.PermissionOverwrite(read_messages=True, send_messages=True, read_message_history=True),
}
    overwrites1 = {
    guild.default_role: discord.PermissionOverwrite(send_messages=True, read_messages=True, read_message_history=True, attach_files=True),
    guild.get_member(612530423188291615): discord.PermissionOverwrite(read_messages=True, send_messages=True, attach_files=True, read_message_history=True),
    guild.get_role(roleid): discord.PermissionOverwrite(read_messages=True, send_messages=True, attach_files=True, read_message_history=True),
}

    msg2 = await client.wait_for('message', check= check)
    input2 = msg2.content
    if input2 == "confirm":
        text = await ctx.send("configuring channels")
        id = text.id
        await guild.create_text_channel('📣︱announcements', overwrites = overwrites ,category = category, position = 0)
        await asyncio.sleep(1)
        await guild.create_text_channel('📝︱registration-process', overwrites = overwrites ,category = category, positon = 1)
        await asyncio.sleep(1)
        await guild.create_text_channel('📝︱results', overwrites = overwrites ,category = category, position = 3)
        await asyncio.sleep(1)
        await guild.create_text_channel('⏲︱schedule', overwrites = overwrites ,category = category, position = 4)
        await asyncio.sleep(1)
        await guild.create_text_channel('🔴︱stream-links', overwrites = overwrites ,category = category, position = 5)
        await asyncio.sleep(1)
        await guild.create_text_channel('✅︱confirmed-teams', overwrites = overwrites ,category = category, positon = 6)
        await asyncio.sleep(1)
        await guild.create_text_channel('❌︱non-confirmed-teams', overwrites = overwrites ,category = category, position = 7)
        await asyncio.sleep(1)
        await guild.create_text_channel('❓︱queries', overwrites = overwrites1 ,category = category, position = 8)
        await asyncio.sleep(1)
        await guild.create_text_channel('💬︱general-chat', overwrites = overwrites1 ,category = category, position = 9)
        await asyncio.sleep(1)
        await guild.create_text_channel('backend', overwrites = overwrites ,category = category, position = 10)
        await asyncio.sleep(1)

        editmsg = await channelid.fetch_message(id)
        await editmsg.edit(content = "Configured")
        await ctx.send(" Do you want me to post over rules??"+'\n'+" reply with yes or no in lowercase")

        msg3 = await client.wait_for('message', check= check)
        input3 = msg3.content
        if input3 == "yes":
            
            rules = await guild.create_text_channel('📜︱rules', overwrites = overwrites ,category = category, position = 2)
            rulesid = rules.id
            rulessend = client.get_channel(rulesid)
            await rulessend.send(""" __***Participation Rules:***__
> 1) A Team must contain 4 Players and team can have 2 substitute players.
> 2) These 4 to 6 players are only allowed to play throughout tournament.
> 3) Any  Clan or Sponsored  org Line up  can register multiple line ups but only one line up Can go into the finals if multiple line up selected.
> 4) If multiple line up selected from same clan or Org then you can have a Single combined line up in Finals.
> 5) Contact Tournament Administration if you didn’t get rule 4 and 5.
> 6) Registration will end on 24th August.
> 7) Tournament will be in three stages- Qualifiers, Eliminators and Finals. 
> 8) In case of Point tie, Team with Highest Kills will move Forward.
> 9) Please Check Points distribution for in details knowledge of point system in the tournament.


__***Game Rules:***__
> 1) Only Tanks are Banned.
> 2) All other vehicles, Weapons and Classes are allowed For this Tournament.



__***Place Point System:***__
> 1st - 15
> 2nd - 12
> 3rd - 10
> 4th - 9
> 5th - 8
> 6th - 7
> 7th - 6
> 8th - 5
> 9th - 4
> 10th - 3.5
> 11th - 3
> 12th - 2.4
> 13th - 2
> 14th - 1.25
> 15th - 1
> 16th - 0.30


> Also Remember that each kills carry 1 points, So Total Points = Place Points + Kill Points

> Note: This Point System will be followed in the Backend though in GFX and in-announcement points will be rounded off that means anything above or equals to 0.5 is rounded of to +1 while anything below 0.5 turns down to 0. """)
            
            await ctx.send("rules posted !!")



        if input3 == "no":
            rules1 = await guild.create_text_channel('📜︱rules', overwrites = overwrites ,category = category, position = 2)
            print(rules1.id)
            await ctx.send("Finished!!")


            
        





client.run("NzUyNzg5NTM2NTg0NzYxMzQ0.X1cv4w.fSxapIvdZ3f19VrfI7yyXAU_KY4")










