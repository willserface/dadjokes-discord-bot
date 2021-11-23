# © 2021 - Will Serface

import discord
from random import randint

client = discord.Client()
reply_list = {}


async def reply_log(message, string):
    if isinstance(string, discord.File):
        log = await message.reply(file=string)
    else:
        log = await message.reply(string)
    reply_list[message] = log


def random_joke():
    jokes = list(open("jokes.txt", 'r'))
    return jokes[randint(0, len(jokes))]


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name="the news")
    )
    print("Logged in as", client.user)


@client.event
async def on_message(message):
    # Prevents self replies
    if message.author == client.user:
        return False

    # Remote stop capabilities
    if message.author.id == 609211773303652372 and str(message.content) == "bot remote shutoff":
        await message.delete()
        await client.change_presence(status=discord.Status.invisible)
        exit("Remote stop initiated")

    # Listens to any variation of 'tell me a joke'
    if (
            str(message.content).upper().__contains__("TELL ") and
            str(message.content).upper().__contains__(" A ") and
            str(message.content).upper().__contains__(" JOKE")
    ):
        await reply_log(message, random_joke())
        return True

    # Listens for "shit"
    if str(message.content).upper().__contains__("SHIT"):
        await reply_log(message, discord.File('shit.png'))
        return True

    # Listens for "bitch"
    if str(message.content).upper().__contains__("BITCH"):
        await reply_log(message, '<@907441492874915861>')
        return True

    # Listens for other curse words
    curses = ["FUCK", "HELL", "HECK", "DICK", "STUPID", "DUMB", "SHUT UP", "DAMN"]
    for curse in curses:
        if str(message.content).upper().__contains__(curse):
            await reply_log(message, "Language!")
            return True

    # Listens to any variation of 'father', 'dad', or 'parent'
    if (str(message.content).upper().__contains__("DAD") or
            str(message.content).upper().__contains__("FATHER") or
            str(message.content).upper().__contains__("PARENT") or
            str(message.content).upper().__contains__("PAPA")):
        await reply_log(message, "Eh? Did someone say my name?")
        return True

    # Listens for 'I'm ____'
    if (
            str(message.content).upper().startswith("IM ") or
            str(message.content).upper().startswith("I'M ") or
            str(message.content).upper().startswith("I AM ")
    ):
        if str(message.content).upper().startswith("I AM"):
            msg_split = str(message.content).split(' ')
            user_is = " ".join(msg_split[2:len(msg_split)])
        else:
            msg_split = str(message.content).split(' ')
            user_is = " ".join(msg_split[1:len(msg_split)])
        if user_is.upper() == "ANAKIN":
            await reply_log(message, "You can't pull a dad joke on your own father!")
            return True
        elif user_is.upper().__contains__("MERIDIA"):
            await reply_log(message, "You can't trick me, <@" + str(message.author.id) + ">.")
            return True

        elif (
                user_is.upper().__contains__("IM ") or
                user_is.upper().__contains__("I'M ") or
                user_is.upper().__contains__("I AM ")
        ):
            await reply_log(message, "Did you stutter?")
            return True
        elif any(not s.isascii() for s in user_is):
            await reply_log(message, "I don't think so, <@"+str(message.author.id)+">")
            return False
        elif user_is != "":
            await reply_log(message, ("Hi, " + user_is + "! I am <@"+str(908798748493217843)+">"))
            return True
        else:
            return False


@client.event
async def on_message_delete(message):
    await reply_list[message].delete()


@client.event
async def on_message_edit(message_before, message_after):
    await reply_list[message_before].delete()
    await on_message(message_after)


client.run(input("Enter bot token: "))
