import discord
from random import randint

client = discord.Client()


def random_joke():
    jokes = list(open("jokes.txt", 'r'))
    return jokes[randint(0, len(jokes))]


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name="\'tell me a joke\'"
        ))
    print("Logged in as", client.user)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(message.content).upper().__contains__("TELL ME A JOKE"):
        await message.channel.send(random_joke())


client.run(input("Enter bot token: "))
