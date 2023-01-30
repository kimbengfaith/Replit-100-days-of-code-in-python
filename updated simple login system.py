# Day 71: Simple Login system
from replit import db

import random,os,time
  
def add():
  time.sleep(2)
  os.system("clear")
  username = input("Enter your username: ")
  if username in db.keys():
    print("This username already exists")
  else:
    password = input("Enter your password: ")
    salt = random.randint(1000,9999)
    newpassword = f"{password}{salt}"
    newpassword = hash(newpassword)
    db[username]={"password":newpassword,"salt":salt}
    print("Login added")


def login():
  time.sleep(2)
  os.system("clear")
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  key = list(db.keys())
  
  if username in key:
    
    newpassword = f"{password}{db[username]['salt']}"
    newpassword = hash(newpassword)
    
    if newpassword == db[username]['password']:
      print("Login successful")
  else:
    print("password or username incorrect")

print("\033[0;32mLogin System\033[0;255m\n")

while True:
  
  menu = input("1: Add user \n2: Login \n>")
  if menu == "1":
    add()

  elif menu == "2":
    login()
    
  else:
    print("please enter a valid menu")

  ask = input("Would you like to quit yes/no ")
  if ask[0] == "y":
    break

  time.sleep(2)
  os.system("clear")