

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# Creating objects
s1 = Student("Aanya", 90)
s2 = Student("Rahul", 80)

print(s1.name)                                
print(s2.grade)  

#isinstance() function checks if an object is an instance of a specific class or data type.

if isinstance([1, 2, 3], list):
    print("Object is a list")
else:
    print("Object is not a list")

if isinstance("12345", list):
    print("Object is a list")
else:
    print("Object is not a list")

#Another method to check if an object is a list is by using the type() function. This function returns the exact type of an object.

l1 = [1, 2, 3]
l2 = (10, 20, 30)  # A tuple

if type(l1) is list:
    print("Object is a list")
else:
    print("Object is not a list")

if type(l2) is list:
    print("Object is a list")
else:
    print("Object is not a list")



#To check if an object is a list , we can use the __class__ attribute and compare it to the list type:
l1 = [1, 2, 3, 4, 5]
l2 = (12, 22, 33)

if l1.__class__ == list:
    print("input is a list")
else:
    print("input is not a list")

if l2.__class__ == list:
    print("input is a list")
else:
    print("input is not a list")



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_details(self):
        print(f"{self.title} by {self.author}")

Books=[Book("abc","authorabc"),Book("def","authordef")]


for b in Books:
    b.display_details()


class Students:
    def __init__(self, name,grade,marks):

        self.name=name
        self.grade=grade
        self.marks=marks

    def display(self):
        print(f"{self.name} is in {self.grade} grade and scored {self.marks}")

student=[]
n=int(input("how many students to enter ? "))
for i in range(n):
    print(f"Enter details of {i+1} student")                      
    nam=input("Enter name : ")
    grd=input("Enter Grade : ")          
    ag=int(input("Enter Marks : "))  
    student.append(Students(nam,grd,ag))


for s in student:
    s.display()
    if s.marks>80:
        print(f"{s.name} is eligible for scholarship")


#sorting
student.sort(key=lambda x:x.marks,reverse=True)
print("students after sorting by marks in descending order")
for s in student:
    print(s.name)

#average calculation
total=0
for s in student:

    total+=s.marks
print("average marks of students",total/n)


#Create a class Movie with title and genre. Let the user enter a genre. Print all movies that match that genre.

class Movie:
    def __init__(self,title,genre):
        self.title=title
        self.genre=genre

    def display(self):
        print(f"{self.title} is a {self.genre} movie")

movies = [
    Movie("Inception", "Sci-Fi"),
    Movie("The Godfather", "Crime"),
    Movie("Finding Nemo", "Animation"),
    Movie("Avengers: Endgame", "Action"),
    Movie("Interstellar", "Sci-Fi")
]

flag=0
genre=input("enter the genre you wanna loo for : ").lower()
for movie in movies:
    if movie.genre.lower()==genre:
        movie.display()
        flag=1
if flag==0:
    print("no movie found with the given genre")

#Create a class Student with name and a list of subjects with marks.Print total marks for each.

class Students:
    def __init__(self,name,subjects):
        self.name=name
        self.subjects=subjects

    def total(self):
        total=sum(self.subjects.values())
        return total

    def display(self):
        print(f"{self.name} has a total of {self.total()} marks")

student=[]
n=int(input("Enter the number of students :"))

for i in range(n):
    name=input("Enter the name of the student :")
    subject={}
    s=int(input("enter number of subjects : "))
    for j in range(s):
        sub=input("Enter the subject name : ")
        marks=int(input("Enter the marks of the subject :"))
        subject[sub]=marks
    student.append(Students(name,subject))
     
for i in student:
    i.display()
    

    

##nested dictionary

students = {
    "Alice": {"Math": 85, "Science": 90},
    "Bob": {"Math": 78, "Science": 82},
    "Charlie": {"Math": 92, "Science": 88}
}

print(students["Alice"]["Math"])  

#update
students["Alice"]["Math"] = 95 
print(students["Alice"]["Math"])

#add
students["David"] = {"Math": 88, "Science": 92}


"""
students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    subject_count = int(input("How many subjects? "))

    subjects = {}
    for j in range(subject_count):
        subject = input("Enter subject name: ").strip()
        marks = int(input(f"Enter marks in {subject}: "))
        subjects[subject] = marks

    students[name] = subjects

"""

for name, subjects in students.items():
    print(f"\n{name}'s Marks:")
    for subject, mark in subjects.items():
        print(f"  {subject}: {mark}")


print("Students who scored more than 80 in Math:")
for name, subjects in students.items():
    if subjects["Math"] > 80:
        print(name)

total = 0
count = 0
for details in students.values():
    if "English" in details:
        total += details["English"]
        count += 1
if count > 0:
    avg = total / count
    print(f"\nAverage marks in English: {avg:.2f}")
else:
    print("No student has English marks entered.")

    


employees = {
    "John": {"department": "IT", "salary": 60000},
    "Sara": {"department": "HR", "salary": 55000}
}

"""
employees = {}

n = int(input("Enter number of employees: "))

for _ in range(n):
    name = input("\nEnter employee name: ")
    dept = input("Enter department: ")
    salary = int(input("Enter salary: "))
    employees[name] = {"department": dept, "salary": salary}
"""
search_dept = input("\nEnter department to search: ")

print(f"\nEmployees in {search_dept} department:")
found = False
for name, details in employees.items():
    if details["department"].lower() == search_dept.lower():
        print(f"{name} - Salary: {details['salary']}")
        found = True

if not found:
    print("No employees found in this department.")
