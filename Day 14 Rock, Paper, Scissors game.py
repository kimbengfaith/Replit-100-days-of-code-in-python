# ROCK, PAPPER, SCISSORS
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
player1=input("Enter any of the above commands: ")
player2=input("Enter any of the above comands: ")
print()
if player1 == 'R' or player1 == 'r':
  if player2 == 'S' or player2 == 's':
    print("Rock covers scissors. player1 wins.")
  else:  
    print("Paper covers rock. player2 wins.")
    
elif player1 == 'P'or player1 == 'p':
  if player2 =='R' or player2 == 'r':
    print("Paper covers rock player1 wins player 2 lose")
  else:  
    print("scissors cuts paper player2 wins")
    
elif player1 == 'S'or player1 == 's':
  if player2 =='P' or player2 == 'p':
    print("scissors cuts paper player1 wins")
  else:
    print("Rock covers scissors player2 wins")
    
elif player1 == player2:
  print("ITS a Draw!!")
else:
  print('please see the rules above and enter the right commands.')