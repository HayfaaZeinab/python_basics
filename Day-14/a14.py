
# Base class
class Animal:
    def speak(self):
        print("This animal makes a sound")

# Derived class
class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Demonstration of polymorphism
for animal in [Dog(), Cat()]:
    animal.speak()
  
#foundation task
class Vehicle:
    def start(self):
        print("Vehicle starting...")

class Car(Vehicle):
    def start(self):
        print("Car: Vroom Vroom!")

class Bike(Vehicle):
    def start(self):
        print("Bike: Brumm Brumm!")

for vehicle in [Vehicle(),Car(),Bike()]:
    vehicle.start()

 
    
#stretch task
import math

class Shape:
    def area(self):
        return 0



class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        return round(math.pi*self.radius**2,1)


class Square(Shape):
    def __init__(self, side):
        self.side=side

    def area(self):
        return self.side**2


class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width


shapes = [Circle(5),Square(6),Rectangle(12, 10)]

for shape in shapes:
    print(f"{shape.__class__.__name__} Area: {shape.area()}")


#challenge task

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def work(self):
        print("Doing some work...")


class Developer(Employee):
    def work(self):
        print("Writing code...")


class Manager(Employee):
    def work(self):
        print("Managing project...")


employees=[Developer("Shyam", 50000),Manager("Rma", 70000)]


for emp in employees:
    print(f"Employee: {emp.name}")
    print(f"Role: {emp.__class__.__name__}")
    print("Task:", end=" ")
    emp.work()
    print()
