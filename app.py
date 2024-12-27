import discord
from discord.ext import commands
import os
import requests
from dotenv import load_dotenv 
from imageProcess import upload_image_to_imgur
load_dotenv()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all()) # command prefix isn't used in this code

@bot.event 
async def on_ready():
     print(f'{bot.user} is online!')

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
            if attachment.filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.mp4', '.mkv', '.mov', '.avi')):
                # Save the file to local storage
                await attachment.save(attachment.filename)
                img_path = attachment.filename
            else:
                await message.delete()
                await message.channel.send("Invalid file type. Please upload an image or a video with the following extensions: .png, .jpg, .jpeg, .gif, .mp4, .mkv, .mov")
                return
           
            # Get the file type of the image
            fileType = img_path.split('.')[-1]
            print(fileType)

            # Upload the image to imgur by calling the function from imageProcess.py
            client_id = os.getenv("IMGUR_CLIENT_ID")
            response = upload_image_to_imgur(img_path, client_id, username, fileType)
            print(response)
            
            # Send the link of the same attachment to the same channel where the user posted it in
            if fileType in ['png', 'jpg', 'jpeg']:
                #await message.channel.send(response)
                embed = discord.Embed(
                title= attachment.filename,
                url=response
                )
                embed.set_image(url=response)
                embed.set_author(name=username, icon_url=message.author.display_avatar.url)
                embed.timestamp = message.created_at
                await message.channel.send(embed=embed)
            elif fileType in ['gif', 'mp4', 'mkv', 'mov', 'avi']:
                embed = discord.Embed(
                title= attachment.filename,
                #description = f"[Click here to view the video.({response})",
                url=response
                )
                embed.set_image(url=response)
                embed.set_author(name=username, icon_url=message.author.display_avatar.url)
                embed.timestamp = message.created_at
                await message.channel.send(embed=embed)
            
            # Delete the image after uploading
            os.remove(img_path)
            
        # Delete the user's message
        await message.delete()
            
bot.run(os.getenv("TOKEN"))