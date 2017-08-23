import youtube_dl
import time

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '128',
    }]
}

t_start = time.time()

y_video_list = ['https://www.youtube.com/watch?v=lIES3ii-IOg',
                'https://www.youtube.com/watch?v=JlqV-kSS0lQ',
                'https://www.youtube.com/watch?v=m8RtlqFgiG8',
                'https://www.youtube.com/watch?v=pcHNc5Ql21o',
                'https://www.youtube.com/watch?v=YCV3Cu73hRk']
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #ydl.download(['https://www.youtube.com/watch?v=bypGsd527dM'])
    ydl.download(y_video_list)

t_end = time.time()
print(t_end - t_start)