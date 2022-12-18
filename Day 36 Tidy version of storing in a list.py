#Day 36 Challenge: Create a list of people's names. Ask for first and last name (surname) separately. 

list_of_names = []
while True:
  first_name = input("Enter your first name: ").strip().capitalize()
  print()
  last_name = input("Enter your last name: ").strip().capitalize()
  name = f"{first_name } {last_name}"
  print()
  if name not in list_of_names:
    list_of_names.append(name)
  else: 
    print("Name already in list")
    print()
  for name in range(len(list_of_names)):
    print(f"{name+1}: {list_of_names[name]}")
  print()