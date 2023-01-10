# Day 60 Challenge
import datetime

print("Event Countdown\n")

today = datetime.date.today()

name = input("Enter the event: ")
year = int(input("Input the year: "))
month = int(input("Input month: "))
day = int(input("Input the day: "))
event = datetime.date(day=day, month=month, year= year)

difference = abs(today - event)
difference = difference.days # gives the output in just days.

if event == today:
  print(f"{name} is today!")
elif event > today:
  print(f"{name} is going to be in {difference} days ")
else:
  print(f"{name} was {difference} days ago. you missed the event.")