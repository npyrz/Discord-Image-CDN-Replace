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

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all()) # command prefix isn't used in this code

@bot.event 
async def on_ready():
     print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    # Get user's username
    username = message.author.name

    # Listen to all messages sent by users and check if its an attachment
    if message.attachments:
        # Loop through each attachment
        for attachment in message.attachments:
            print(attachment.filename) # Print check to see its printing all the attachments

            # Get the image from the attachment URL
            response = requests.get(attachment.url)
           
            # Opens image and saves to "imgs" directory with file name
            img = Image.open(BytesIO(response.content))
            img_path = os.path.join("imgs", attachment.filename)
            img.save(img_path)

            fileType = img_path.split('.')[-1]
            print(fileType)

            # Upload the image to imgur by calling the function from imageProcess.py
            client_id = os.getenv("IMGUR_CLIENT_ID")
            response = upload_image_to_imgur(img_path, client_id, username, fileType)
            print(response)
            
            # Send the link of the same attachment to the same channel where the user posted it in
            await message.channel.send(response)
            
            # Delete the image after uploading
            os.remove(img_path)
            
        # Delete the user's message
        await message.delete()
            
bot.run(os.getenv("TOKEN"))