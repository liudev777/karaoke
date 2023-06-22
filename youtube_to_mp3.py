import time
from pytube import YouTube
from spleeter.separator import Separator
import os

def convert_youtube_to_mp3():
    try:
        yt = YouTube(str(input("Enter youtube URL:\n>> ")))
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path="assets")

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        
        os.rename(out_file, new_file)
        print(yt.title + " successfully converted")
        return new_file

    except Exception as e:
        print("Something went wrong")
        print(e)
    

if __name__ == '__main__':
    new_file = convert_youtube_to_mp3()
    separator = Separator('spleeter:2stems') # Initialize Spleeter separator
    time.sleep(1)
    separator.separate_to_file(f'{new_file}', 'output') # Separate the audio