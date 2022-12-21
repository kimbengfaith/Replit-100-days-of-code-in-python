import random,time,os

def printcard():
  print()
  for row in bingo_card:
    for number in row:
      print(f"{number: ^10}",end=" | ")
    print()

#checks if you guess the correct number or not
def prettyprint():
  time.sleep(1)
  os.system("clear")
  count = 0
  for row in bingo_card:
    for number in row:
      print()
      guess = int(input("Guess the number: "))
      if guess in row:
        count +=1
        i = row.index(number)
        row[i] = "x"
        # prints the card after each guess
        printcard()
      else:
        # prints the card after each guess
        printcard()
        continue
  # outputs the bingo card and checks if you have won or lost the game
  print()
  for row in bingo_card:
    for number in row:
      print(f"{number: ^10}",end=" | ")
    print()
  if count == 8:
    print("\n\033[0;34mYou have won")
  else:
    print("\n\033[0;31mYou have lost")   
      
#creates the bingo card      
number = []
for i in range(8):
  num = random.randint(0,90)
  number.append(num)
number.sort()
bingo_card= [[number[0],number[1], number[2]],
             [number[3],"Bingo",number[4]],
             [number[5],number[6],number[7]]
            ]

prettyprint()