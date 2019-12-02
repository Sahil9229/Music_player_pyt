from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
import sys
import os
from pygame import mixer

root=Tk()
mixer.init()   #initialize

menu_bar=Menu(root)
root.config(menu=menu_bar)

def about_us():
    tkinter.messagebox.showinfo('About PLAyeR','Music player developed in python')

def open_file():
    global filename
    filename = filedialog.askopenfilename()
    print(filename)
sub_menubar=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='File',menu=sub_menubar)
sub_menubar.add_command(label="Open",command = open_file)
sub_menubar.add_command(label="Exit",command=root.destroy)

sub_menubar=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Help',menu=sub_menubar)
sub_menubar.add_command(label="About",command=about_us)




root.geometry('300x300')
root.title("PLAyeR")
#p1 = PhotoImage(file = 'headphones.png') 
#root.iconphoto(False, 'headphones.png')

#root.iconbitmap("play(1).png") #rawstring
text=Label(root,text = 'noise')
text.pack()
global playing 
global paused
paused = False
playing = False
def play_song():
    volume=scale.get()
    mixer.music.set_volume(volume/100)
    global playing
    global paused
    if playing:
        #print('playing')
        mixer.music.rewind()
    else:
     #print('no song')
     if paused:
        print('unpausing')
        playing = True
        paused = False
        mixer.music.unpause()
        status_bar['text'] = 'Playing ' + os.path.basename(filename)
       
     else:
      #print('not paused')
      open_file()
      try:
         mixer.music.load(filename)
         mixer.music.play()
         playing = True
         status_bar['text'] = 'Playing ' + os.path.basename(filename)
      except:
         tkinter.messagebox.showinfo('PLAyeR','open a song first')
    
        
    #print('OK fine')
def stop_song():
    global playing
    global paused
    paused = False
    playing = False
    mixer.music.stop()
    status_bar['text'] = 'Music Stopped'
    #print()
def pause_song():
   global paused
   global playing
   if playing:  
    paused = True
    playing = False
    mixer.music.pause()
    status_bar['text'] = 'Music Paused'
def set_vol(val):
    volume = int(val)/100
    mixer.music.set_volume(volume)  #0 to 1

play_photo=PhotoImage(file = 'asset/play.png')
stop_photo=PhotoImage(file = 'asset/stop.png')
pause_photo=PhotoImage(file = 'asset/pause.png')


#labelphoto = Label(root,image = photo)
#labelphoto.pack()

playbutton = Button(root,image=play_photo,command = play_song)
playbutton.pack()
stopbutton = Button(root,image=stop_photo,command = stop_song)
stopbutton.pack()
pausebutton = Button(root,image=pause_photo,command = pause_song)
pausebutton.pack()


scale = Scale(root,from_ = 0,to = 100,orient = HORIZONTAL,command = set_vol)
scale.set(70)
scale.pack()

status_bar = Label(root,text='Welcome',relief  = SUNKEN, anchor = W) #west sunken border
status_bar.pack(side = BOTTOM, fill = X)

root.mainloop()

#import tkinter as tk
#c = 650
#window = tk.Tk()
#back = tk.Frame(width=700, height=c)
#back.pack()
#window.title("Notifications")
#window.iconbitmap("headphones.ico")
#window.mainloop()
