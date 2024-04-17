from scripts.telegram_uploader import upload_to_telegram
from scripts.twitter_space_downloader import download_audio
from scripts.config import bot_token, chat_id


def main():

    download_audio(space_link, cookie_file)

    upload_to_telegram(bot_token, chat_id, ".")


if __name__ == "__main__":
    main()
