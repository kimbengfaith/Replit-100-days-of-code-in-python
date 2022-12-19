import random,time,os
print("Welcome to the Hangman Game")
print('''+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
list_of_words = ["british", "suave", "Integrity", "accent", "evil", "genius", "Downton"]
word_choice =(random.choice(list_of_words)).lower()
# new list
new_list = []
#prints out blanks based on the number of letters in the word
for number in range(len(word_choice)):
  new_list.append("_")

#number of lives
lives = 5
while True:
  time.sleep(2)
  os.system("clear")
  letter = input("Choose a letter\n > ").lower()
  # if number is already in new list
  if letter in new_list:
    print("letter already in the list")
    continue
    
  elif letter in word_choice:
    print("Correct!\n")
    i = word_choice.index(letter)
    new_list[i] = letter
    
  elif letter not in word_choice:
    lives -= 1
    print("the letter is not found in word\n")
  #compares both list
  for num in word_choice:
    if num.lower() in new_list:
      print(num,end="")
      all_letters = True # if you have a correct letter
    else:
      print("_",end="")
      all_letters=False
  print()
  print()
  
  if all_letters:
    print("congratulations you have won.")
  else:
    print(f"you have got {lives} left")
#checks how many lives you have left
  if lives <= 0:
    print("you have lost")
    break
    