#day 48 challenge: here am going to learn how to create a file and write to it in python

import time, os
print("🌟HIGH SCORE TABLE�\n")

f = open("high score.txt", 'a+')
while True:
  initials = input("input 3 letter initail > ")
  score = input("Enter score: ")
  f.write(f"{initials} {score}\n")
  print("Added to high score table")
  question = input("do you want to add another(yes or no)? ")
  
  if question.lower()== "no":
    f.close()
    break
  time.sleep(2)
  os.system("clear")
  
  