import youtube_dl

links = [line.strip() for line in open('input.txt')]

tmpdir = "output"

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '190',
    }],
    'noplaylist': True,
    'outtmpl': './output/%(title)s.%(ext)s',
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(links)
