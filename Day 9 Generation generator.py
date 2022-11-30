# just a fun game to know what generation you are part of.
print("Enter your Year of birth to know the generation you were born in")
print()
year_Of_birth=int(input("Enter year of birth: "))
print()
if year_Of_birth >= 1925 and year_Of_birth <= 1946:
  print("your a Traditinalist")
elif year_Of_birth >= 1947 and year_Of_birth<= 1964:
  print("your part of the Baby Boomers")
elif year_Of_birth >= 1965 and year_Of_birth<= 1981:
  print("Wow you are part of Generation X")
elif year_Of_birth >= 1892 and year_Of_birth<= 1995:
  print(" your one of the Millenials")
elif year_Of_birth >= 1996 and year_Of_birth<= 2015:
  print("your in Generation Z")
else:
  print("Hmm i dont think i know your generation try any year between 1952 and 2015")