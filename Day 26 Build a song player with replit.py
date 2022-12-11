#Day 26 Challenge
#Task: Play a song from this repl and build a menu to go with it. Make it look like an iPod!
from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    stop_playback = int(input("Press 2 anytime to stop playback and go back to the menu : "))
    if stop_playback == 2:
      source.paused = True
      return
    else:
      continue
while True:
  # clear the screen 
  os.system("clear")
  # Show the menu
  print("🎵 MyPOD Music Player")
  print(""" 
   Press 1 to Play
   Press 2 to Exit

   Press anything else to see the menu again.
   """)
  time.sleep(1)
  # take user's input
  press=int(input("Select any of the above instructions: "))
  # check whether you should call the play() subroutine depending on user's input
  if press == 1:
    play()
  elif press == 2:
    exit()
  else:
    continue