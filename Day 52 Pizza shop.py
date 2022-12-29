# Day 52 Challenge: Pizza shop

import os, time
print("What will you like to do in todays menu?\n")
pizza_order = []
# auto load
try:
  file = open("pizza.txt","r")
  pizza_order = eval(file.read())
  file.close()
except Exception as err:
  print("File cannot be found")


def top_list():
  row = ["Name","Quantity","Size","Cost"]
  if row not in pizza_order:
     pizza_order.append(row)
top_list()


# add order to list  
def add_list():
  time.sleep(1)
  os.system("clear")
  name = input("Enter your name: ")
  quantity = input("How many pizzas do you want?: ")
  size = input("what size would you like (l, s, m)? ").lower()
  
  try:
    quantity = int(quantity)
    if size == "s":
      cost = quantity*5.99
      cost = round(cost,2)
    elif size == "m":
      cost = quantity*9.99
      cost = round(cost,2)
    else:
      cost = quantity*14.99
      cost = round(cost,2)
    row = [name, quantity, size, cost] 
    pizza_order.append(row)
    print(f"Nice! your order has been added. your cost will be \033[0;35m{cost}$ \033[0;255m")
    
  except Exception as err:
    print("Enter an interger for the quantity")
    
# view order
def view_list():
  time.sleep(1)
  os.system("clear")
  for row in pizza_order:
    for item in row:
      print(f"{item:^10}",end = "  |  ")
    print()
  
while True:
  print("What would you like to do?")
  ask = input("1:Add to list \n2: View list\n>")
  if ask == "1":
    add_list()
  elif ask == "2":
    view_list()
  
   # autosave
  file = open("pizza.txt","w")
  file.write(str(pizza_order))
  file.close()
  time.sleep(2)
  os.system("clear")
 