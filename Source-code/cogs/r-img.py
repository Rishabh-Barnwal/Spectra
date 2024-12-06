# Modules we are going to require for the r-img command
import praw  # Python Reddit API Wrapper
import discord
from discord.ext import commands
from discord import app_commands
import random

# Definition of a class named Rimg
class Rimg(commands.Cog):  # Links the command file to the command handler
    def __init__(self, bot):  # Initializes the bot to itself
        self.bot = bot

        # Set up Reddit API credentials
        self.reddit = praw.Reddit(
            client_id="YOUR_CLIENT_ID",  # Replace with your Reddit App Client ID
            client_secret="YOUR_CLIENT_SECRET",  # Replace with your Reddit App Client Secret
            user_agent="Spectra Bot (by u/YOUR_USERNAME)"  # Replace with your Reddit username
        )

    @commands.Cog.listener()  # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self):  # This one is just for confirming that the command has been loaded
        print('r-img loaded')

    @app_commands.command(name="r-img", description="Sends random Reddit pictures from r/LandscapePhotography subreddit!")
    async def r_img(self, interaction: discord.Interaction):
        try:
            # Fetch subreddit posts
            subreddit = self.reddit.subreddit("LandscapePhotography")
            posts = list(subreddit.hot(limit=50))  # Fetch the top 50 hot posts

            # Choose a random post
            random_post = random.choice(posts)

            # Extract necessary fields
            Title = random_post.title
            Url = random_post.url
            Post_Url = random_post.shortlink

            # Create and send the embed
            r_image = discord.Embed(
                title=Title,
                url=Post_Url,
                color=discord.Color.orange()
            )
            r_image.set_image(url=Url)
            await interaction.response.send_message(embed=r_image)
        except Exception as e:
            # Handle errors
            await interaction.response.send_message(
                f"Failed to fetch posts from Reddit. Error: {str(e)}",
                ephemeral=True
            )
            print(f"Error: {str(e)}")

async def setup(bot):  # Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(Rimg(bot))
