import subprocess


def download_audio(space_link, cookie_file):
    subprocess.run(["twspace_dl", "-i", space_link,"-c" ,cookie_file ,"-o","%(title)s%(start_date)s" ])


def split_audio(space_link):
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            space_link,
            "-f",
            "segment",
            "-segment_time",
            "3600",
            "-c",
            "copy",
            f"{space_link}%01d.m4a",
        ]
    )
