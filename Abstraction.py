# Abstraction in Oops
# In python, Abstractiom means is the process of hiding information or hiding implementation details and showing only the essential details of an object.
# Data abstraction means showing only the essential features and hiding the complex internal details.
# Technically, in Python abstraction is used to hide the implementation details from the user and expose only necessary parts, making the code simpler and easier to interact with.


# Abstraction class:
# An Abstact class is a fundamental concept in Oops(Oblect oriented programming). It servers as a blueprint for other classes and cannot be instantiated on it's own.

# Abstract Class: An abstract class is a class that can contain one or more abstract methods. For an abstract class you can’t create an object directly.

# Abstract Method:  abstract method is a method that is declared but not implemented — it prevents direct execution because subclasses must override it.


# Examples:
from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def car(self):
        pass

    @abstractmethod
    def bus(self):
        pass

    def bike(self):
        print("This is a bike")

class Types_of_vehicle(Vehicle):
    def __init__(self, vehicle_name, vehicle_type):
        self.name = vehicle_name
        self.vehicle_type = vehicle_type

    def car(self):
        print("This is a car")

    def bus(self):
        print(f"This is a bus for {self.name} and the vehicle type is {self.vehicle_type}.")


s = Types_of_vehicle("School", "Public")
s.car()
s.bus()
s.bike()
# p = Vehicle() # This will raise an error because we cannot instantiate an abstract class directly.



print("\n\n\n")
# Corrected Version of Abstraact Class
from abc import ABC, abstractmethod

# creating class abstract
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass       # No implementation
        
    def fuel_type(self):
        return "Disel or Petrol"     # Concrete Method

class Car(Vehicle):
    def start(self):
        return "Car Engine started"

class Bike(Vehicle):
    def start(self):
        return "Bike Engine started"

v1 = Car()
B1 = Bike()

print(v1.start())
print(v1.fuel_type())

print(B1.start())
print(B1.fuel_type())


print("\n\n\n")



# Concrete Method:
# Concrete methods are fully implemented methods within an abstract class. Subclasses can inherit and use them directly, promoting code reuse without needing to redefine common functionality.
# Example for Concrete method
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def move(self):
        return "Moving"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

dog = Dog()
print(dog.move())



