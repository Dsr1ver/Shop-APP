

from datetime import datetime
print("Welcome to the Shop")


inventory = {
    "Keyboards": 10,
    "Mice": 8,
    "Microphones": 9,
    "GPUS": 25,
}


products_total = 0
for val in inventory.values():
    products_total += val


print("Please enter your name")
name = input()
print("Please enter your last name")
lastname = input()

#Concatenacion

full_name = name + " " + lastname

print("Thanks for visiting us", full_name)