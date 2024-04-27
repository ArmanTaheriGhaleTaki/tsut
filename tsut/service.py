import asyncio
import os
import glob
from telegram import Bot
import logging

class TSUT:
    def __init__(self, telegram_bot_token: str, telegram_channel_id: str, space_link: str, cookie_file: str):
        self.telegram_bot_token = telegram_bot_token
        self.telegram_channel_id = telegram_channel_id
        self.space_link = space_link
        self.cookie_file = cookie_file


    async def upload_to_telegram(self, directory="."):
        bot = Bot(self.telegram_bot_token)
        with open('output.txt', 'r') as desc:
            message = desc.read()
        for file in os.listdir(directory):
            if file.endswith('m4a'):
                await bot.send_audio(chat_id=self.telegram_channel_id, audio=file)


    async def download_audio(self):
        logging.info("Downloading content has been started...")
        process = await asyncio.create_subprocess_shell(
            f"twspace_dl -i {self.space_link} -c {self.cookie_file} -o '%(title)s;%(start_date)s;%(creator_name)s;%(creator_screen_name)s;'",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        if process.returncode != 0:
            logging.error(f"Error downloading audio: {stderr.decode()}")
        else:
            logging.info("Downloading content has been finished...")
            text = glob.glob('*.m4a')
            with open('output.txt', 'w') as file:
                for i in text:
                    x = i.split(";")
                    file.write(str(x[0])+'\n'+'\n'+str(x[3])+' ('+str(x[2])+')'+'\n'+'\n'+str(x[1])+'\n'+'\n'+'\n'+self.space_link)
                    newname = str(x[0])
                    if len(newname) == 0:
                        newname = x[3]
                    os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), newname))

                    await self.split_audio(newname)


    async def split_audio(self, newname):
        logging.info(f"Splitting audio {newname}...")
        process = await asyncio.create_subprocess_shell(
            f"ffmpeg -i {newname} -f segment -segment_time 3600 -c copy {newname}_%01d.m4a",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        if process.returncode != 0:
            logging.error(f"Error splitting audio: {stderr.decode()}")
        else:
            logging.info(f"Splitting {newname} has been finished...")
