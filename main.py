#!/usr/bin/env python
from scripts.telegram_uploader import upload_to_telegram
from scripts.twitter_space_downloader import download_audio
from scripts.config import bot_token, chat_id
import click
import os 

@click.command()
@click.option(
    "-i",
    "--link",
    "link",
    type=click.Path(),
    multiple=True,
    help="The space link to download .",
)
@click.option(
    "-c",
    "COOKIE_FILE",
    type=click.Path(),
    multiple=True,
    help="""cookies file in the Netscape format. The specs of the
                        Netscape cookies format can be found here:
                        https://curl.se/docs/http-cookies.html. The cookies
                        file is now required due to the Twitter API change
                        that prohibited guest user access to Twitter API
                        endpoints on 2023-07-01.""",
)
def hi(link,COOKIE_FILE):

   download_audio(link[0],COOKIE_FILE[0])
   upload_to_telegram(bot_token, chat_id, ".")
        
if __name__ == '__main__':
    hi()

