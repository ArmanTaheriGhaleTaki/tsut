import subprocess
import glob
import ffmpeg
import math
import os

def download_audio(space_link, cookie_file):
    subprocess.run(["twspace_dl", "-i", space_link,"-c" ,cookie_file ,"-o","%(title)s;%(start_date)s;%(creator_name)s;%(creator_screen_name)s;" ])
    text= glob.glob('*.m4a')
    with open('output.txt', 'w') as file:
        for i in text:
            x=i.split(";")
            file.write(str(x[0])+'\n'+'\n'+str(x[3])+' ('+str(x[2])+')'+'\n'+'\n'+str(x[1])+'\n'+'\n'+'\n'+space_link)
            newname=str(x[0])
            os.rename(i,newname)
            split_audio(newname)

def split_audio(newname): # Added python-native ffmpeg library instead of calling it using executable


    probe = ffmpeg.probe(input_file)
    video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
    duration = float(video_info['duration'])

    # Calculate the number of segments
    num_segments = math.ceil(duration / segment_length)

    # Split the video
    for i in range(num_segments):
        start_time = i * segment_length
        end_time = start_time + segment_length
        output_file = f"{newname}_{str(i+1).zfill(3)}.m4a"

        # Use ffmpeg-python to split the video
        (
            ffmpeg
            .input(input_file)
            .output(output_file, ss=start_time, t=segment_length, c='copy')
            .run()
        )


#   subprocess.run(
#       [



            # "ffmpeg",
            # "-i",
            # newname,
            # "-f",
            # "segment",
            # "-segment_time",
            # "3600",
            # "-c",
            # "copy",
            # f"{newname}_%01d.m4a",
#      ]
#   )
