import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize pygame mixer
pygame.init()
pygame.mixer.init()

# Globals
current_user = "A"
user_playlists = {"A": [], "B": []}
current_index = {"A": 0, "B": 0}

# Functions
def load_music(user):
    files = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
    if files:
        user_playlists[user] = list(files)
        current_index[user] = 0
        status_label.config(text=f"User {user} loaded {len(files)} songs.")

def play_music():
    playlist = user_playlists[current_user]
    if playlist:
        idx = current_index[current_user]
        pygame.mixer.music.load(playlist[idx])
        pygame.mixer.music.play()
        song_name = playlist[idx].split("/")[-1]
        status_label.config(text=f"User {current_user} playing: {song_name}")
    else:
        status_label.config(text=f"No songs loaded for User {current_user}.")

def pause_music():
    pygame.mixer.music.pause()
    status_label.config(text="Music paused.")

def unpause_music():
    pygame.mixer.music.unpause()
    status_label.config(text="Music resumed.")

def stop_music():
    pygame.mixer.music.stop()
    status_label.config(text="Music stopped.")

def next_song():
    if user_playlists[current_user]:
        current_index[current_user] = (current_index[current_user] + 1) % len(user_playlists[current_user])
        play_music()

def previous_song():
    if user_playlists[current_user]:
        current_index[current_user] = (current_index[current_user] - 1) % len(user_playlists[current_user])
        play_music()

def switch_user():
    global current_user
    current_user = "B" if current_user == "A" else "A"
    status_label.config(text=f"Switched to User {current_user}")

# GUI
root = tk.Tk()
root.title("🎵 Two-User Music Player")
root.geometry("600x400")  # Rectangular size
root.configure(bg="#f2f2f2")

title = tk.Label(root, text="🎧 Python Music Player", font=("Arial", 18, "bold"), bg="#f2f2f2")
title.pack(pady=10)

# Frame for Load Buttons
frame_top = tk.Frame(root, bg="#f2f2f2")
frame_top.pack(pady=5)

tk.Button(frame_top, text="🎵 Load Playlist A", width=20, command=lambda: load_music("A")).grid(row=0, column=0, padx=20, pady=5)
tk.Button(frame_top, text="🎵 Load Playlist B", width=20, command=lambda: load_music("B")).grid(row=0, column=1, padx=20, pady=5)

# Frame for Music Controls
frame_controls = tk.Frame(root, bg="#f2f2f2")
frame_controls.pack(pady=15)

tk.Button(frame_controls, text="▶️ Play", width=15, command=play_music).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_controls, text="⏸️ Pause", width=15, command=pause_music).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_controls, text="▶️ Unpause", width=15, command=unpause_music).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_controls, text="⏹️ Stop", width=15, command=stop_music).grid(row=1, column=1, padx=5, pady=5)

# Frame for Navigation
frame_nav = tk.Frame(root, bg="#f2f2f2")
frame_nav.pack(pady=10)

tk.Button(frame_nav, text="⏮️ Previous", width=15, command=previous_song).grid(row=0, column=0, padx=10)
tk.Button(frame_nav, text="⏭️ Next", width=15, command=next_song).grid(row=0, column=1, padx=10)
tk.Button(frame_nav, text="🔁 Switch User", width=15, command=switch_user).grid(row=0, column=2, padx=10)

# Status Label
status_label = tk.Label(root, text="Welcome! Load playlists to begin.", font=("Arial", 12), bg="#f2f2f2", fg="green")
status_label.pack(pady=20)

root.mainloop()
