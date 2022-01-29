#somecode
from tkinter import *
from pytube import YouTube
from tkinter import messagebox as mb
root = Tk()




def dialog():
    if entry.get() == '':
        mb.showerror('Error', 'You must enter url!')
    else:
        yt = YouTube(entry.get())
        v = yt.streams.get_highest_resolution()
        v.download(filename='video.mp4')

        mb.showinfo(title='Video info', message=f'Video downloaded successfully. Info: Title {yt.title}, Description {yt.description}, Channel url: {yt.channel_url}, Publish date: {str(yt.publish_date)}, Thumbnail url: {yt.thumbnail_url}.')


root.title('YouTube Video Info')
text = Label(width=40, text='Enter here video url and click Get data from video')
entry = Entry(width=10)
btn = Button(width=20, text='Get data from video', command=dialog)

text.pack()
entry.pack()
btn.pack()


root.mainloop()