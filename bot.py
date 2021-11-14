# © 2021 - Will Serface

import discord
from random import randint

client = discord.Client()


def random_joke():
    jokes = list(open("jokes.txt", 'r'))
    return jokes[randint(0, len(jokes))]


def server_name(user):
    return user.display_name


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name="the news"
        ))
    print("Logged in as", client.user)


@client.event
async def on_message(message):
    # Prevents self replies
    if message.author == client.user:
        return

    # Listens to any variation of 'father', 'dad', or 'parent'
    if (str(message.content).upper().__contains__("DAD") or
            str(message.content).upper().__contains__("FATHER") or
            str(message.content).upper().__contains__("PARENT") or
            str(message.content).upper().__contains__("PAPA")):
        await message.channel.send("Eh? Did someone say my name?")
        return

    # Listens to any variation of 'tell me a joke'
    if str(message.content).upper().__contains__("TELL ME A JOKE"):
        await message.reply(random_joke())
        return

    # Listens for curse words
    curses = ["FUCK", "SHIT", "BITCH", "HELL", "HECK", "FRICK", "FREAK", "DICK", "STUPID", "DUMB", "SHUT UP"]
    for curse in curses:
        if str(message.content).upper().__contains__(curse):
            if curse == "SHIT":
                await message.reply(file=discord.File('shit.png'))
                return
            else:
                await message.reply("Language!")
                return

    # Listens to 'I'm ____'
    if (
            str(message.content).upper().startswith("IM") or
            str(message.content).upper().startswith("I'M") or
            str(message.content).upper().startswith("I AM")):
        if str(message.content).upper().startswith("I AM"):
            msg_split = str(message.content).split(' ')
            user_is = " ".join(msg_split[2:len(msg_split)])
        else:
            msg_split = str(message.content).split(' ')
            user_is = " ".join(msg_split[1:len(msg_split)])
        if user_is.upper() == "ANAKIN":
            await message.reply("You can't pull a dad joke on your own father!")
        else:
            await message.reply("Hi, " + user_is + "! I am " + server_name(client.user))
        return


client.run(input("Enter bot token: "))
