#You are going to ask the user to type in the name of a test, maximum score they could receive, and how many points they received. For example, your test could be called "Python Skills" and the maximum score is 50 points and the user receives 30 points out of 50 possible points.
print("Enter the following Bellow")
print()
name_of_test=input("Enter the name of the test: ")
maximum_score= float(input('enter the maximum score: '))
marks=float(input("Enter the score you had: "))
percent_score=marks/maximum_score*100
if percent_score >= 90 and percent_score<=100:
  print("your grade is A+")
elif percent_score >= 80 and percent_score<=89:
  print("Your grade is A")
elif percent_score >= 70 and percent_score<=79:
  print("your grade is B")
elif percent_score >= 60 and percent_score<=69:
  print("Your grade is C")
elif percent_score >= 50 and percent_score<=59:
  print("Your grade is D")
elif percent_score< 50:
  print("You've got a U grade")
  