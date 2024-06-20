import argparse
import logging
import sys

from .service import TSUT
from .utils import id_normalizer


async def perform():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i",
        "--link",
        help="The space link to download ."
    )

    parser.add_argument(
        "-c",
        "--cookie-file",
        help="""cookies file in the Netscape format. The specs of the
                            Netscape cookies format can be found here:
                            https://curl.se/docs/http-cookies.html. The cookies
                            file is now required due to the Twitter API change
                            that prohibited guest user access to Twitter API
                            endpoints on 2023-07-01.""",
    )

    parser.add_argument(
        "-b",
        "--bot-token",
        help="Telegram bot token."
    )

    parser.add_argument(
        "-C",
        "--channel-id",
        help="Telegram channel ID."
    )

    args = parser.parse_args()

    if args.link is None:
        logging.error("Error: space link has not been provided.")
        sys.exit(1)

    if args.cookie_file is None:
        logging.error("Error: twitter cookie file has not been provided.")
        sys.exit(1)

    if args.channel_id is None:
        logging.error("Error: channel id has not been provided.")
        sys.exit(1)

    if args.bot_token is None:
        logging.error("Error: bot token has not been provided.")
        sys.exit(1)

    channel_id = id_normalizer(args.channel_id)

    t = TSUT(args.bot_token, channel_id, args.link, args.cookie_file)
    await t.download_audio()
    await t.upload_to_telegram()


def run():
    import asyncio
    asyncio.run(perform())


if __name__ == "__main__":
    run()
