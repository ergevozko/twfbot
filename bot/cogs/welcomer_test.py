import discord
from discord.ext import commands
from PIL import Image, ImageChops, ImageDraw, ImageFont
from io import BytesIO
import asyncio
import os
import datetime
import random
import numpy as np

class _circle():
    

class testWelcomer(commands.Cog):

    def __init__(self, client):
        self.client = client


    # Code to round the Image (Profilepicture)
    @staticmethod
    def circle(pfp,size = (240,240)):
        pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
        bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(pfp.size, Image.ANTIALIAS)
        mask = ImageChops.darker(mask, pfp.split()[-1])
        pfp.putalpha(mask)
        return pfp


    # Test Welcome Message trigger with command
    @commands.command()
    @commands.is_owner()
    async def testwelcome(self, ctx, user: discord.Member):
        text = "Halo"+user.mention+", selamat datang dan semoga betah di TeaWaffle!\n\nJangan lupa baca dulu peraturan server di 『 📜｜rules 』 » lalu perkenalkan dirimu di 『 👋｜introduction 』 » setelah itu pilih roles agar bisa berinteraksi dan dapat informasi menarik lainnya di 『 🥇｜get-roles 』"
        with BytesIO() as image_binary:
            
            useravatar = user.avatar_url_as(size=1024)  # Profilepicture = member.avatar_url_as(size=500)
            datavatar = BytesIO(await useravatar.read())
            avatar = Image.open(datavatar).convert("RGBA")
            avatar = circle(pfp)
            avatar = pfp.resize((265,265)) # Resizes the Profilepicture so it fits perfectly in the circle
            
            img = Image.open("bot\resources\welcomer\twfcard.png")
            draw = ImageDraw.Draw(img)
            msgtop = user.id + "just joined the server"
            msgtopfont = ImageFont.truetype("bot\resources\welcomer\shentox-medium.otf", 42)
            msgbot = ("Member #" + str(guild.member_count))
            msgbotfont = ImageFont.truetype("bot\resources\welcomer\shentox-medium.otf", 28)
            draw.text((62, 340), msgtop, (255, 255, 255), font=msgtopfont) #draws top text
            draw.text((62, 420), msgbot, (255, 255, 255), font=msgtopfont) #draws bottom text
            
            img.paste(pfp, (430,70), pfp) # Pastes the Profilepicture on the Background Image
            
            arr = io.BytesIO()
            img.save(arr, format='PNG') # img.save(image_binary, 'PNG')
            arr.seek(0) # image_binary.seek(0)
            imgFile = discord.File(arr)
            
            await ctx.send(file=imgFile)

def setup(client):
    client.add_cog(testWelcomer(client))