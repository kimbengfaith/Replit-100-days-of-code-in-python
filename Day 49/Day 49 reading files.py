# Day 49 Challenge: Readind a file

print("🌟Current Leader🌟\n")
'''
f = open("high score.txt", 'a+')
while True:
  initials = input("input 3 letter initail > ")
  score = input("Enter score: ")
  f.write(f"{initials} {score}\n")
  print("Added to high score table")
  question = input("do you want to add another(yes or no)? ")
  
  if question.lower()== "no":
    f.close()
    break
'''
list_of_lists =[]
list_name =[]
list_number = []


def separate():
  for lists in list_of_lists:
    list_name.append(lists[0])
    list_number.append(int(lists[1]))
    
f= open("high score.txt","r")

while True:
  content = f.readline().strip()
  contents = content.split()
  if content == "":
    break
  list_of_lists.append(contents)



separate()  
highest = max(list_number)
i = list_number.index(highest)
print("Analyzing high scores......\n")
print(f"current leader is {list_name[i]} {highest}")

