import os
import subprocess
def upload_to_telegram(bot_token, channel_id,directory):
    with open('output.txt', 'r') as desc:
        message = desc.read()
    for file in os.listdir(directory):
        if file.endswith('m4a'):
           print(file)
           filepath = os.path.join(directory, file)
           subprocess.run(
              [
               "curl",
               "-s",
               "-X",
               "POST",
               f"https://api.telegram.org/bot{bot_token}/sendDocument",
               "-F",
               f"chat_id={channel_id}",
               "-F",
               f"document=@{file}",
               "-F",               
               f"caption={message}",
              ]
    )
