#You have a Parent class called Vehicle.
#It has a method move() that prints "Vehicle moves".
#Now you want a child class called Car that:
#Inherits from Vehicle
#Has its own method honk() that prints "Car honks"

class Vehicle:
    def moves(self):
        print('vehicles move.')
        
class Car(Vehicle):
    def honks(self):
        print('car honks.')
        
c = Car()
c.moves()
c.honks()


print()
print()
#"Suppose you have:
#Parent class Animal
#Method speak() → prints "Animal speaks"
#Make a child class Cat that:
#Inherits Animal
#Overrides speak() to print "Cat meows"

class Animal:
   def speak(self):
       print('animals speak.')
       
class Cat(Animal):
    def speak(self):
        print('cat meows')
        
c = Cat()
c.speak()


print()
print()
#Try writing a class:
#Parent class: Vehicle
#Method: start() → prints "Vehicle starts."
#Child class: Bike
#Method: start() → calls parent start() using super(), then prints "Bike zooms!"

class Vehicle:
    def Start(self):
        print('vehicle starts.')
        
class Bike(Vehicle):
    def Start(self):
        #super().Start()
        print('Bike zooms!')
        
b = Bike()
v = Vehicle()
for vaahan in (b,v):
    vaahan.Start()
        
        
print()
print()
#You need to create a Teacher class and a MathTeacher class that inherits from it.
#Requirements:
#Teacher should have a __init__ constructor that accepts:
#name
#subject
#Print: "Teacher created: {name}, teaches {subject}"
#MathTeacher should:
#Inherit from Teacher
#Override the constructor and use super() to call the parent
#Also print "Math Teacher specializes in Algebra."
#Create a MathTeacher object with name "Mr. Jacob" and subject "Mathematics"

class Teacher():
    def __init__(self, name,subject):
        self.name = name
        self.subject = subject
        print(f'Teacher created: {self.name}, teaches {self.subject}.')
        
class MathTeacher(Teacher):
    def __init__(self, name, subject):
        super().__init__(name, subject)
        print('Math Teacher specializes in Algebra.')
    
    
x = MathTeacher('Mr. Jacob', 'Mathematics')

