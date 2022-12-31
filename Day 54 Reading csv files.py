import csv
total_cost = 0.0
with open("Day54Totals.csv") as file:
  content = csv.DictReader(file)
  for row in content:
    multiple = float(row["Quantity"]) * float(row["Cost"])
    total_cost += multiple
print(f"\nthe total cost for the day is {round(total_cost,2)}")


