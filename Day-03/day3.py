"""#foundation task

for i in range(1,20,2):
    print(i,end=" ")
"""

"""
#stretch task

a=input("Enter secret cose : ")
while(a!="python"):
    a=input("Enter secret cde:")
print("access granted")
"""


"""
import random
a=random.randint(1,10)

tries=0
while True:
    guess=int(input("Enter a number"))
    tries+=1

    if guess==a:
        print(f"you guessed in {tries} tries. ")
        break
    elif guess<a:
        print("too low try again")
    elif guess>a:
        print("high try again")
"""

#bonus task

a=int(input("Enter a number to genereate multplication table : "))

for i in range(1,11):
    print(f"{a}x{i}={a*i}")
