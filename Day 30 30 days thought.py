#Day 30 Challenge
#Task: Create a program that uses a loop that asks the user what they have thought of each of the 30 days of challenges so far.
import time, os
info="""We are now day 30 on the 100 days of code on replit and for each day you will write what you felt after completing a lesson.\n"""
print(f"{info:^100}")
time.sleep(3)
os.system("clear")
print("30 Days Down")
for day in range(1,31):
  print(f"Day {day}:")
  thought=input()
  print()
  statement = f"You thought Day {day} was {thought}"
  print(f"{statement:^39}")
  time.sleep(3)
  os.system("clear")
  
  