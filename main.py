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

bottom_frame = Frame(root, bg="#FFFFFF", width=485, height=180)
bottom_frame.place(x=0, y=400)
root.mainloop()