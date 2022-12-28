#Day 50 challenge
import random, os, time
print("🌟Idea Storage �")
i = 1
while True:
  time.sleep(2)
  os.system("clear")
  f = open("my.ideas","a+")
  question = input("Do you want to see a random idea or add an idea a/r? ").strip().lower()
  if question[0] == 'a':
    idea = input("What would you like to add? ")
    f.write(f'{i}: {idea}\n')
    i +=1
    print("\n Nice! your idea has been added")
    f.close()
    
  elif question[0] == "r":
    f = open("my.ideas","r")
    idea = f.read().split("\n")
    any_idea = random.choice(idea)
    print(f"\n{any_idea}")
    
    
