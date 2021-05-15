import discord
import datetime
import asyncio
import time_str

from datetime import datetime
from discord.ext import commands,tasks

intents=discord.Intents.all()
client = commands.Bot(command_prefix="!",intents=intents)
client.launch_time = datetime.utcnow()
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot is online")

@client.command()
async def ping(ctx):
    embed=discord.Embed(title="MDB Ping",description=f"My ping is {round(client.latency * 1000)}ms ",color=discord.Colour.blurple())
    await ctx.reply(embed=embed)

@client.command()
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    embed=discord.Embed(title="MDB Uptime",description=f"{days}d, {hours}h, {minutes}m, {seconds}s",color=discord.Colour.blurple())
    await ctx.reply(embed=embed)

@client.command()
async def stats(ctx):
    guilds = client.guilds
    members = 0

    for guild in guilds:
        gmembers = guild.members
        num = len(gmembers)
        members += num
        
    delta_uptime = datetime.utcnow() - client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    embed = discord.Embed(title="MDb Stats",description=f"Client Status  :  \n```Servers  ::  {str(len(client.guilds))}\nUsers  ::  {members}\nPing  ::  {round(client.latency * 1000)}ms\nUptime  ::  {days}d, {hours}h, {minutes}m, {seconds}s```",color=discord.Colour.blurple())
    await ctx.send(embed=embed)


@client.command()
async def remindme(ctx,time: time_str.convert,*,message=None):
    if message == None:
        message ="Something"
    emoji = client.get_emoji(842736272631660598)
    await ctx.reply(f"{emoji} Reminder set ")
    await asyncio.sleep(time.total_seconds())
    mention = f"{ctx.author.mention}"
    embed=discord.Embed(title="Reminder",description=f"{time} ago you asked about to remind you about ``{message}``",color=discord.Colour.blurple())
    await ctx.send(mention,embed=embed)

'''
@client.command()
async def emoji(ctx):
    emoji = client.get_emoji(842736272631660598)
    await ctx.reply(emoji)
'''
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx,member:discord.Member,reason=None):
    if ctx.author == member:
        ur_embed=discord.Embed(title="Error trying to kick",description=f"Unable to kick {member.mention}. Why are you trying to kick yourself?",color=discord.Colour.red())
        await ctx.reply(embed=ur_embed)
        return
    elif member.top_role > ctx.author.top_role:
            role_heirachy = discord.Embed(title="Role Heirachy",description="Error : The person you are trying to kick is higher than you hence cannot be kicked",color=discord.Colour.red())
            await ctx.reply(embed=role_heirachy)
            return
    else:
        try:
            mem_embed=discord.Embed(title="You have been kicked",description=f"You have been kicked from **{ctx.guild.name}** by {ctx.author.mention}. Reason : {reason}",color=discord.Colour.red())
            await member.send(embed=mem_embed)
            await member.kick(reason=reason)
            suc_embed=discord.Embed(title=f"User Kicked",description=f"{member.mention} has been kicked by {ctx.author.mention}. Reason : {reason}",color=discord.Colour.blurple())
            await ctx.send(embed=suc_embed)
        except discord.errors.Forbidden:
            await member.kick(reason=reason)
            suc1_embed=discord.Embed(title=f"User Kicked",description=f"{member.mention} has been kicked by {ctx.author.mention}. Reason : {reason}",color=discord.Colour.blurple())
            await ctx.send(embed=suc1_embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def kick(ctx,member:discord.Member,reason=None):
    if ctx.author == member:
        ur_embed=discord.Embed(title="Error trying to ban",description=f"Unable to ban {member.mention}. Why are you trying to kick yourself?",color=discord.Colour.red())
        await ctx.reply(embed=ur_embed)
        return
    elif member.top_role > ctx.author.top_role:
            role_heirachy = discord.Embed(title="Role Heirachy",description="Error : The person you are trying to ban is higher than you hence cannot be kicked",color=discord.Colour.red())
            await ctx.reply(embed=role_heirachy)
            return
    else:
        try:
            mem_embed=discord.Embed(title="You have been banned",description=f"You have been banned from **{ctx.guild.name}** by {ctx.author.mention}. Reason : {reason}",color=discord.Colour.red())
            await member.send(embed=mem_embed)
            await member.ban(reason=reason)
            suc_embed=discord.Embed(title=f"User banned",description=f"{member.mention} has been banned by {ctx.author.mention}. Reason : {reason}",color=discord.Colour.blurple())
            await ctx.send(embed=suc_embed)
        except discord.errors.Forbidden:
            await member.ban(reason=reason)
            suc1_embed=discord.Embed(title=f"User banned",description=f"{member.mention} has been banned by {ctx.author.mention}. Reason : {reason}",color=discord.Colour.blurple())
            await ctx.send(embed=suc1_embed)
    
client.run("TOKEN_HERE")
