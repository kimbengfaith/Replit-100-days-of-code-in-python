#Day 32 Challenge: Create a list that stores greetings in different languages. Start with the language you speak.
# At random, when the user clicks run, print one of the greetings.
print("Each time you click the run botton, hello in a different language will be printed out.")
import random
greetings = ["Hello","salut","Hola","Privet","Ni hao","Salve","Ya Yo","Hallo, Hi","Ola","Anyoung","Goddag"]
greet = random.randint(0,10)
print(f"\033[0;32m{greetings[greet]}")