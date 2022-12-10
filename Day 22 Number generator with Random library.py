#Day 22 Challenge: Copy and paste your code from Day 18 to make a number generator.
#using the random library
import random
number = random.randint(1,1000000)
count=0
while True:
  guess= int(input("What is your guess: "))
  if guess<0:
    exit()
  elif guess < number:
    print("too low")
    count += 1
  elif guess > number:
    print("too high")
    count += 1
  elif guess == number:
    print("You're correct.")
    count += 1
    break
  print()
print("It took you",count,"attemps to guess correctly.")