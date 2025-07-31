# Recursive function to count down
def count_down(n):
    if n <= 0: # Base case
        return
    print(n)
    count_down(n - 1)# Recursive call

count_down(5)

#foundation
def sum(n):
    if n==1:
        return 1
    else:
        return n + sum(n-1)
    
n=int(input("enter a number : "))
if n>=1:
    print("sum of number is ",sum(n))
else:
    print("enter a positive number")

#stretch
def stars(n,curr=1):
    if curr>n:
        return 
    print("*"*curr)  
    stars(n,curr+1)
rows=int(input("Enter number of rows: "))
stars(rows)

#challenge

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


terms=int(input("Enter how many terms: "))
print("Fibonacci sequence:")

for i in range(terms):
    print(fibonacci(i), end=" ")
