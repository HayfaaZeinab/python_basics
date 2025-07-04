'''
#foundation task

x=int(input("Enter a number : "))
if (x==0):
    print("Its Zero")
elif(x<0):
    print("Its negative")
else:
    print("Its positive")
'''



'''
#stretch task
a=input("Do you like coding ?(yes/no) : ")
if (a=="yes" or a=="Yes"):
    print("Great!!Lets crack this together!")
elif (a=="no" or a=="No"):
    print("Thats alright...we can work together!!")
'''


"""
#challenge task
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=input("Enter the operation you want to perform (+,-,*,/) : ")
if c=="+":
    result=a+b
elif c=="-":
    result=a-b
elif c=="*":
    result=a*b
elif c=="/":
    result=a/b

print("result : ",result)"""

#Bonus task

print("TECH PERSONALITY QUIZ")
print("")
print("Answer 3 question and check where your interest lies...possible results:")
print("The Coder")
print("The Designer")
print("The Planner")

print("")

code=0
des=0
pla=0

print("1. What part of a project excites you most? ")
print("a) Writing efficient code")
print("b) Designing the interface")
print("c) Planning features and deadlines")
a=input("Enter an option : ")
if a=="a":
    code+=1
elif a=="b":
    des+=1
elif a=="c":
    pla+=1

print("\n2. How do you approach a problem?")
print("s) Break it into functions and write code")
print("b) Sketch ideas or visualize solutions")
print("c) Think of how to organize it or assign tasks")
a=input("Enter an option : ")
if a=="a":
    code+=1
elif a=="b":
    des+=1
elif a=="c":
    pla+=1

print("\n3. You are most satisfied when...")
print("a) Your code compiles and works!")
print("b) The interface looks perfect")
print("c) Everything is organized and on track")
print("d) You’ve learned or discovered something new")
a=input("Enter an option : ")
if a=="a":
    code+=1
elif a=="b":
    des+=1
elif a=="c":
    pla+=1

if code>=des and code>=pla:
    personality = "The Coder"
elif des>=code and des>=pla:
    personality = "The Designer"
elif pla>=code and pla>=des:
    personality = "The Planner"

print("")
print(f"You are: {personality}\n")


