import yt_dlp
yt_dlp.YoutubeDL({'format':'best','outtmpl':'%(title)S.%(ext)s'}).download([])