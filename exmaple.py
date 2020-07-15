#Code I just want to test out
import discord
from discord.ext import commands
from jokes import father
import random
from discord.ext.commands import has_permissions
from datetime import datetime
import time
import youtube_dl
from discord.utils import get
import os
import shutil
import asyncio
from profanity import bad_words_list

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is ready")

#Clears a specified amount of messages
@client.command()
@has_permissions(kick_members=True)
async def clear(ctx, amount=1):
    amount += 1
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    now = datetime.now()
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .clear {amount}, {now}, clear\n") #.logs <name not id>
    await ctx.channel.purge(limit=amount)


#Stupid command, I am not sure why I made it
@client.command()
async def prefix(ctx):
    await ctx.send(f"Hello")

#Bans a user
@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    hello = str(member.id)
    hello1 = "<@" + hello + ">"
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    now = datetime.now()
    with open("punishments.csv", "a") as f:
        f.write(f"{hello1}, {reason}, {now}, **BAN**")
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .ban {hello1} {reason}, {now}, ban\n")
    await member.ban(reason=reason)

#Kicks a user
@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    hello = str(member.id)
    hello1 = "<@" + hello + ">"
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    now = datetime.now()
    with open("punishments.csv", "a") as f:
        f.write(f"{hello1}, {reason}, {now}, **KICKED**")
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .kick {hello1} {reason}, {now}, kick\n")
    await member.kick(reason=reason)

#Bot repeats message
@client.command()
async def echo(ctx, *, arg):
    amount = 1
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    now = datetime.now()
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .echo {arg}, {now}, echo\n")
    await ctx.channel.purge(limit=amount)
    await ctx.send(arg)

#Makes an announcement in announcement channel
@client.command()
@has_permissions(manage_roles=True)
async def announce(ctx, *, message):
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    now = datetime.now()
    real_user = str(ctx.message.author.name)
    channel = client.get_channel(730958836151877703)
    embed = discord.Embed(
        title = "**Announcement!**",
        description = message,
        colour = discord.Colour.green()
    )
    embed.set_footer(text = "Sent by: " + real_user)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/730132856067588203/730947681895055440/GRN_2.png")
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .announce {message}, {now}, announce\n")
    await channel.send(embed=embed)

# @client.command()
# async def ping(ctx, member : discord.Member):
#     hello = str(member.id)
#     hello1 = "<@" + hello + ">"
#     await ctx.send(f"PONG {hello1}")

#Warns a player
@client.command()
@has_permissions(kick_members=True)
async def warn(ctx, member : discord.Member, *, reason=None):
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    now = datetime.now()
    hello = str(member.id)
    hello1 = "<@" + hello + ">"
    with open("warnings.csv", "a") as f:
        f.write(f"{hello1}, {reason}\n")
    sentence = "Warned " + hello1 + " for " + reason
    now = datetime.now()
    with open("punishments.csv", "a") as f:
        f.write(f"{hello1}, {reason}, {now}, **WARN**\n")
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .warn {hello1} {reason}, {now}, warn\n")
    await ctx.send(sentence)

#Checks previous warnings
@client.command()
@has_permissions(kick_members=True)
async def warns(ctx, member : discord.Member):
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    now = datetime.now()
    hello = str(member.id)
    hello1 = "<@" + hello + ">"
    searchfile = open("warnings.csv", "r")
    for lines in searchfile:
        if lines.startswith(hello1):
            await ctx.send(lines)

    searchfile.close()
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .warns {hello1}, {now}, warns\n")

#Gives a dadjoke
@client.command()
async def dadjoke(ctx):
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    now = datetime.now()
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .dadjoke, {now}, dadjoke\n")
    joke = random.choice(father)
    await ctx.send(joke)

#Reports a player
@client.command()
async def report(ctx, member : discord.Member, *, reason=None, amount=1):
    hello = str(member.id)
    hello1 = "<@" + hello + ">"
    await ctx.channel.purge(limit=amount)
    report_message = "Successfully reported"
    await ctx.send(report_message)
    channel = client.get_channel(730962771596017754)
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    now = datetime.now()
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .report {hello1} {reason}, {now}, report\n")
    await channel.send("Report sent by " + username1 + " against " + hello1 + " for:\n" + "``" + reason + "``")
    time.sleep(3)
    await ctx.channel.purge(limit=amount)

# @client.command()
# async def ticket(ctx, *, reason):
#     username = ctx.message.author.name
#     username1  = str(ctx.message.author.id)
#     username2 = "<@" + username1 + ">"
#     name = "tickets"
#     category = discord.utils.get(ctx.guild.categories, name=name)
#     guild = ctx.message.guild
#     channel = await ctx.guild.create_text_channel(username, category=category)
    ###await message.channel.set_permissions(message.author, read_messages=True,send_messages=True, overwrite=True)
    # await channel.set_permissions(member, read_messages=False)
    # await channel.send("Ticket send by: " + username2 + "\n" + "``" + reason + "``")

#Makes a ticket
@client.command()
async def ticket (ctx, *, reason):
    username1 = str(ctx.message.author.id)
    username2 = "<@" + username1 + ">"
    now = datetime.now()
    with open("tickets.csv", "a") as f:
        f.write(f"{username2},{reason}\n")
    with open("logs.csv", "a") as f:
        f.write(f"{username2}, .ticket {reason}, {now}, ticket\n")
    await ctx.send("We have recieved your ticket!")

#Checks list of tickets
@client.command()
@has_permissions(kick_members=True)
async def tickets(ctx):
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    now = datetime.now()
    searchfile = open("tickets.csv", "r")
    for line in searchfile:
        await ctx.send(line)
    searcfile.close()
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .tickets, {now}, tickets\n")

#Deletes all tickets
@client.command()
@has_permissions(kick_members=True)
async def tdelete(ctx):
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    now = datetime.now()
    file = open("tickets.csv", "r+")
    file.truncate(0)
    file.close()
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .tdelete, {now}, tdelete\n")
    await ctx.send("Tickets have been deleted!")

#Permit someone to post a link, but it doesn't stop them from posting it even if they don't have a permit
@client.command()
@has_permissions(kick_members=True)
async def permit(ctx, member: discord.Member):
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    hello = str(member.id)
    hello1 = "<@" + hello + ">"
    now = datetime.now()
    with open("permits.csv", "a") as f:
        f.write(f"{hello1},{now}\n")
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .permit {hello1}, {now}, permit\n")
    sentence = "Permitted " + hello1 + " to post a link! You have 5 minutes to post a link or your permit will be revoked!"
    await ctx.send(sentence)

#Checks someone previous permits
@client.command()
@has_permissions(kick_members=True)
async def permits(ctx, member: discord.Member):
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    now = datetime.now()
    hello = str(member.id)
    hello1 = "<@" + hello + ">"
    searchfile = open("permits.csv", "r")
    for line in searchfile:
        if line.startswith(hello1):
            await ctx.send(line)

    searchfile.close()
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .permits {hello1}, {now}, permits\n")

#Adds suggestions
@client.command()
async def suggest(ctx, *, reason=None):
    now = datetime.now()
    amount = 1
    await ctx.channel.purge(limit=amount)
    username1 = str(ctx.message.author.id)
    username2 = "<@" + username1 + ">"
    real_user = str(ctx.message.author.name)
    embed = discord.Embed(
        title = "Suggestor",
        description = real_user + "\n\n",
        colour=discord.Colour.green()
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/730132856067588203/730947681895055440/GRN_2.png")
    reason = "**" + reason + "**"
    embed.add_field(name="Suggestion", value=reason)
    embed.set_footer(text=username2 + "       " + str(datetime.now()))
    with open("logs.csv", "a") as f:
        f.write(f"{username2}, .suggest {reason}, {now}, suggest\n")
    await ctx.send(embed=embed)

#Adds something to todo list
@client.command()
async def todo(ctx, *, reason=None):
    username1 = str(ctx.message.author.id)
    username2 = "<@" + username1 + ">"
    now = datetime.now()
    with open("todo.csv", "a") as f:
        f.write(f"{username2}, {reason}\n")
    with open("logs.csv", "a") as f:
        f.write(f"{username2}, .todo {reason}, {now}, todo\n")
    await ctx.send("Added to todo list")

#Checks todo list
@client.command()
async def todolist(ctx):
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    now = datetime.now()
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .todolist, {now}, todolist\n")
    searchfile = open("todo.csv", "r")
    for line in searchfile:
        await ctx.send(line)

#Delete todo list
@client.command()
async def dtodo(ctx):
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    now = datetime.now()
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .dtodo, {now}, dtodo\n")
    file = open("todo.csv", "r+")
    file.truncate(0)
    file.close()
    await ctx.send("To do list has been cleared!")

#Checks bot's ping
@client.command()
async def ping(ctx):
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    now = datetime.now()
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .ping, {now}, ping\n")
    await ctx.send(f"Your ping is: {round(client.latency * 1000)}ms")

#Mutes a player
@client.command()
@has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    hello = str(member.id)
    hello1 = "<@" + hello + ">"
    role = get(member.guild.roles, name='muted')
    await member.add_roles(role)
    sentence = hello1 + " has been muted for " + reason
    now = datetime.now()
    with open("punishments.csv", "a") as f:
        f.write(f"{hello1}, {reason}, {now}, **MUTE**\n")
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .mute {hello1} {reason}, {now}, mute\n")
    await ctx.send(sentence)

#Unmute a person
@client.command()
@has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member, *, reason=None):
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    hello = str(member.id)
    hello1 = "<@" + hello + ">"
    role = get(member.guild.roles, name='muted')
    await member.remove_roles(role)
    sentence = hello1 + " has been unmuted for " + reason
    now = datetime.now()
    with open("punishments.csv", "a") as f:
        f.write(f"{hello1}, {reason}, {now}, **UNMUTE**\n")
    with open("unmute", "a") as f:
        f.write(f"{username1}, .unmute {hello1} {reason}, {now}, unmute\n")
    await ctx.send(sentence)

#Checks punishment history
@client.command()
@has_permissions(kick_members=True)
async def history(ctx, member: discord.Member):
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    now = datetime.now()
    hello = str(member.id)
    hello1 = "<@" + hello + ">"
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .history {hello1}, {now}, history\n")
    searchfile = open("punishments.csv", "r")
    for line in searchfile:
        if line.startswith(hello1):
            await ctx.send(line)

#Check all previously used commands
@client.command()
@has_permissions(ban_members=True)
async def logs(ctx, member: discord.Member):
    hello = str(member.id)
    hello1 = "<@" + hello + ">"
    searchfile = open("logs.csv", "r")
    for line in searchfile:
        if line.startswith(hello1):
            await ctx.send(line)
    searchfile.close()

#Delete all logs
@client.command()
@has_permissions(ban_members=True)
async def dellogs(ctx):
    file = open("logs.csv", "r+")
    file.truncate(0)
    file.close()
    await ctx.send("All logs have been deleted")

#Log deleted messages and puts them into a channel
@client.event
async def on_message_delete(message):
    now = str(datetime.now())
    channel = client.get_channel(731303668309033022)
    content = message.content
    channel101 = str(message.channel.id)
    channel102 = "<#" + channel101 + ">"
    author = str(message.author.id)
    author1 = "<@" + author + ">"
    post = author1 + " deleted a message in " + channel102
    embed = discord.Embed(
        title="**Someone has deleted a message!**",
        description=post,
        colour = discord.Colour.red()
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/730132856067588203/730947681895055440/GRN_2.png")
    embed.add_field(name='Message:\n', value=content)
    await channel.send(embed=embed)

#Welcome message and auto role
@client.event
async def on_member_join(member):
    channel = client.get_channel(730958846268407879)
    role = get(member.guild.roles, name='Bot Tester')
    await member.add_roles(role)
    memberid = str(member.id)
    memberfid = memberid
    channel_id = str(730966148643815504)
    bot_info_channel = "<#" + channel_id + ">"
    await channel.send("Welcome to Skills Bot Test Server, check out " + bot_info_channel + ", <@" + memberfid + ">" + "!")

#.active for moderators who are online, this can allow them to recieve permit requests
@client.command()
@has_permissions(kick_members=True)
async def online(ctx):
    now = datetime.now()
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    member = ctx.message.author
    role = get(member.guild.roles, name='online')
    await member.add_roles(role)
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .online, {now}, online\n")
    await ctx.send(username1 + ", you are now marked as online!")

#.offline for moderators who are logging off, this won't give them permit request notifcations
@client.command()
@has_permissions(kick_members=True)
async def offline(ctx):
    now = datetime.now()
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    member = ctx.message.author
    role = get(member.guild.roles, name='online')
    await member.remove_roles(role)
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .offline, {now}, offline\n")
    await ctx.send(username1 + ", you are now marked as offline")

#Sends out a message to moderators with online status
#Permit request
@client.command()
async def rpermit(ctx):
    channel101 = str(ctx.channel.id)
    channel102 = "<#" + channel101 + ">"
    now = datetime.now()
    username = str(ctx.author.id)
    username1 = "<@" + username + ">"
    active_staff_id = str(731581259712692326)
    active_staff = "<@&" + active_staff_id + ">"
    channel = client.get_channel(731584332400951298)
    with open("logs.csv", "a") as f:
        f.write(f"{username1}, .rpermit, {now}, rpermit\n")
    await channel.send(username1 + " has requested a permit in " + channel102 + "\n" + active_staff + "\n")
    await ctx.send("Your permit request has been sent!")

@client.event
async def on_message(message):
    content = message.content
    channel101 = str(message.channel.id)
    channel102 = "<#" + channel101 + ">"
    channel = client.get_channel(732352107495292939)
    now = datetime.now()
    username = str(message.author.id)
    username1 = "<@" + username + ">"
    user_post = username1 + " posted in channel " + channel102 + ":\n"
    uppercased = content.isupper()
    for words in bad_words_list:
        if words in message.content:
            embed = discord.Embed(
                title="**FLAGGED!**",
                description=user_post,
                colour=discord.Colour.red()
            )
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/730132856067588203/730947681895055440/GRN_2.png")
            embed.add_field(name="Post:\n", value=content)
            await channel.send(embed=embed)
        elif uppercased == True:
            embed = discord.Embed(
                title="**FLAGGED!**",
                description=user_post,
                colour=discord.Colour.red()
            )
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/730132856067588203/730947681895055440/GRN_2.png")
            embed.add_field(name="Post:\n", value=content)
            await channel.send(embed=embed)
            break

    await client.process_commands(message)

'''
@client.command(pass_context=True)
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await ctx.send(f"Joined {channel}")

@client.command(pass_context=True)
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f"Left {channel}")

@client.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url):

    def check_queue():
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_q = length - 1
            try:
                first_file = os.listdir(dir)[0]
            except:
                print("No more queued song(s)\n")
                queues.clear()
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
            if length != 0:
                print("Songs done, playing next queued\n")
                print(f"Songs still in queue: {still_q}")
                song_there = os.path.isfile("songs.mp3")
                if song_there:
                    os.remove("song.mp3")
                shutil.move(song_path, main_location)
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, "song.mp3")

                voice.play(discord.FFmpegpCMAudio("songs.mp3"), after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.07

            else:
                queues.clear()
                return
        else:
            queues.clear()
            print("No songs were queued before the ending of the last song\n")

    songs_there = os.path.isfile("songs.mp3")
    try:
        if songs_there:
            os.remove("songs.mp3")
            queues.clear()
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music Playing")
        return

    Queue_infile = os.path.isdir("./Queue")
    try:
        Queue_folder = "./Queue"
        if Queue_infile is true:
            print("Removed old Queue Folder")
            shutil.rmtree(Queue_folder)
    except:
        print("No old Queue folder")

    await ctx.send("Getting everything ready now")

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        'postprocessors': [{
            "key" : "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading Audio Now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = (f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("songs.mp3"), after=lambda e: check_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    await ctx.send(f"Playing: {nname[0]}")
    print("playing\n")

@client.command(pass_context=True, aliases=['pa', 'pau'])
async def pause(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music Paused")
        voice.pause()
        await ctx.send("Music Paased")
    else:
        print("Music not playing failed pause")
        await ctx.send("Music not playing")

@client.command(pass_context=True, aliases=['r', 'res'])
async def resume(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Resumed Music")
        voice.resume()
        await ctx.send("Resumed Music")
    else:
        print("Music is NOT paused")
        await ctx.send("Music is NOT paused")

@client.command(pass_context=True, aliases=['s', 'ski'])
async def skip(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    queues.clear()

    if voice and voice.is_playing():
        print("Song skipped")
        voice.stop()
        await ctx.send("Song skipped")
    else:
        print("Not playing")
        await ctx.send("Not playing")

# queues = {}
#
# @client.command(pass_context=True, aliases=['q', 'que'])
# async def queue(ctx, url: str):
#     Queue_infile = os.path.isdir("./Queue")
#     if Queue_infile is False:
#         os.mkdir("Queue")
#     DIR = os.path.abspath(os.path.realpath("Queue"))
#     q_num = len(os.listdir(DIR))
#     q_num += 1
#     add_queue = True
#     while add_queue:
#         if q_num in queues:
#             q_num += 1
#         else:
#             add_queue = False
#             queues[q_num] = q_num
#
#     queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song {q_num}.%(ext)s")
#
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'quiet' = True,
#         'outtmpl': queue_path,
#         'postprocessors' : [{
#             'key': 'FFmpegExtractAudio',
#
#     }]
#     }

# @client.command(pass_context=True, aliases)

# @client.command(pass_context=True)
# async def play(ctx, url):
#     server = ctx.message.guild
#     voice_client = ctx.message.guild.voice_client(server)
#     player = await voice_client.create_ytdl_player(url)
#     players[server.id] = player
#     player.start()


# @client.event
# async def on_message(message):
#     if message.content.startswith('wassup'):
#         channel = message.channel
#         await channel.send("nothing much")
'''
client.run("NzEwNTAzNDc5NjcxNzgzNDU2.XwTBwA.9DipgPu2aP9gFj3tVU-E0MXI8hc")