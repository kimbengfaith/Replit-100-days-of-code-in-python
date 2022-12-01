# How many seconds are in a year?
year=int(input("Enter any year: "))
if year%4 == 0:
  number_of_days=366
  hours=number_of_days*24
  minutes=hours * 60
  seconds=minutes*60
  print("the number of seconds in the year",year,"is",seconds)
else:
  number_of_days=365
  hours=number_of_days*24
  minutes=hours * 60
  seconds=minutes*60
  print("the number of seconds in the year",year,"is",seconds) 