import discord
from discord.ext import commands
from discord import app_commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ping loaded')


    @app_commands.command(name = "ping", description = "Sends the time it takes your message to reach spectra!")
    async def  ping(self, interaction: discord.Interaction): #The parameters are basically context (or the command) and length of the password (Default is 12)
        latency = interaction.client.latency*1000
        await interaction.response.send_message(f"Latency: {latency:.2f}")

async def setup(bot):
    await bot.add_cog(ping(bot))
