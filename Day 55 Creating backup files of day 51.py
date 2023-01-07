# Day 55 creating backups
import time, os, random

to_do_list = []

file_exist = True

#auto load
try:
  file = open("to_do_list.txt","r")
  to_do_list = eval(file.read()) # eval function runs the code in the brackets and returns the working code.
  file.close()
except Exception as err:
  file_exist = False
  print("file does not exist")

def print_priority(priority):
  for row in to_do_list:
    if priority in row:
      for item in row:
        print(f"{item:^10}", end="  |  ")
      print("\n")
#prints out the enterer list
def print_list():
  print()
  for row in to_do_list:
    for item in row:
      print(f"{item:^10}", end ="  |  ")
    print("\n")

print("🌟Life Organizer🌟\n\n")
print("Welcome to the life organizer.\n\n")
print("Enter any of the following below\n")

while True:
  time.sleep(3)
  os.system("clear")
  menu = input("do you want to \n> Add \n> View \n> Remove \n> Edit \n").strip()

  # add a list of elements to our list
  if menu.lower() == "add":
    task = input("What is the task: ")
    date = input("When is it due: ")
    priority = input("What is the priority(high, meduim or low): ")
    row = [task, date, priority]
    to_do_list.append(row)
    print("Thanks your task has been added\n")
  # views the list
  elif menu.lower() == "view":
    print("Enter either \033[0;32mview all \033[0;255m or \033[0;32mview priority \033[0;255m \n")
    view_output = input("do you want to view all(shows the enterer list) or \nView priority(aloows you to search for meduim, high or low.) ").strip().lower()
    if view_output == "view all":
      print_list()
    elif view_output == "view priority":
      prio = input("what is the priority: ")
      print_priority(prio)
    else:
      print("\nplease enter the commands as instructed")
      
  # edits the list
  elif menu.lower() == "edit":
    item = input("What would you like to change: ")
    item_change = input("Enter the item: ")
    row_1 = int(input("Which row is the element found in? "))
    row_2 = row_1 -1
    if row_2 not in range(len(to_do_list)):
      print("hello the row you entered is not found in the list. please enter a valid row")
      continue
    if item not in to_do_list[row_2]:
      print("the item you entered is not found you can view the list to see the valid items")
      continue
    else:
      i = to_do_list[row_2].index(item)
      to_do_list[row_1-1][i] = item_change
      print("\n Thanks the task has been done.")
      
   # remove an enter row   
  elif menu.lower() == "remove":
    print("\nMake sure you have viewd the list to see if the row you want to remove exist")
    row_1 = int(input("what row number do you want to remove"))
    row_2 = row_1 - 1
    if row_2 not in range(len(to_do_list)):
      print("\nhello the row you entered is not found in the list. please enter a valid row")
      continue
    else:
      to_do_list.remove(to_do_list[row_1-1])
      print("\n you have succesfully removed an item")
  else:
    print("\nPlease enter the following commands above")
  
  ask = input("\ndo you want to see the menu or quit? > ")
  
# creating a backup
  if file_exist == True:
    try:
      os.mkdir("backups")
    except:
      pass
    name = f"backup{random.randint(1,1000000000)}.txt"
    file_name = os.path.join("backups/",name)
    f = open(file_name,"w")
    f.write(str(to_do_list))
    f.close()
    
   #auto save
  file = open("to_do_list.txt","w")
  file.write(str(to_do_list))
  file.close()
  
  
  if ask.lower() == "quit":
    break
  else:
    continue
 

