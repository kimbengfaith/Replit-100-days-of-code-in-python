#Day 18 Challenge:We are going to build a "Guess the Number" guessing game.

number = 900
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