from playsound import playsound as play
import os
from os import listdir
from os.path import isfile, join
import random

musicFolder = input("enter your music path: ")
extensions = (".mp3", ".wav", ".ogg", ".flac")

onlyfiles = [f for f in listdir(musicFolder) if isfile(join(musicFolder, f))]
print("hi..")
print(onlyfiles)
random.shuffle(onlyfiles)
print(onlyfiles)

while True:
    for file in onlyfiles:
        if file.lower().endswith(extensions):
            file_path = os.path.join(musicFolder, file)
            print("Now playing " + file + " for you..")
            x = input("Press 1 to go to the next song: ")
            if x == "1":
                continue
            try:
                play(file_path)
            except Exception as e:
                print(f"An error occurred: {e}")
                input("press enter to continue..")
                continue
        else:
            print("Invalid music file: {file}")