#Day 28 Challenge:
#Task: Use Day 27's character generator for this project...to build an automated game battle system!
import os, time
import random

instructions="""
Welcome to the Battle for you life Game wher Two of your best characters either in 
Cartoons or in movies will be battling against one another.

The instructions is as follows...

- The 2 characters will need to roll a 6 sided dice each
- if the first character wins his health remains thesame and the the health of the second character 
will be subtracted by the difference in their strenghts.and vice versa
- Note of they Both have thesame dice roll they are both moving on to the next round.
- the status of Both characters will be pasted after each round.

Enjoy!! and may the Best of the Best Win
"""
print(instructions)
time.sleep(10)
os.system("clear")
# number of sides the dice have
sides = 6

# function that asks the user for the name and character type in cartoons
def firstname_chartype():
  firstname = input("Name your Legend:\n")
  print()
  chartype = input("Character type(Human, Elf,Wizard,Org,...):\n")
  print()
  return firstname
  
# function to determine the health statistics of your character
def health_stats(size):
  sided_roll= random.randint(1,size)
  healthstats = (6-sided_roll)*(12-sided_roll)/2 + 10
  return healthstats,sided_roll
  
# function to determine the strength statistics of your character
def stats_strenght(size):
  sided_roll= random.randint(1,size)
  statstrenght = (6-sided_roll)*(12-sided_roll)/2 + 12
  return statstrenght
# prints out the strenght and health stats of your character
# character 1
  
name1 = firstname_chartype()
health1,roll1 = health_stats(sides)
strenght1 = stats_strenght(sides)
print("HEALTH:",int(health1))
print("STRENGTH:",int(strenght1))
print()
print("Who are they battling with?")
print()

  # Character 2
name2 = firstname_chartype()
health2,roll2 = health_stats(sides)
strenght2 = stats_strenght(sides)
print("HEALTH:",int(health2))
print("STRENGTH:",int(strenght2))

# returns back to the original
time.sleep(2)
os.system("clear")

# difference bet the strenght of lossers
round =0
while True:
  amount = abs(strenght2 - strenght1)
  # the game depends on the amount(difference between the strenghts of players)
  # if the both have same strenghts the game remains constant
  # we need to check if the game is constant or not
  # checks if the ammount is the 0 0r not
  if amount == 0:
    strenght1 = stats_strenght(sides)
    strenght2 = stats_strenght(sides)
  round += 1
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The battle begins!")
  print()
  print("Round",round)
  print()
  
  health,roll1= health_stats(sides)
  health,roll2 = health_stats(sides)
  
  #checks if the first character has the greatest dice roll
  if roll1 > roll2:
    if round == 1:
      health2 -= amount
      print(name1,"wins the blow",name2,"takes a hit with",amount,"damage")
    else:
      health2 -= amount
      print(name1,"wins round",round,name2,"takes a hit with",amount,"damage")
      
  #Checks if the second character has the greatest dice roll  
  elif roll2 > roll1:
    if round == 1:
      health1 -= amount
      print(name2,"wins the blow",name1,"takes a hit with",amount,"damage")
    else:
      health1 -= amount
      print(name2,"wins round",round,name1,"takes a hit with",amount,"damage")
      
    # when both characters have thesame dice roll
  elif roll1 == roll2:
        print("Wow,They are both having thesame dice roll")
    
  # prints out status of the 2 characters after each battle 
  print()
  print(name1)
  print("HEALTH:",int(health1),"\n")
  print()
  print(name2)
  print("HEALTH:",int(health2),"\n")
  
  #Checks if any of them has lost
  if health1 > 0 and health2 <= 0:
      print("oh no",name1,"died!","\n")
      print(name1,"destroyed",name2,"in",round,"rounds!")
      break
    
  elif health2 > 0 and health1 <= 0:
      print("oh no",name1,"died!")
      print(name2,"destroyed",name1,"in",round,"rounds!")
      break
    
  print("And they're both standing for the next round!")
  time.sleep(10)
  os.system("clear")