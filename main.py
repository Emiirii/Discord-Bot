import discord
from discord.ext import commands
from utils import *
from functions import * 
import os 
import asyncio

 
intents=discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)

Bot=commands.Bot(command_prefix="!dc", intents=intents)

token=open("token.txt", "r").read()

game = Game()

@Bot.event
async def on_ready():
    print("Ben Hazırım")
    asyncio.get_running_loop

@Bot.event
async def on_member_join(member):
    channel=discord.utils.get(member.guild.text_channels, name="hos-geldiniz")
    await channel.send(f"{member} ramıza katıldı hoş geldi")
    print(f"{member} aramıza katıldı hoş geldi")
    asyncio.get_running_loop

@Bot.event
async def on_member_remove(member):
    channel=discord.utils.get(member.guild.text_channels, name="ayrılanlar")
    await channel.send(f"{member} aramızdan ayrıldı güle güle:(")
    print(f"{member} aramızdan ayrıldı güle güle:(")
    asyncio.get_running_loop

@Bot.command(aliases=["game", "oyun"])
async def emir(ctx, *args):
    if "roll" in args:
        await ctx.send(game.roll_dice())
    else:
        await ctx.send("aramızdakioyuncu.com")
        asyncio.get_running_loop

@Bot.command()
@commands.has_role("Yönetim Ekibi")
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount)
    asyncio.get_running_loop


@Bot.command(aliases=["copy"])
@commands.has_role("Yönetim Ekibi")
async def clone_channel(ctx, amount=1):
    await ctx.channel.clone()
    asyncio.get_running_loop

@Bot.command()
@commands.has_role("Yönetim Ekibi")
async def kick(ctx, member:discord.Member, *args, reason="Yok"):
    await member.kick(reason=reason)
    asyncio.get_running_loop

@Bot.command()
@commands.has_role("Yönetim Ekibi")
async def ban(ctx, member:discord.Member, *args, reason="Yok"):
   await member.ban(reason=reason)
   asyncio.get_running_loop

@Bot.command()

async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    asyncio.get_running_loop

    for bans in banned_users:
        user = bans.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned user {user.mention}")
            return
            

@Bot.command()
async def load(ctx, extension):
    Bot.load_extension(f"cogs.{extension}")
    asyncio.get_running_loop


@Bot.command()
async def unload(ctx, extension):
    Bot.unload_extension(f"cogs.{extension}")
    asyncio.get_running_loop

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        Bot.load_extension(f"cogs.{filename[:-3]}")



Bot.run(token)
