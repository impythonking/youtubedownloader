from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("YouTube video downloader")

link = StringVar()

Label(root, text = 'Paste Youtube Video Link:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 55,textvariable = link).place(x = 32, y = 90)

def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'Download Done.', font = 'arial 15').place(x= 180 , y = 210)

Button(root,text = 'Download Now', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()