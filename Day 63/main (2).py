# Day 63: storing subroutines in different python files and using them in the main file
# main.py
import color as co
menu = input("enter any color: ").strip().lower()

co.color(menu)
print("This is your named color")