import subprocess

from pytube import YouTube
from urllib.parse import unquote


def download(url):
    print("Downloading video...")
    #unencode url
    videoId = url.split("watch?v=")[1]
    video_name = 'tmp/' + videoId + '.mp4'
    audio_name = 'tmp/' + videoId + '.mp3'
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename=video_name)
    print("Download finished!")
    print("Extracting audio...")
    subprocess.call(['ffmpeg', '-y', '-i', video_name, '-vn', '-acodec', 'libmp3lame', '-ab', '64k', audio_name], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    print("Extraction finished!")
    subprocess.call(['rm', video_name], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return audio_name
