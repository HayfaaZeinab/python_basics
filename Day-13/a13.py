
# Defining a simple class and object
class Person:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Creating an object
p1 = Person("Alice", 25)
p1.greet()

class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year

    def summary(self):
        print("Book Summary:")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Published: {self.year}")
        print()  


books=[]

n=int(input("How many books do you want to enter? "))

for i in range(n):
    print(f"\nEnter details for book {i + 1}:")
    title=input("Title: ")
    author=input("Author: ")
    year=input("Published Year: ")
    books.append(Book(title, author, year))


for b in books:
    b.summary()


class Student:
    def __init__(self,name,rollnumber,marks):
        self.name=name
        self.rollnumber=rollnumber
        self.marks=marks

    def haspassed(self):
        return self.marks > 40

    def display(self):
        print(f"\nStudent: {self.name}")
        print(f"Roll No: {self.rollnumber}")
        print(f"Marks: {self.marks}")
        if self.haspassed():
            print("Status: Passed")
        else:
            print("Status:Failed")



students=[]

n=int(input("Enter the number of students: "))
for i in range(n):
    print(f"\nEnter details for student {i+1}:")
    name=input("Name: ")
    roll=int(input("Roll number: "))
    marks=int(input("Marks: "))
    students.append(Student(name, roll, marks))



for student in students:
    student.display()
