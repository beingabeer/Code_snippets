#!/home/beer/anaconda3/bin/python
from pydub import AudioSegment
from pydub.playback import play
import os
import time
import random

# Change the current working directory to scripts location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


# Create list of files in the directory (all mp3's have to be in the folder)
music_list = []
file_list = os.listdir()
for audioFile in full_list:
    if 'mp3' in audioFile:
        music_list.append(audioFile)

# Remove songs from playlist
music_list.remove(sample_one)
music_list.remove(sample_two)

# Make a separate playlist
playlist2 = []
for file in os.listdir():
    if 'music_1' in file or 'music_2' in file:
        playlist2.append(file)


# Play songs
song = AudioSegment.from_mp3('music_file.mp3')
play(song)


# Play first random song
first_random_song = random.choice(music_list)
song = AudioSegment.from_mp3(first_random_song)
play(song)

# Remove first random song from music playlist
music_list.remove(first_random_song)

# Play second random song (should not be first_random_song)
second_random_song = random.choice(music_list)
song = AudioSegment.from_mp3(second_random_song)
play(song)
