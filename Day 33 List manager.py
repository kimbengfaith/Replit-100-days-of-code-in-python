#to do list manager
import time, os

print("Welcome to your list to do manager. You can only Add, View of Edit the list.")
print("Start building your that schedule a fitting them into a list.")
time.sleep(2)
os.system("clear")

# your list
Todo_list= []

#output list
def printlist():
  for item in Todo_list:
    print()
    print(f"\033[0;31m{item}\033[0;255m")
    print()
    
# Add elements to list
def Add():
  print()
  item = input("What do you want to add?: ")
  Todo_list.append(item)
  
# remove elements from list
def Remove():
  print()
  item = input("What do you want to remove?: ")
  if item in Todo_list:
    Todo_list.remove(item)
  else:
    print()
    print(f"\033[0;31m{item} \033[0;255mis not found in the list")

while True:
  instructions = input("Do you want to Stop, View, Add, Edit items from the list?: ")
  if instructions == 'View' or instructions == "view":
    printlist()
  elif instructions == "Add" or instructions == "add":
    Add()
  elif instructions == "Edit" or instructions == "edit":
    info = input("Do you want to add or remove elements?: ")
    if info == "Add" or info == "add":
      Add()
    elif info == "Remove" or info == "remove":
      Remove()
  elif instructions == "stop" or instructions == "Stop":
    break
  else:
    print("please enter either \033[0;32mEdit, \033[0;34mView, \033[0;35mAdd, \033[0;31mStop \033[0;255melemnts from the list.")
  time.sleep(1)
  os.system("clear")