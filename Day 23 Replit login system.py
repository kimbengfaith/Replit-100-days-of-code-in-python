#Day 23 Challenge: Create a subroutine with both a username and password.

print("Welcome back to Replit.\nPlease enter your correct password to login to your system")
print()
def login_system():
  tryers = 1
  while True:
    if tryers <= 5:
      login_password = 'kimfaith'
      login_username ='kimbengfaith'
      password=input("What is your password?: ")
      username=input("What is your username?: ")
      if password == login_password and username == login_username:
        print("Welcome to Replit! ")
        break
      else:
        print("Whoops! I don't recognize that password or username\n Try again!")
    
    else:
      print("You have exeded the number of tryers pls try again after 30s")
      break
    tryers +=1 
login_system()
