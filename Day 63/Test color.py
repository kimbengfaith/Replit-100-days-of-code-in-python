# test.py file
def color(name):
  if name == "black":
    print("\033[0;30m")
  elif name == "red":
    print("\033[0;31m")
  elif name == "green":
    print("\033[0;32m")
  elif name == "brown":
    print("\033[0;33m")
  elif name == "blue":
    print("\033[0;34m")
  elif name == "purple":
    print("\033[0;35m")
  elif name == "yellow":
    print("\033[1;33m")
  elif name == "cyan":
    print("\033[0;36m")
  else:
    print("\033[1;37m")