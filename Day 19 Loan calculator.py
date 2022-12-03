#Day 19 Challenge: create a loan calculator that shows how much money you owe for a loan of $1,000 with a 5% APR (APR is fancy for Annual Percentage Rate) over 10 years.

borrow=float(input("How much money did you borrow: "))
apr = 5/100
for year in range(10):
  loan=borrow + (borrow * apr)
  print("year",year+1,":",loan)
  apr +=(5/100)
print("hence your total loan after 10 years is",loan,"$")
  
  