import random

check = True

while check:
    print(random.randint(1,6))
    again_roll = input("Do you want to Roll the dice again (y/n)? ")
    if again_roll.lower() == 'y':
        continue
    else:
        break


