import random
import datetime
import math

# Generate random numbers
lucky_number = random.randint(1, 100)
print(f"Your lucky number is: {lucky_number}")

# Work with dates
today = datetime.date.today()
print(f"Today is: {today}")

# Mathematical operations
radius = 5
area = math.pi * math.pow(radius, 2)
print(f"Circle area: {area:.2f}")

# Import specific functions
from random import choice
colors = ["red", "blue", "green", "yellow"]
print(f"Random color: {choice(colors)}")


#foundation task 
import random
while True:
    print("\n\nDice Roller\n")
    print("1. Roll  a 6 -sided  dice")
    print("2. Roll a 20-sided dice")
    print("3. Roll multiple dice")
    print("4. Exit")
    choice=int(input("Choose Option : "))
    if choice==1:
        print("You rolled a",random.randint(1,6))
    elif choice==2:
        print("You rolled a",random.randint(1,20))
    elif choice==3:
        a=int(input("how many dice do you want to roll ?"))
        side=int(input("how many sides should each die have ? "))
        print("You rolled",a,"dice with",side,"sides: ")

        for i in range(a):
            print(random.randint(1,side),end=" ")
    elif choice==4:
        break

# Stretch task

import datetime

print("Birthday Calculator ")
dt=input("Enter your birthdate (yyyy-mm-dd) : ")
d=datetime.datetime.strptime(dt, "%Y-%m-%d")
today = datetime.date.today()
print(dt)
print(today)

##i could complete this task...i think it requires more time..ill try this one later



#challenge task



import random
import string

print("Advanced Password Generator")


while True:
    try:
        l=int(input("Password length (8-50): "))
        if 8<=l<=50:
            break
        else:
            print("Please enter a number between 8 and 50.")
    except ValueError:
        print("Enter a valid number!")


include_upper=input("Include uppercase letters? (y/n): ").lower()
include_digits=input("Include numbers? (y/n): ").lower()
include_symbols=input("Include symbols? (y/n): ").lower()
exclude_similar=input("Exclude similar characters (0,O,l,1)? (y/n): ").lower()


characters=string.ascii_lowercase

if include_upper=='y':
    characters+= string.ascii_uppercase

if include_digits=='y':
    characters+=string.digits

if include_symbols=='y':
    characters+= string.punctuation

if exclude_similar == 'y':
    for ch in "0Ol1":
        characters = characters.replace(ch, "")


password = ""

for i in range(l):
    random_char=random.choice(characters)
    password+=random_char

print("\nGenerated password:", password)
print("\nPassword Analysis:")

if l>=12:
    print("Length:",l,"characters-Strong")
else:
    print("Length:",l,"characters-Weak")


has_upper=False
for c in password:
    if c.isupper():
        has_upper=True
        break

if has_upper:
    print("Uppercase: Yes")
else:
    print("Uppercase: No")


has_lower=False
for c in password:
    if c.islower():
        has_lower=True
        break

if has_lower:
    print("Lowercase: Yes")
else:
    print("Lowercase: No")


has_digit=False
for c in password:
    if c.isdigit():
        has_digit = True
        break

if has_digit:
    print("Numbers: Yes")
else:
    print("Numbers: No")


has_symbol = False
for c in password:
    if c in string.punctuation:
        has_symbol=True
        break

if has_symbol:
    print("Symbols: Yes")
else:
    print("Symbols: No")

score=0
if l>=12:
    score+=1
if has_upper:
    score+=1
if has_lower:
    score+=1
if has_digit:
    score+=1
if has_symbol:
    score+=1

if score==5:
    print("Overall strength: Very Strong")
elif score>=3:
    print("Overall strength: Strong")
else:
    print("Overall strength: Weak")
