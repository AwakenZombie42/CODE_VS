# Single inheritance

# Base Class
class Animal:
    def sound(self):
        print("This is an animal sound.")

# Derived Class
class Dog(Animal):
    def sound(self):
        print("Dog barks.")

# Example
dog = Dog()
dog.sound()  # Output: Dog barks.


# Multiple inheritance

# Base Classes
class Father:
    def profession(self):
        print("Father is a doctor.")

class Mother:
    def hobby(self):
        print("Mother loves painting.")

# Derived Class
class Child(Father, Mother):
    def talent(self):
        print("Child loves music.")

# Example
child = Child()
child.profession()  # Output: Father is a doctor.
child.hobby()       # Output: Mother loves painting.
child.talent()      # Output: Child loves music.


# Multilevel inheritance

# Base Class
class Animal:
    def move(self):
        print("Animals can move.")

# Intermediate Derived Class
class Mammal(Animal):
    def walk(self):
        print("Mammals can walk.")

# Derived Class
class Dog(Mammal):
    def bark(self):
        print("Dog barks.")

# Example
dog = Dog()
dog.move()  # Output: Animals can move.
dog.walk()  # Output: Mammals can walk.
dog.bark()  # Output: Dog barks.


# Hierarchical inheritance

# Base Class
class Vehicle:
    def type(self):
        print("This is a vehicle.")

# Derived Classes
class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels.")

class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels.")

# Example
car = Car()
bike = Bike()

car.type()   # Output: This is a vehicle.
car.wheels() # Output: Car has 4 wheels.

bike.type()  # Output: This is a vehicle.
bike.wheels() # Output: Bike has 2 wheels.


# Hybrid inheritance

# Base Class
class Animal:
    def sound(self):
        print("Animals make sounds.")

# Derived Class 1
class Bird(Animal):
    def fly(self):
        print("Birds can fly.")

# Derived Class 2
class Mammal(Animal):
    def walk(self):
        print("Mammals can walk.")

# Derived Class from two parents
class Bat(Bird, Mammal):
    def echo(self):
        print("Bats use echolocation.")

# Example
bat = Bat()
bat.sound()   # Output: Animals make sounds.
bat.fly()     # Output: Birds can fly.
bat.walk()    # Output: Mammals can walk.
bat.echo()    # Output: Bats use echolocation.