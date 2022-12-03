#Day 20 Challenge:Ask the user to list a starting number, ending number, and increment to use. Display an answer based on the users' answers 

start = int(input("Enter a starting number: "))
stop= int(input("enter a stop number: "))
increment = int(input("enter an increment number: "))
for number in range(start,stop,increment):
  print(number)