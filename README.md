# discord-to-dropbox-archiver
This Discord bot utilizes the handy [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter) tool to export the message history of a channel
into an HTML file. This file is then stored in a Dropbox folder.

## Requirements
It's expected this bot will run in a Python3 environment with certain third-party installed via
```
pip3 install -r requirements.txt
```

You'll need two tokens in order for this bot to work: a Discord token and a Dropbox token. To generate a Discord token, the DiscordChatExporter wiki has
useful instructions that can be found [here](https://github.com/Tyrrrz/DiscordChatExporter/wiki/Obtaining-Token-and-Channel-IDs#how-to-get-a-bot-token).
For a Dropbox token, check this [guide](https://developers.dropbox.com/oauth-guide).

Finally the Discord token should be set as `DISCORD_TOKEN` and the Dropbox token as `DROPBOX_TOKEN` as environment variables on your local machine or
as config variables on Heroku.

## Usage
To run the bot on your machine
```
python3 slash-archive.py
```

To run via Docker
```
docker build -t tag_name 
docker run -e "DISCORD_TOKEN=discord_token" -e "DROPBOX_TOKEN=dropbox_token" tag_name
```

Then in whatever Discord channel you wish to archive
```
/archive some_category
```
