from __future__ import unicode_literals
import youtube_dl

options = {
    'list-formats': True,
    'format': 'best audio', # choice of quality
    'extractaudio' : True,      # only keep the audio
    'audioformat' : "mp3",     # convert to best possible 
    'outtmpl': '%(title)s.%(ext)s',        # name the file the ID of the video
    'noplaylist' : True,        # only download single song, not playlist
}

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(['https://youtu.be/xudtBUqmswg'])
