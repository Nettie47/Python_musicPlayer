"""
Program: music_Player.py
Author: Nanette
3/9/26
*** MUST INSTALL PYGAME-CE before running thos app!!!!!!!!***
at command promp / terminal run : python3 -m pip install pygame-ce

Simple command-line based music player that can play a standard.mp3 audio file from their computer. 
"""

import pygame
import os

# Initialize the mixer module from pygame
pygame.mixer.init()

# display a menu for our user interface 
print("\nWelcome to the Python Music Player!")
print("Enter 1 to select a song file.")
print("Enter 2 to begin playing the chosen song.")
print("Enter 3 to pause an active song.")
print("Enter 4 to unpause the song.")
print("Enter any other key to exit the program. ")

# Loop and logic statements that determine which option was entered and what to do
while True:
    fileDir = os.path.dirname(os.path.abspath(__file__))
    
    menuChoice = input("Please select a menu option >>").strip()
    # Decision making that triggers the various features
    if menuChoice == "1":
        songFile = input("Please enter the song's filename>>")
        filePath = os.path.join(fileDir, songFile)
        pygame.mixer.music.load(filePath)
        print(f"Song {songFile} loaded successfully!")
    elif menuChoice == "2":
        pygame.mixer.music.play()
    elif menuChoice =="3":
        pygame.mixer.music.pause()
    elif menuChoice =="4":
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.stop()
        input("\nThank you for using the music player. Press Enter to exit.")
        break