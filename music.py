import yt_dlp

ydl_opts = {

    'format': 'bestaudio/best',

    'postprocessors': [

        {

            'key': 'FFmpegExtractAudio',

            'codec': 'mp3',

            'preferredquality': '192',

        }

    ],

}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=Ef9wB_IJ3kQ&list=RDEf9wB_IJ3kQ&start_radio=1&pp=ygURa2FuZSBicm93biBoZWF2ZW6gBwE%3D'])