#Day 47 Challenge: Top Trumpers

import os, time, random
value_key =[]
print("🌟Top Trumps🌟")
print("\n\nWelcome to the Top Trumps 'Most Handsome Computing Teachers' Simulator")

trumps = {}
#produces a list of subkeys
def value_keys():
  for keys, value in trumps.items():
    for subkey in value:
      if subkey in value_key:
        continue
      else:
        value_key.append(subkey)
#prints out who has won  
def level():
  print(f"{my_card} has a {card_stat} stat of of {my_stat}")
  print(f"{computer_card} has a {card_stat} stat of of {computer_stat}")
  
# creates a 2D dictionary
trumps["David"] = {"Intelligence": 178, "Speed": 4, "Guile": 80, "Baldness Level": 99}
trumps["Mr Spock"] = {"Intelligence": 200, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Moica from Friends"] = {"Intelligence": 150, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Professor X"] = {"Intelligence": 250, "Speed": 1, "Guile": 200, "Baldness Level": 101}

main_key=list(trumps.keys())
  
value_keys()
print(value_key)

while True:
  my_card = input("\nchoose a card below \nDavid \nMr Spock \nMoica from Friends \nProfessor X \n> ")
  computer_card = random.choice(main_key)
  print(f"\nthe computer chooses {computer_card}")

  card_stat = input("\nchoose any of the stats below... \nIntelligence \nSpeed \nGuile \nBaldness Level\n ")
  
  if my_card not in main_key:
    print("Please enter a valid card")
    continue
  if card_stat not in value_key:
    print("Please you have entered a invalid stats please choose a correct stats.")
    continue
  my_stat = trumps[my_card][card_stat]              # lookes for the values of each player     
  computer_stat = trumps[computer_card][card_stat]
  
  if my_stat > computer_stat:
    level()
    print(f"********* {my_card} wins *********")
  elif computer_stat > my_stat:
    level()
    print(f"********* {computer_card} wins *********")
  else:
    level()
    print("Its a Draw")

  ask = input("\ndo you want to quite: ")
  if ask.lower() == "yes":
    break
  time.sleep(2)
  os.system("clear")
  
  
  