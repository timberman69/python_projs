import tkinter as tk
from tkinter import font
import youtube_dl
# Download Video
def download_video(entry):
    ydl_opts = {
        'format': '22',
    
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([entry])
        lable['text'] = 'Downloading...'
    ret = lable['text'] = 'Downloaded'
    return ret
# Download Audio
def download_audio(entry):
    ydl_opts = {
        'format': '140',
    
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([entry])
        lable['text'] = 'Downloading...'
    ret = lable['text'] = 'Downloaded'
    return ret

root = tk.Tk()

canvas = tk.Canvas(root, height = 630, width = 1100, bg = '#232323')
canvas.pack()

#frame in which all the contents are located
frame = tk.Frame(root, bg = '#232323')
frame.place(relwidth = 1, relheight = 1)

# Download button mp4
button = tk.Button(frame, text = "Download Video", bg = '#a367ff', fg = '#fff', command=lambda : download_video(entry.get()), font =('courier', 12))
button.place(relx = 0.8, rely = 0.26, relwidth = 0.14, relheight = 0.080)

# Download button audio
button = tk.Button(frame, text = "Download M4a", bg = '#a367ff', fg = '#fff', command=lambda : download_audio(entry.get()), font =('courier', 12))
button.place(relx = 0.8, rely = 0.35, relwidth = 0.14, relheight = 0.080)

# Url Entry Box
entry = tk.Entry(frame, bg = '#989898', fg = '#fff', font =('courier', 12))
entry.place(relx = 0.04, rely = 0.26, relwidth = 0.75, relheight = 0.080)

# Staus of Downloaded and Downloading
lable = tk.Label(frame, text = '', bg = '#989898', fg = '#fff', font =('courier', 12))
lable.place(relx = 0.04, rely = 0.38, relwidth = 0.5, relheight = 0.08)

root.mainloop()

#'postprocessor': [{
#           'key': 'FFmpegExtractAudio',
#            'preferredcodec': 'mp3',
#            'preferredquality': '120'
#        }]