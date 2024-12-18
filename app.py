import discord
from discord.ext import commands
import os
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime
from dotenv import load_dotenv 
load_dotenv()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all()) # MAY BE REMOVED ON RELEASE 

@bot.event 
async def on_ready():
     print(f'We have logged in as {bot.user}')

# @bot.command()
# async def sync(ctx):
#     await bot.tree.sync()
#     await ctx.send("Synced!")

@bot.event
async def on_message(message):
    # Listen to all messages sent by users and check if its an attachment
    if message.attachments:
        # Loop through each attachment
        for attachmentURL in message.attachments:
            print(attachmentURL.filename) # Print check to see its printing all the attachments

            response = requests.get(attachmentURL)
            # Generate a timestamped file name
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            file_name = f"{timestamp}.png"
            # Opens image and saves to "imgs" directory with custom timestamped file name
            img = Image.open(BytesIO(response.content))
            img.save(os.path.join("imgs", file_name))

            await message.channel.send(attachmentURL)
        

bot.run(os.getenv("TOKEN"))