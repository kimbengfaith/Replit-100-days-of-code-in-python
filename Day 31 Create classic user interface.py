#Day 31:Create a classic user interface using string manipulation.

# Interface 1:
head = "\033[0;31m=\033[0;255m=\033[0;34m=\033[1;33m Music App \033[0;31m=\033[0;255m=\033[0;34m="
print(f"          {head: <35}\n")
def color_text(color,text):
  if color == "red":
    statement = f"\033[0;31m{text}"
  elif color == "yellow":
    statement = f"\033[1;33m{text}"
  elif color == "green":
    statement = f"\033[0;32m{text}"
  elif color == "pink":
    statement = f"\033[0;35m{text}"
  elif color == "blue":
    statement = f"\033[0;34m{text}"
  else:
    statement = f"\033[0;255m{text}"
  return statement
  
stat_1 = color_text("white","Radio Gaga")
print(f"{stat_1: ^26}")
stat_2 =  color_text("yellow","Queen")
print(f"{stat_2: ^20}\n\n")
stat_3 = color_text("white","PREV")
print(stat_3)
stat_4 = color_text("green","NEXT")
print(f"{stat_4: ^20}")
stat_5 = color_text("pink","PAUSE")
print(f"{stat_5:^30}\n\n\n")

#Interface 2:
stat_1 = color_text("white","WELCOME TO")
print(f"{stat_1: ^35}")
stat_2 = color_text("blue","--   ARMBOOK   --")
print(f"{stat_2: ^35}\n")
stat_3 = color_text("yellow","Definitely not a rip pff of")
print(f"{stat_3: ^49}")
stat_4 = color_text("yellow","a certain other social ")
print(f"{stat_4: ^55}")
stat_5 = color_text("yellow","networking site")
print(f"{stat_5: ^60}\n")
stat_6 = color_text("red","Honest.")
print(f"{stat_6: ^39}")
stat_7 = color_text("white","Username:")
print(f"{stat_7: ^41}")
stat_8 = color_text("white","Password:")
print(f"{stat_8: ^41}")
