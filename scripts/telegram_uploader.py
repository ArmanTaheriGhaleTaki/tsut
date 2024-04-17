import os
import subprocess
from telegram import Bot



def upload_to_telegram(bot_token, channel_id,directory):
    message = "test"
    telegram_bot = Bot(token=bot_token)
    for file in os.listdir(directory):
        if file.endswith('.m4a'):
           filepath = os.path.join(directory, file)
           subprocess.run(
              [
               "curl",
               "-s",
               "-X",
               "POST",
               f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",
               "-F",
               f"chat_id={CHAT_ID}",
               "-F",
               f"document=@{file}",
               "-F",               
               f"caption={message}",
              ]
    )
