# Day 46 challenge: Moke beast Moke dex

print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
print("\nthe type of the beast should either be \n>earth \n>fire \n>water \n>air\n")

mokebeast_dict = {}


def change_colors(type):
  if type.lower() == "earth":
    print("\033[0;32m",end="") #green
  elif type.lower() == "fire":
    print("\033[0;31m",end="") #red
  elif type.lower() == "water":
    print("\033[0;34m", end="") #blue 
  elif type.lower() == "air":
    print("\033[1;33m", end="") #yellow
  else:
    print("\033[0;30m", end="") #black


def print_dict():
  change_colors(mokebeast_dict[name]["element"])
  for key, value in mokebeast_dict.items():
    print(f"name: {key}", end=" | ")
    for subkey, subvalue in value.items():
      print(f"{subkey:^10} : {subvalue:^10}", end = " | ")
    print()

while True:
  name = input("\n\033[0;255menter the beast's name: ")
  type = input("Beast's type: ")
  move = input("Beast's special move: ")
  hp = input("staring hp: ")
  mp = input("staring mp: ")
  print()
  mokebeast_dict[name] = {"element": type, "special move": move, "staring HP": hp, "staring MP": mp}
  print_dict()
  ask = input("Again? > ")
  if ask.lower() == "no":
    break
  else:
    continue

    


