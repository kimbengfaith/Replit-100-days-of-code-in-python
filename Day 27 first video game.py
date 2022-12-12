#Day 27 Challenge:
#Task: Welcome to your first video game creation. You will create a video game that creates a character's health and attack stats...along with an epic name for your character.
import os, time
import random

instructions="""
Enter the following instructions as below to see the healthstats and strenght starts of your favourite characters in the movies
"""
print(instructions)
time.sleep(3)
os.system("clear")
sides=int(input("How many sides does your dice have?: "))
# function that asks the user for the name and character type in cartoons
def firstname_chartype():
  firstname = input("Name your Legend:\n")
  print()
  chartype = input("Character type(Human, Elf,Wizard,Org):\n")
  print()
  return firstname
# function to determine the health statistics of your character
def health_stats(size):
  print(firstname_chartype())
  sided_roll= random.randint(1,size)
  healthstats = (6-sided_roll)*(12-sided_roll)/2 + 10
  return healthstats
# function to determine the strength statistics of your character
def stats_strenght(size):
  sided_roll= random.randint(1,size)
  statstrenght = (6-sided_roll)*(12-sided_roll)/2 + 12
  return statstrenght
# prints out the strenght and health stats of your character
want_to_continue="yes"
while want_to_continue == "yes":
  health = health_stats(sides)
  strenght = stats_strenght(sides)
  print("HEALTH:",int(health))
  print("STRENGTH:",int(strenght))
  want_to_continue=input("Do yo want to continue? ")
  if want_to_continue == 'yes':
    time.sleep(2)
    os.system("clear")
  elif want_to_continue == "no":
    break
  else:
    time.sleep(2)
    os.system("clear")
    

  
  
  