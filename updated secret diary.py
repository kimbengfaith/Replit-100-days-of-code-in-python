# Update secret diary

from replit import db
import datetime,os,random

def add():
  item = input("what will you like to add: ")
  timestamp = datetime.datetime.now()
  db[timestamp] = item
  print("your item has been added ")

def view():
  keys = list(db.keys())
  keys.sort()
  keys.reverse()
  for key in keys:
    os.system("clear")
    if key != username:
      print(f"{key}:{db[key]}")
    ask = input("\nwould you like to see the next? yes/no: ").lower()
    if ask[0] == "y":
      if key == keys[-1]:
        print("\033[1;35m\nyou have viewed everything on the diary\n\033[0;255m")
        break
      else:
        print()
        continue
    else:
      break
    
def main():
  while True:
   os.system("clear")
   menu = input("\nEnter the following numbers below \n1: Add to diary \n2:View diary entries \n> ")
   if menu == "1":
     add()
   elif menu == "2":
     view()
   ask = input("continue? yes or no: ").lower()
   if ask[0] == "y":
     continue
   else:
     break
     

if len(db.keys())<1:
  print("Create a new account")
  username = input("username: ")
  password = input("Password: ")
  salt = random.randint(1000,9999)
  password = f"{password}{salt}"
  password = hash(password)
  db[username] = {'password':password,"salt":salt}
  main()
else:
  username = input("Enter your username: ")
  if username in db.keys():
    password = input("Enter the diary Password: ")
    password = f"{password}{db[username]['salt']}"
    password = hash(password)
    if password == db[username]['password']:
      main()
    else:
      print("password incorrect")
  else:
    print("username incorrect")