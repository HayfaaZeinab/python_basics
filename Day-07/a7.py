
"""
# Foundation task
def celsius(a):
    return (a - 32) * 5.0/9.0
a=int(input("Enter temperature in Farenheit : "))

print("Temperature in Celsius is : ",celsius(a))


# Stretch task
print("Rectangle Calculator : ")
a=int(input("Enter lenght of rectangle : "))
b=int(input("Enter breadth of rectangle : "))
def rectangle(a,b):
    perimeter= 2*(a+b)
    area=a*b
    return perimeter,area
perimeter,area=rectangle(a,b)
print(f"perimeter of rectangle {perimeter}")
print(f"area of rectangle {area}")


#challenge task

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Error! Division by zero is not allowed."
    else:
        return x/y

    

def calculator():
    print("CALCULATOR  \n")
    print("1. Addition \n")
    print("2. Subtraction \n")
    print("3. Multiplication \n")
    print("4. Division \n")


    ch=int(input("Enter your choice : "))

    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))

    if ch==1:
        print(f"Addition of {a} and {b} is {add(a,b)}")
    
    elif ch==2:

        print(f"Subtraction of {a} and {b} is {subtract(a,b)}")
    
    elif ch==3:
        print(f"Multiplication of {a} and {b} is {multiply(a,b)}")

    elif ch==4:
        print(f"Division of {a} and {b} is {divide(a,b)}")

calculator()
    
    
    """
