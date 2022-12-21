print("🌟Website Rating🌟")

#Day 41 Challenge: Website rating
website_dict = {"name":None, "URL":None, "description":None, "rating":None}

def print_dictionary():
  for key, value in website_dict.items():
    print()
    print(f"{key}: {value}")

for key in website_dict:
  print()
  print(f"Enter the {key} of the website")
  value = input("> ")
  website_dict[key] = value
print_dictionary()
  
  