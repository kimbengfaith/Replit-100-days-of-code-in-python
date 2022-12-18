#Day 35 Challenge: Advanced Todolist.

import os, time
print("Welcome to todays to do list please enter the following commands below.")
time.sleep(3)
os.system("clear")

todolist = []
#prints out the elements of the list
def view():
  os.system("clear")
  for item in range(len(todolist)):
    print(f"{item + 1}: {todolist[item]}")

while True:
  menu = input("1: Add\n2: View\n3: remove\n4: delete\n>")
  print()
  #Adds an item to list
  if menu == "1":
    item = input("What do you want to add?: ")
    if item in todolist:
      print("item already in list. you cannot add elements more than once.")
    else:
      todolist.append(item)
   # Views the list   
  elif menu == "2":
    view()
   # removes or edits elements in list 
  elif menu == "3":
    ask = input("Do yo want to \nremove \nor \nedit\n>")
    # removes element
    if ask == "remove":
      item = input("What would you like to remove?: ")
      if item in todolist:
        todolist.remove(item)
      else:
        print("Element not found please view the list to enter a valid element")
       # changes elements 
    elif ask == "edit":
      item = input("What item would you like to change? ")
      new_item = input("Enter the new item")
      if item in todolist:
        index = todolist.index(item)
        todolist[index] = new_item
      else:
        print("Please the item you want to change is not found")
  # Deletes the list      
  elif menu == "4":
    todolist = []
  #Checks if command you entered are correct.  
  else: 
    print("Please enter a valid number.")
    
  time.sleep(3)  
  os.system("clear")