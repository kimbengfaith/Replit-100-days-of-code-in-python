# ROCK, PAPPER, SCISSORS
# Day 17 Challenge: Use a loop to repeat the game multiple rounds.
#Keep score of player 1 and player 2.
#End the game when a player wins three rounds using break and exit.
#Use continue to restart the round until one player wins three rounds.
#Your last bit of code should be the results of which player won.

from getpass import getpass as input # it ensures that whenever you use input, each player cannot see what the other typed in
rules=''' 
The following code is our very own rock, paper scissors game.
Make sure you folow the instructions bellow else you may not get any responce.
Rules:
Enter the following short forms bellow.
R or r = rock
S or s = scissors
P or P = papper
'''
print(rules)
print()
list_1=['R','r','P','p','S','s']

score1=0
score2=0
round=0
# while loop that checks if the score player1 or player2 has 3 points
while True:
  round +=1
  print("Round",round)
  if score1 == 3 or score2 == 3:
    break
  else:
    player1=input("Enter any of the above commands: ")
    player2=input("Enter any of the above comands: ")
    print()
    if player1 not in list_1 or player2 not in list_1:
      print('please enter a valid variable.\n')
      continue
      
    if player1 == player2:
      print("ITS a Draw!!")
      continue
      
    if player1 == 'R' or player1 == 'r':
      if player2 == 'S' or player2 == 's':
        score1 +=1
        print("Rock covers scissors. player1 wins.")
      else:
        score2+=1
        print("Paper covers rock. player2 wins.")
        
    elif player1 == 'P'or player1 == 'p':
      if player2 =='R' or player2 == 'r':
        score1+=1
        print("Paper covers rock player1 wins player 2 lose")
      else:
        score2+=1
        print("scissors cuts paper player2 wins")
        
    elif player1 == 'S'or player1 == 's':
      if player2 =='P' or player2 == 'p':
        score1+=1
        print("scissors cuts paper player1 wins")
      else:
        score2+=1
        print("Rock covers scissors player2 wins")
        
    elif player1 == player2:
      print("ITS a Draw!!")
      continue
      
if score1 ==3:
  print("player1 has a score of",score1,"and player2 has a score of",score2,"\n. Hence player 1 wins.")
  exit()
else:
  print("player1 has a score of",score1,"and player2 has a score of",score2,"\n. Hence player 2 wins.")