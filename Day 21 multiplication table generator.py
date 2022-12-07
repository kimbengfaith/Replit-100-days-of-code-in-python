info='''
welcome to the multiplicating calculation. this game is intented to help you solve the multiplication time table from 1 to 12 for any number.
Its mostly build for children with a beginner knowledge in maths calculation. 
Enjoy!!
'''
print(info,"/n")
multiple= int(input("Enter your multiple: "))
counter = 0
for number in range(1,13):
  print(number, "x", multiple)
  correct_answer = number * multiple
  answer = int(input("= "))
  if answer == correct_answer:
    print("Great work!")
    counter += 1
  else:
    print("Nope. The answer is",correct_answer)
if counter == 12:
  print("you scored",counter,'out of',12)
  print("Congratulations!! you scored a perfect score")
elif counter >=7 and counter < 12:
  print("you scored",counter,'out of',12)
  print("You passed try getting a perfect score next time ")
else:
  print("you scored",counter,'out of',12)
  print("dont worry you will do great next time just continue practicing")