# Day 61 challenge: creating a one person tweet

from replit import db
import datetime,os, time


def view():
  i = 1
  keys = list(db.keys())
  keys.sort()
  keys.reverse()
  for key in keys:
    if len(keys) < 10:
      print(f"{key}: {db[key]}")
    else:
      if i%11 == 0:
        menu = input("Next 10? ")
        if menu[0] == "y":
          os.system("clear")
          print(f"{key}: {db[key]}")
        else:
          break
      else:
        print(f"{key}: {db[key]}")
    i += 1
        
    
while True:
  time.sleep(2)
  os.system("clear")
  print("Tweeter\n")
  menu = input("1: Add tweets \n2: View tweets \n>")
  if menu == "1":
    tweet = input("enter your tweet: ")
    timestamp = datetime.datetime.now()
    db[timestamp] = tweet
    print("\n Tweet has been added")
  elif menu == "2":
    view()
  else:
    print("enter as instructed in the above menu")
  ask = input("would you like to see the menu? \n1: yes \n>")
  if ask == "1":
    continue
  else:
    break


