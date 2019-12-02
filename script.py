from tkinter import *
import sys
import os
from pygame import mixer

root=Tk()
mixer.init()   #initialize


root.title("PLAyeR")
#p1 = PhotoImage(file = 'headphones.png') 
#root.iconphoto(False, 'headphones.png')

#root.iconbitmap("headphones.ico") #rawstring
text=Label(root,text = 'noise')
text.pack()

def play_song():
    mixer.music.load('asset/Alan_Walker_Ft_Sabrina_Carpenter_Farruko_-_On_My_Way.mp3')
    mixer.music.play()
    #print('OK fine')
def stop_song():
    mixer.music.stop()
    #print()
play_photo=PhotoImage(file = 'asset/play.png')
stop_photo=PhotoImage(file = 'asset/stop.png')
#labelphoto = Label(root,image = photo)
#labelphoto.pack()

playbutton = Button(root,image=play_photo,command = play_song)
playbutton.pack()
stopbutton = Button(root,image=stop_photo,command = stop_song)
stopbutton.pack()

root.mainloop()

#import tkinter as tk
#c = 650
#window = tk.Tk()
#back = tk.Frame(width=700, height=c)
#back.pack()
#window.title("Notifications")
#window.iconbitmap("headphones.ico")
#window.mainloop()
