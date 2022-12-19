# Day 40 Challenge

import time, os
print("🌟Contact Card🌟")

name = input("Input your name: ")
date_of_birth = input("Input your date of birth: ")
tel_number = input("Input your telephone number: ")
email = input("Input your email: ")
physical_address = input("Input your physical address: ")

info_dict = {"name": name, "dob": date_of_birth, "telephone":tel_number,"email": email, "physical_address": physical_address}

time.sleep(2)
os.system("clear")

print(f"Hi {info_dict['name']}. Our dictionary says that you are born on {info_dict['dob']}, we can call you on {info_dict['telephone']}, email {info_dict['email']}, or write to {info_dict['physical_address']}.")