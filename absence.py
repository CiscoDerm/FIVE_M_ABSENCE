import discord
from discord.ext import commands
from discord.ui import Button, View, Modal, TextInput
import datetime

TOKEN = 'TOKEN_BOT'  # Remplacez par votre token de bot

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

class AbsenceModal(Modal):
    def __init__(self):
        super().__init__(title="Déclaration d'absence")

        self.add_item(TextInput(label="Prénom - Nom", placeholder="Entrez votre prénom et nom"))
        self.add_item(TextInput(label="Date", placeholder="Entrez la date (JJ/MM/AAAA)"))
        self.add_item(TextInput(label="Motif", placeholder="Entrez le motif de l'absence", style=discord.TextStyle.long))

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Déclaration d'absence", color=discord.Color.dark_gray())
        embed.add_field(name="Prénom - Nom", value=self.children[0].value, inline=False)
        embed.add_field(name="Date", value=self.children[1].value, inline=False)
        embed.add_field(name="Motif", value=self.children[2].value, inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=False)

class AbsenceView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Absence', style=discord.ButtonStyle.red)
    async def declare_absence(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = AbsenceModal()
        await interaction.response.send_modal(modal)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channel = bot.get_channel(ID_CHANNEL)  # Remplacez par l'ID de votre channel
    await channel.send("Cliquez sur le bouton pour déclarer une absence :", view=AbsenceView())

bot.run(TOKEN)
