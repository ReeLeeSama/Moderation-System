import discord
import asyncio

from discord.ext import commands

intents=discord.Intents.all()
client = commands.Bot(command_prefix="!",intents=intents)
client.launch_time = datetime.utcnow()

@client.event
async def on_ready():
    print("Bot is online")
    
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
async def ban(ctx,member:discord.Member,reason=None):
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
