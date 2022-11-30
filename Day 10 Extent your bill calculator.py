# a tip function that adds the total tip to the bill before splitting it equally between the people

total_bill= float(input("Enter your total bill: "))
print()
percent_tip= float(input("What percentage of tip will you leave to be added to the bill: "))
print()
tip=percent_tip/100*total_bill
total_bill_with_tip= tip + total_bill
number_of_people=int(input("Enter how many people are splitting the bill: "))
amount_per_person=total_bill_with_tip/number_of_people
print("Your total bill is",total_bill_with_tip,"$")
print()
if number_of_people == 1:
  print("you will pay a total amount of",total_bill_with_tip,"$")
else:
  print("your total bill per person is",amount_per_person,"$")