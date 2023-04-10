import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os

root = Tk()
root.title("FoxJox Player")
root.geometry("485x700+100+10")
root.configure(background="#333333")
root.resizable(False, False)

def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

    for song in songs:
        if song.endswith(".mp3"):
            Playlist.insert(END, song)


bottom_frame = Frame(root, bg="#FFFFFF", width=485, height=180)
bottom_frame.place(x=0, y=400)

logo = PhotoImage(file="logo.png")
root.iconphoto(False, logo)

Menu = PhotoImage(file = "")
Label(root, image= Menu).place(x=0, y=580, width=485, height=100)
frame_music = Frame(root, bd = 2, relief=RIDGE)
frame_music.place(x=0,y=585, width=485, height=100)
Button(root, text="Browse Music", width=59, height=1, font=("calibri", 12, "bold"), fg="black", bg="#FFFFFF", command = AddMusic).place(x=0,y=550))
Scrollbar(frame_music)




root.mainloop()