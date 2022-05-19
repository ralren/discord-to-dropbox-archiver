
import os
import glob
import subprocess
import disnake
import dropbox

from disnake.ext import commands
from dropbox.files import WriteMode

discord_token = os.environ['DISCORD_TOKEN']
dropbox_token = os.environ['DROPBOX_TOKEN']

dbx = dropbox.Dropbox(dropbox_token)
bot = commands.Bot(command_prefix='!',
    sync_commands_debug=True
)

@bot.slash_command(description="Archives the channel into dropbox")
async def archive(
    inter: disnake.ApplicationCommandInteraction, 
    category: str = commands.Param(choices=["Category1, Category2, Category3"])
):
    await inter.response.defer()
    await local_archive_channel(inter.channel)
    await dropbox_archive_channel(inter.channel, category)
    await inter.followup.send("Channel has been archived succesfully.")

async def local_archive_channel(channel):
    command = "dotnet DiscordChatExporter.CLI/DiscordChatExporter.Cli.dll export -t {0} -c {1} -o {2}.html".format(discord_token, channel.id, channel.name)
    subprocess.call(command, shell = True)

async def dropbox_archive_channel(channel, category):
    archived_file = "{0.name}.html".format(channel)
    with open(archived_file, 'rb') as f:
        rename = '/{0}/{1.name}.html'.format(category, channel)
        dbx.files_upload(f.read(), rename, mode=WriteMode('overwrite'))
        print('{0} has been uploaded to Dropbox'.format(rename))
        
    os.remove(archived_file)

bot.run(discord_token)
