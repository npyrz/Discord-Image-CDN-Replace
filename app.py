import discord
from discord.ext import commands
import os
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime
from dotenv import load_dotenv 
from imageProcess import upload_image_to_imgur
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
    # Get user's username
    username = message.author.name

    # Listen to all messages sent by users and check if its an attachment
    if message.attachments:
        # Loop through each attachment
        for attachment in message.attachments:
            print(attachment.filename) # Print check to see its printing all the attachments

            response = requests.get(attachment.url)
            # Generate a timestamped file name
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            file_name = f"{timestamp}.png"
            # Opens image and saves to "imgs" directory with custom timestamped file name
            img = Image.open(BytesIO(response.content))
            img_path = os.path.join("imgs", file_name)
            img.save(img_path)

            client_id = os.getenv("IMGUR_CLIENT_ID")
            response = upload_image_to_imgur(img_path, client_id, attachment.filename, username)
            print(response)
            
            # Send the link of the same attachment to the same channel where the user posted it in
            await message.channel.send(response)
            
            # Delete the image after uploading
            os.remove(img_path)
            
            # Delete the user's message
            await message.delete()
            

bot.run(os.getenv("TOKEN"))