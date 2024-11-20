# Modules we are going to require for the r-img command
import requests
import discord
from discord.ext import commands
from discord import app_commands
# Definition of a class named Rimg
class Rimg(commands.Cog): # Links the command file to the command handler
    def __init__(self, bot): # Initializes the bot to itself
        self.bot = bot

    @commands.Cog.listener() # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self): # This one is just for confirming that the command has been loaded
        print('r-img loaded')


    @app_commands.command(name = "r-img", description = "Sends random Reddit pictures from r/landscapes subreddit!")
    async def r_img(self, interaction: discord.Interaction): #The parameters are basically context (or the command) and length of the password (Default is 12)

        # Define the URL to fetch random photo from the Reddit LandscapePhotography subreddit
        url = 'https://www.reddit.com/r/LandscapePhotography/random/.json'

        # Fetch the response from Reddit
        response = requests.get(url, headers={'User-agent': 'Spectra'})

        # Parse the JSON content
        if response.status_code == 200:
            content = response.json()  # equivalent to JSON.parse(response.body) in JS
            
            # Extract necessary fields from the first meme post
            img_data = content[0]['data']['children'][0]['data']
            
            permalink = img_data['permalink']
            Url = f"https://reddit.com{permalink}"
            Image = img_data['url']
            Title = img_data['title']
            
            # Output the results (or you can embed them similarly as in JS)
            r_image = discord.Embed(
                title=Title,
                url=Url,
                color = discord.Color.orange()
            )
            r_image.set_image(url=Image)
            await interaction.response.send_message(embed=r_image)
        else:
            print(f"Failed to fetch image, status code: {response.status_code}")

async def setup(bot): # Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(Rimg(bot))