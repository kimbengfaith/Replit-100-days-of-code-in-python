#Day 42 challenge: The moke beast

print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
print("\nthe type of the beast should either be \n>earth \n>fire \n>water \n>air\n")

mokebeast_dict = {"name":None, "type":None, "special move":None, "staring HP":None, "staring MP":None}

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

for key in mokebeast_dict:
  print(f"Input your beast's {key}")
  value = input("> ").strip()
  mokebeast_dict[key] = value

def color_dict():
  change_colors(mokebeast_dict["type"])
  for key, value in mokebeast_dict.items():
    print()
    print(f"{key}: {value}")
color_dict()


