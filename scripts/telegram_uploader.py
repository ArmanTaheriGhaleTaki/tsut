import os
import subprocess
from telegram import Bot

def upload_to_telegram(bot_token, channel_id,directory):
    bot = Bot(token=bot_token) # initialize bot
    with open('output.txt', 'r') as desc: # read the desc
        message = desc.read()
    for file in os.listdir(directory): # open file
        if file.endswith('m4a'):
            print(file)
            filepath = os.path.join(directory, file) # store the full path
            with open(filepath, 'rb') as audio_file: # open the file
                bot.send_audio(chat_id=channel_id, audio=audio_file)

           # subprocess.run(
           #    [
           #     "curl",
           #     "-s",
           #     "-X",
           #     "POST",
           #     f"https://api.telegram.org/bot{bot_token}/sendDocument",
           #     "-F",
           #     f"chat_id={channel_id}",
           #     "-F",
           #     f"document=@{file}",
           #     "-F",
           #     f"caption={message}",
           #    ]
            #)
