# adding some color to your adventure story
# Example below
# print("Uh, oh, you've been given a", "\033[31m", "warning", "\033[0m", "for being a bad, bad person.")
# make sure to use the number that represents the color such as below
print(""" 
          Color         	Value
          Default         	0
          Black	            30
          Red	              31
          Green	            32
          Yellow	          33
          Blue	            34
          Purple	          35
          Cyan	            36
          White	            37""")
print("the syntax to add color to a text is \n {'\033[ value of color m'}.")
print()
print(''' Welcome to your adventure simulator. 
I am going to ask you a bunch of questions and then create an epic story with you as a star!''')
print()
name=input('What is your name? ')
live=input('Where do you live? ')
worst_enemy=input('What is your worst enemy"s name? ')
superpower=input("What is your superpower? ")
food=input("What is your favourite food? ")
print()
print("Hello",name,"! Your ability to",superpower,"\033[31m","will make sure you never have to look at",worst_enemy,"again. Go eat",food,"as you walk down the streets of",live,"\033[0m","and use",superpower,"for good and not evil!")