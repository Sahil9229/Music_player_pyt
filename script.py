from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
import sys
import os
from pygame import mixer
from mutagen.mp3 import MP3
import time
import threading

root=Tk()
mixer.init()   #initialize
               #root = menubar + leftframe + rightframe + statusbar

menu_bar=Menu(root)
root.config(menu=menu_bar)

root.geometry('600x260')
root.title("PLAyeR")

status_bar = Label(root,text='Welcome',relief  = SUNKEN, anchor = W) #west sunken border
status_bar.pack(side = BOTTOM, fill = X)   #pack automatically arranges widgets from top to bpttom in vertical manner


leftframe = Frame(root)
leftframe.pack(side = LEFT,padx = 30)

rightframe = Frame(root)
rightframe.pack()

topframe = Frame(rightframe)
topframe.pack()

length_bar=Label(topframe,text = 'length 00:00')
length_bar.pack(pady = 10)
current_time_bar=Label(topframe,text = 'time 00:00', relief = GROOVE)
current_time_bar.pack()


mid_frame = Frame(rightframe)  #relief = RAISED borderwidth =1
mid_frame.pack(padx = 10,pady = 10)

bottom_frame = Frame(rightframe)
bottom_frame.pack()


play_list = Listbox(leftframe)
#play_list.insert(0,'song1')      #index from 0,(index,element)
#play_list.insert(0,'song2') 
play_list.pack() 

def open_file():
    global filename
    filename = filedialog.askopenfilename()
    print(filename)
    add_to_playlist(filename)

index = 0 

def add_to_playlist(f):
    global index
    f = os.path.basename(f)
    play_list.insert(index,f)
    index +=1




add_btn = Button(leftframe, text = 'Add', command = open_file)
add_btn.pack(side = LEFT)
del_btn = Button(leftframe, text = 'Del')
del_btn.pack(side = LEFT)



def about_us():
    tkinter.messagebox.showinfo('About PLAyeR','Music player developed in python')


sub_menubar=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='File',menu=sub_menubar)
sub_menubar.add_command(label="Open",command = open_file)
sub_menubar.add_command(label="Exit",command=root.destroy)

sub_menubar=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Help',menu=sub_menubar)
sub_menubar.add_command(label="About",command=about_us)





#p1 = PhotoImage(file = 'headphones.png') 
#root.iconphoto(False, 'headphones.png')

#root.iconbitmap("play(1).png") #rawstring

#text=Label(root,text = 'Play something')
#text.pack()


global playing 
global paused
paused = False
playing = False

def start_count(t):
    global paused
    global playing
    current_time = 0

    while  t and mixer.music.get_busy():    #returns false when stop is pressed
        if playing:
            mins,secs = divmod(t,60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins,secs)
            current_time_bar['text'] = 'time ' + timeformat
            time.sleep(1) #seconds  
            print(timeformat)
            t -= 1




def show_details():
    global filename
    #text['text'] = os.path.basename(filename)
    file_data = os.path.splitext(filename)
    if file_data[1] == '.mp3':
        #mp3
        audio = MP3(filename)
        total_length = audio.info.length
    else:
        a = mixer.Sound(filename)
        total_length = a.get_length()
    mins,secs = divmod(total_length,60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins,secs)
    print(timeformat)
    length_bar['text'] = 'length ' + timeformat
    t1 = threading.Thread(target = start_count,args = (total_length,))     #tread for start_count()
    t1.start()
    #start_count(total_length)


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
        show_details()
       
     else:
      #print('not paused')
      open_file()
      try:
         mixer.music.load(filename)
         mixer.music.play()
         playing = True
         status_bar['text'] = 'Playing ' + os.path.basename(filename)
         show_details()
         print('PLAYED')
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
    length_bar['text'] = 'length 00:00'
    current_time_bar['text'] = 'time 00:00'
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


muted = False
vol = 0
def mute_music():
    global muted
    global vol
    if muted:
        volumebutton.configure(image = volume_photo)
        scale.set(vol)
        mixer.music.set_volume(vol) 
        muted = False
        
    else:
        vol = scale.get()
        mixer.music.set_volume(0)  
        scale.set(0)
        volumebutton.configure(image = mute_photo)
        muted = True



play_photo=PhotoImage(file = 'asset/play.png')
stop_photo=PhotoImage(file = 'asset/stop.png')
pause_photo=PhotoImage(file = 'asset/pause.png')
mute_photo=PhotoImage(file = 'asset/mute24.png')
volume_photo=PhotoImage(file = 'asset/volume24.png')




#labelphoto = Label(root,image = photo)
#labelphoto.pack()

playbutton = Button(mid_frame,image=play_photo,command = play_song)
playbutton.grid(row = 0, column = 0, padx = 10)                      #side = LEFT for pack()
stopbutton = Button(mid_frame,image=stop_photo,command = stop_song)
stopbutton.grid(row = 0, column = 2, padx = 10)
pausebutton = Button(mid_frame,image=pause_photo,command = pause_song)
pausebutton.grid(row = 0, column = 1, padx = 10)
volumebutton = Button(bottom_frame,image=volume_photo, command = mute_music)
volumebutton.grid(row = 1, column = 0, sticky = 'e', pady = 15)



scale = Scale(bottom_frame,from_ = 0,to = 100,orient = HORIZONTAL,command = set_vol)
scale.set(70)
scale.grid(row = 1, column = 1,sticky = 'n')  #pack automatically arranges widgets from top to bpttom in vertical manner



def on_Closing():
    stop_song()
    root.destroy()




root.protocol("WM_DELETE_WINDOW",on_Closing)  #way of communication
root.mainloop()

#import tkinter as tk
#c = 650
#window = tk.Tk()
#back = tk.Frame(width=700, height=c)
#back.pack()
#window.title("Notifications")
#window.iconbitmap("headphones.ico")
#window.mainloop()
