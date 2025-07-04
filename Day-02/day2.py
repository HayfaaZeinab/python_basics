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
a=int(input("Enter an option : "))
if a=="a":
    code+=1
elif a=="b":
    des+=1
elif a=="c":
    pla+=1





