import IPython.display as ipd
from IPython.core.interactiveshell import InteractiveShell
import os

def download_song(song_id):
    '''downloads the sond using spotdl python package (pip install spotdl)'''
    song_url = 'https://open.spotify.com/track/' + song_id
    os.system(f"spotdl {song_url} --format mp3 --output {{track-id}}")

def play_song(song_id, album_url):
    '''displays image in cell output'''
    image = ipd.Image(url=album_url)
    ipd.display(image)

    '''displays audio widget in the same cell'''
    sample_rate = 44100 # mandatory
    audio_path = song_id + '.mp3'
    audio = ipd.Audio(filename=audio_path, rate=sample_rate)
    ipd.display(audio)
