from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')


@bot.command(name="insult", help="type !insult to generate a Sheakespearean insult")
async def insult(ctx):

    adjective = ['thin-boned', 'small-eyed', 'bumbling', 'pig-nosed', 'wretched', 'looming', 'shivering']
    noun = ['worm', 'creature', 'toad', 'witch', 'shrew', 'insectoid', 'loon', 'fool', 'weasel']

    insult = f'Thou art a {random.choice(adjective)} {random.choice(noun)}!'
    await ctx.send(insult)


with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)
    