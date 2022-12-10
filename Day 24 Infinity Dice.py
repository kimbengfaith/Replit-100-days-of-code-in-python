#Day 24 Challenge: Create subroutines that will roll a dice with any number of sides (essentially as big of a number as you like). Write one subroutine with one parameter that allows us to call a function (such as rollDice).  
print("Welcome to infinity Dice\n Please enter the number of sides you will like your dice to have.")
def roll_dice(sides):
  import random
  while True: 
    rolled=random.randint(1, sides) 
    print("you rolled",rolled)
    print()
    roll_again=input("Do you want to roll again?:")
    if roll_again == 'yes':
      continue
    elif roll_again == 'no':
      break
number= int(input("How many sides?: "))
roll_dice(number)