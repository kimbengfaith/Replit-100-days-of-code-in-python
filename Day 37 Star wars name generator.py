#Days 37: this program will generate your Star Wars Name.

import os, time
print("starwars name generator".upper())
print()
while True:
  ask = input("Do you want to stop? ").strip()
  if ask.lower() == 'no':
    first_name = input("Input your first name > ").strip()
    last_name = input("Input your last name > ").strip()
    maiden_name = input("Input your mother's maiden name > ").strip()
    city = input("Input your city(where you were born) > ").strip()
    print()
    starwars = f"{first_name[0:3]+last_name[0:3]}".capitalize()
    starwars1 = f"{maiden_name[0:2]+ city[-3:]}".capitalize()
    
    print(f"Your star wars name is {starwars} {starwars1}")
    time.sleep(3)
    os.system("clear")
  else:
    break

