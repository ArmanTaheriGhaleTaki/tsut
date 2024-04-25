import subprocess
import glob
import os

def download_audio(space_link, cookie_file):
    subprocess.run(["twspace_dl", "-i", space_link,"-c" ,cookie_file ,"-o","%(title)s;%(start_date)s;%(creator_name)s;%(creator_screen_name)s" ])
    text= glob.glob('*.m4a')
    with open('output.txt', 'w') as file:
        for i in text:
            x=i.split(";")
            file.write(str(x[0])+'\n'+'\n'+str(x[3])+'('+str(x[2])+')'+'\n'+'\n'+str(x[1])+'\n'+'\n'+'\n'+space_link)
            # newname=str(x[0])+".m4a"
            newname=str(x[0])
            os.rename(i,newname)
            split_audio(newname)

def split_audio(newname):
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            newname,
            "-f",
            "segment",
            "-segment_time",
            "3600",
            "-c",
            "copy",
            f"{newname}_%01d.m4a",
        ]
    )
