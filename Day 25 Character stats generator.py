#Day 25 Challenge:
#Task: Let's extend Day 24's project and create a health stats generator for a character in a video game.
#Name: Character stats generator
print("Lets play a game!!.\n In this game you are goin to see the health stats of your favourite characters by rolling a one six-sided and one eight-sided dice.\nThe health stats will be the multiplied value of the eight and the six dice you rolled.\nEnjoy!! the game. ")
import random
def roll_dice(size):
  number = random.randint(1,size)
  return number
dice_size= int(input("Enter any size of a dice: "))
num = roll_dice(dice_size)
#print(num)
def one_six_eight_dice(six_dice,eight_dice):
  num1= random.randint(1,six_dice)
  num2= random.randint(1,eight_dice)
  char_health= num1* num2
  return char_health
want_to_continue='yes'
while want_to_continue == 'yes':
  print()
  worrior=input("name your worrior: ")
  char_health = one_six_eight_dice(6,8) 
  print("Their health is:",str(char_health)+"hp")
  want_to_continue= input("Do you want to continue?: ")