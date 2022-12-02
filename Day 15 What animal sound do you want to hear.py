#Day 15 Challenge: Write a program that loops. Inside the loop, ask the user what animal sound they want to hear.

rules='''
Welcome to friendly kids game were the user would ask for an animal get to know the sound the animal makes in english.
The list below contains a list of animals that their sound will be gotten from.
anything not part of the list will be considered as invalid and asked for a valid animal.

list of valid animals = [cow, dog, cat, lion, duck, frog, horse, mice, pig, sheep]
'''
print(rules,'\n')
while exit != 'yes':
  animal = input("What animal do you want? ")
  if animal == 'cow' or animal == 'Cow':
    print("A",animal,"goes moo")
  elif animal == 'cat' or animal == 'Cat':
    print("A",animal,"goes meow")
  elif animal == 'dog' or animal == 'Dog':
    print("A",animal,"goes woof-woof")
  elif animal == 'duck' or animal == 'Duck':
    print("A",animal,"goes quack-quack")
  elif animal == 'frog' or animal == 'Frog':
    print("A",animal,"goes ribbit")
  elif animal == 'horse' or animal == 'Horse':
    print("A",animal,"goes neigh")
  elif animal == 'mice' or animal == 'Mice':
    print("A",animal,"goes squeak")
  elif animal == 'pig' or animal == 'Pig':
    print("A",animal,"goes oink")
  elif animal == 'sheep' or animal == 'Sheep':
    print("A",animal,"goes bah!!")
  elif animal == 'lion' or animal == 'Lion':
    print("A",animal,"goes Roar")
  else:
    print("please enter any animal given to you from the list above.")
  exit = input("Do you want to exit? ")