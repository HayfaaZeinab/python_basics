
#foundation task
print("Safe Calculator")

try:
    num1=int(input("Enter a number : "))
    num2=int(input("Enter a number : "))
    print(f"Result : {num1/num2}")

except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")

except ValueError:
    print("Error! Invalid input.")


#stretch task


print("File Reader")
while True:

    try:
        filename=input("Enter the file name : ")
        with open(filename,"r") as file:
            print(f"File contents : {file.read()}")
            break
        


    except FileNotFoundError:
        print("File dosent exist")
        choice=input("Would you like to try another filename ? (yes/no) : ").lower()

        if choice=="no":
            print("Exiting the program")
            break

#challenge task

print("Grade Calcualator ")
while True:

    try:
        num=int(input("How many grades to enter? "))
        break
    
    except ValueError:
        print("Please enter a valid number")


grades=[]
for i  in range(num):
    while True:      
        try:
            grade=int(input(f"Enter grade {i+1}: "))
            if 0<=grade<=100:
                grades.append(grade)
                break 
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


average=sum(grades)/len(grades)

if average>=90:
    letter="A"
elif average>=80:
    letter="B"
elif average>=70:
    letter= "C"
elif average>=60:
    letter="D"
else:
    letter="F"

print("Aversge Score : ",average)
print("Grade",letter)
            
