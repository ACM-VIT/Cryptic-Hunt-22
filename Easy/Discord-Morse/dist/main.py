# https://discord.com/api/oauth2/authorize?client_id=1017668108686729237&permissions=0&scope=bot%20applications.commands

import dotenv
from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import interactions

server_id = 1017708756676644935


load_dotenv()
token = os.getenv('TOKEN')
bot = interactions.Client(token)


@bot.event
async def on_ready():
    print("Ready!")

# hello command


@bot.command(
    name="hello",
    description="An example command",
    scope=server_id,
)
async def hello(ctx: interactions.CommandContext, user: discord.Member = None):
    if user == None:
        user = ctx.author
        await ctx.send("Check DM!", ephemeral=True)
        await user.send("Hello There!")


# youtube link command
@bot.command(
    name="answer",
    description="Maybe Happy will give you a reward?",
    scope=server_id,
    options=[
        interactions.Option(
            type=interactions.OptionType.STRING,
            name="answer",
            description="Input your answer"
        ),
    ],
)
async def say(ctx: interactions.CommandContext, user: discord.Member = None, *, answer=str):
    if user == None:
        user = ctx.author
        if (answer == "Hi"):
            await ctx.send("Correct Answer!", ephemeral=True)
            await user.send("https://youtu.be/_dkFaEcR9ig")

        else:
            await ctx.send("Wrong Answer!", ephemeral=True)


bot.start()
