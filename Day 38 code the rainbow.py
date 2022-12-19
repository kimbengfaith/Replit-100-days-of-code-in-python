#Day 38 Challenge: Code the rainbow!

sentence = input("Type in any sentence: ").strip()

for letter in sentence:
  if letter.lower() == "r":
    print("\033[0;31m"+letter,end="")
  elif letter.lower() == " ":
    print("\033[0;255m"+letter,end="")
  elif letter.lower() == "b":
    print("\033[0;34m"+letter,end="")
  elif letter.lower() == "g":
    print("\033[0;32m"+letter,end="")
  elif letter.lower() == "p":
    print("\033[0;35m"+letter,end="")
  elif letter.lower() == "y":
    print("\033[1;33m"+letter,end="")
  else:
    print(letter,end="")