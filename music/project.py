from tkinter import *
from tkinter import filedialog
from pygame import mixer
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Music Player")
root.geometry("920x670+20+85")
root.configure(bg="#ffffff")

mixer.init()
playlist_songs = []
current_index = 0

def open_folder():
    global playlist_songs
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = [song for song in os.listdir(path) if song.endswith(".mp3")]
        playlist_songs = songs
        playlist.delete(0, END)
        for song in songs:
            playlist.insert(END, song)

def play_song(index=None):
    global current_index
    if index is None:
        index = playlist.curselection()
        if not index:
            return
        current_index = index[0]
    song = playlist_songs[current_index]
    mixer.music.load(song)
    mixer.music.play()
    playlist.selection_clear(0, END)
    playlist.selection_set(current_index)

def next_song():
    global current_index
    if current_index < len(playlist_songs) - 1:
        current_index += 1
        play_song(current_index)

def previous_song():
    global current_index
    if current_index > 0:
        current_index -= 1
        play_song(current_index)

def change_volume(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)

# Top design and logo
top = PhotoImage(file="images/top.png")
Label(root, image=top, bg="#FFFFFF").pack()

logo = PhotoImage(file="images/logo.png")
Label(root, image=logo, bg="#FFFFFF").place(x=65, y=110)

# Buttons
play_img = PhotoImage(file="images/play.png")
Button(root, image=play_img, bg="#FFFFFF", bd=0, command=play_song).place(x=100, y=400)

stop_img = PhotoImage(file="images/stop.png")
Button(root, image=stop_img, bg="#FFFFFF", bd=0, command=mixer.music.stop).place(x=30, y=500)

resume_img = PhotoImage(file="images/resume.png")
Button(root, image=resume_img, bg="#FFFFFF", bd=0, command=mixer.music.unpause).place(x=115, y=500)

pause_img = PhotoImage(file="images/pause.png")
Button(root, image=pause_img, bg="#FFFFFF", bd=0, command=mixer.music.pause).place(x=200, y=500)

next_img = PhotoImage(file="images/next.png")  # Add this image to your 'images' folder
Button(root, image=next_img, bg="#FFFFFF", bd=0, command=next_song).place(x=160, y=400)

prev_img = PhotoImage(file="images/previous.png")  # Add this image to your 'images' folder
Button(root, image=prev_img, bg="#FFFFFF", bd=0, command=previous_song).place(x=40, y=400)

menu = PhotoImage(file="images/menu.png")
Button(root, image=menu, bg="#FFFFFF").pack(padx=10, pady=50, side=RIGHT)

# Open folder button
Button(root, text="Open Folder", width=15, height=2, command=open_folder,
       font=("arial", 10, "bold"), fg="Black", bg="#21b3de").place(x=330, y=300)

# Frame for playlist
frame = Frame(root, bd=2, relief=RIDGE)
frame.place(x=330, y=350, width=560, height=250)

scroll = Scrollbar(frame)
scroll.pack(side=RIGHT, fill=Y)

playlist = Listbox(frame, width=80, height=15, font=("arial", 10),
                   bg="#333333", fg="grey", bd=0, cursor="hand2", yscrollcommand=scroll.set)
playlist.pack(side=LEFT, fill=BOTH)
scroll.config(command=playlist.yview)

# Volume slider
Label(root, text="Volume", bg="white", font=("arial", 10, "bold")).place(x=330, y=620)
volume_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=change_volume, bg="white")
volume_slider.set(70)  # default volume
volume_slider.place(x=400, y=600)

root.mainloop()
