import requests
import discord
import os
import json
from discord.ext import commands
import dotenv

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

bot = discord.Bot()

@bot.command(description="Fetches the specified Bible verse.")
@discord.option("version", type=discord.SlashCommandOptionType.string, description="The Bible version to use.")
@discord.option("book", type=discord.SlashCommandOptionType.string, description="The book of the Bible.")
@discord.option("chapter", type=discord.SlashCommandOptionType.integer, description="The chapter of the book.")
@discord.option("verse", type=discord.SlashCommandOptionType.integer, description="The verse number.")
async def verse(ctx, version: str, book: str, chapter: int, verse: int):
    try:
        url = f"https://cdn.jsdelivr.net/gh/wldeh/bible-api/bibles/{version}/books/{book}/chapters/{chapter}/verses/{verse}.json"
        response = requests.get(url)
        data = response.json()
        await ctx.respond(f"**{data["text"]}**")
    except:
        await ctx.respond(f"An error occurred while fetching the verse.")

bot.run(token)