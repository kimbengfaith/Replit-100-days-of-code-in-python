list_inventory = []

# auto load
try:
  file = open("inventory.txt","r")
  list_inventory = eval(file.read())
  file.close()
except Exception as err:
  print("\n File not found")

def view_list():
  item = input("Input the item you want to view: ").strip().upper()
  count = list_inventory.count(item)
  print(f"\nYou have {count} {item}")
  

def remove_item():
  item = input("what would you like to remove? ").strip().upper()
  if item in list_inventory:
    for element in list_inventory:
      if element == item:
           list_inventory.remove(element)
        
    print("\n The item has been removed")
    
  else:
    print("\nitem not found")

def add_item():
  item = input("What would you like to add? ").upper()
  list_inventory.append(item)
  # auto save
  print("\n Nice! item has been added")


while True:
  print("Please enter only intergers\n")
  menu = input("would you like to \n1:Add \n2:View \n3:Remove \n>")
  if menu == "1":
    add_item()
  elif menu == "2":
    view_list()
  elif menu == "3":
    remove_item()

  else:
    print("please choose a number")
  
  
  file = open("inventory.txt","w")
  file.write(str(list_inventory))
  file.close()
  ask = input("Would you like to continue? no/yes ").lower()
  if ask == "no":
    break
    
    
  
  