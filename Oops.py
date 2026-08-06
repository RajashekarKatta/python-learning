# Oops:¶
# In Python Oops(Object Oriented Programming) is a way of structuring of your code using classes and objects, so that it becomes resuable, modular and organized.

# Class:
# In python, object oriented programming (Oops), A class is a blueprint or template for creating objects. It defines set of propeties(attributes) and methods (behavior). class can be created by using class Keyword

# Object:
# An object is the actual thing built from the blueprint. It is a instance of a class. Multiple objects can be created from the same class, and each object is independent.

# In python everything is an object. An object is a fundamental building block that represents a piece of data.

# Constructor:
# In Python a constructor is a special method that is automatically called when an object is created for a class.

# __init__method (Constructor)
# In python init is a Constructor method used inside classes. When an object is created, Python first allocates memory for the new object. Then Python automatically calls the init method to initialize the object. Inside the init method, the arguments are assigned to the object's attributes using self.

# If a Constructor takes a parameters then it would be called as parametarized constructor.

# Parameters:¶
# A parameter is a variable defined inside a function or method definition, which acts as a placeholder to receive a value when the function is called. It does not have an actual value until you call the function.

# def greet(name):      # 'name' is a parameter
# print("Hello", name)
# Arguments:
# An argument is the actual value you pass to a function or method when calling it. Arguments are the real values you give to the function.

# greet("Raja")      # "Raja" is an argument

# Example:
class Car:
    def __init__(self, brand, color):      # here these are parameters
        self.brand = brand
        self.color = color

c1 = Car("BMW", "Black")      # here these are arguments
print(c1.brand, c1.color)



# self:
# In python self is a reference to the current object(instance). when we create an object from a class, self is used to access the data and methods that belongs to that specific object.

# Attributes can be created only by using the self variable and the dot(.) operator. Wihout self we are only creating an Local Variable.

class Mobile:
    def __init__(self):
        print("Inside constructor")

    def purchase (self):                    # here in functions first parameter should be self. 
        print("Purchasing a mobile")

mob1=Mobile()
mob1.purchase()



# Attributes in Oops:
# In Oops Attributes are variables that belong to an object or class They store data about the object
# Class = Blueprint (design of a house)
# Object = Actual House built from blueprint
# Attributes = Properties of that house (color, size, number of rooms, etc.)


# Types of Attributes in Python
# Instance Attribute: Instance attributes are variables that belong to a specific object (instance) of a class. They defined inside methods using self.
# Class Attributes: Class attributes (or class variables) are variables that belong to the class itself, not to any one object. They are shared by all instances of the class.
# Dynamic attributes are created at runtime — that is, after the object has already been created. They are not defined in the class or constructor, but you can add them manually to an object anytime.


# The syntax for attribute ---> reference_variable.attribute_name=value.
# 1. instance Attributes
class Car():
    def __init__(self, brand, color):
        self.brand = brand      # Instance attribute
        self.color = color      # Instance attribute

car1 = Car("BMW", "Black")
car2 = Car("AUDDI", "White")

print(car1.brand, car1.color)
print(car2.brand, car2.color)




# 2. Class Attributes (Static Attributes)
# Belong to the class itself, shared across all objects.
class fruits():
    taste = "Sweet"     # Class Attribute(Same for all Fruits)
    def __init__(self, fruit):
        self.fruit = fruit   # instance Attribute

fruit1 = fruits("Apple")
fruit2 = fruits("Mango")

print(fruit2.taste, fruit2.fruit)
print(fruit1.fruit, fruit1.taste)



# Dynamic Attributes
# You can add attributes to an object at runtime (Python allows it).
class Student():
    def __init__(self, name):
        self.name = name

s1 = Student("Pavankalyan")
s1.age = 25   # Dynamic Attribute
s2 = Student("Praveen")
s2.age = 23   # Dynamic Attribute

print(s1.name, s1.age)
print(s2.name, s2.age)



# Attributes vs Methods
# Attributes → Variables (object state).
# Methods → Functions inside class (object behavior).
class Dog():
    special = "Mammal"      # class Attribute

    def __init__(self, name, age):
        self.name = name          # Instance attribute
        self.age = age           # Instance attribute

    def bark(self):          # Method
        print(f"{self.name} is barking")
    
dog1 = Dog("Scooby", 4)
dog1.type = "Foody."   # Dynamic or Runtime Attribute

print(dog1.name + " The Dog age is " + str(dog1.age) + " and the breed of dog is " + dog1.special + " dog and it is " + dog1.type)
dog1.bark()

print(dog1.__dict__)   # Shows instance attributes


# The str() Method:
# str is a special method (also called a dunder method) in Python classes. Purpose: To return a human-readable string representation of an object.
# If the str() method is not set, the string representation of the object is returned:

# The string representation of an object WITHOUT the __str__() method
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("raja", 23)
print(p1.name, p1.age)



# The string representation of an object WITH the __str__() method.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name} and i am {self.age} years old."

p1 = Person("raja", 23)
print(p1)



class Mobile:
    def __init__(self, brand, price):
        print("Id of self constructor", id(self))
        self.brand = brand
        self.price = price     # Instance attribute
        brand = "Apple"        # without self it is a Local Variable

mob1 = Mobile("Apple", 25000)
mob2 = Mobile("Samsung", 17500)

print("Id of mob1 in driver code", id(mob1))
print("Id of mob2 in driver code", id(mob2))


# Example of Class and Object in Python:
class Student:   # defining a class
    School_name = "ABC School"   # class Attribue
    def __init__(self, name, age):
        self.name = name         # instance Attribue
        self.age = age           # instance Attribue

    def display(self):           # method
        print(f"Student Name: {self.name}, Age: {self.age}, School: {Student.School_name}")

    @classmethod
    def change_school(cls, new_school):   # class method to change school name
        cls.School_name = new_school

s = Student("Raja", 24) # creating an object of the class
s.display()
s.change_school("XYZ School")  # changing school name using class method
s.display()  # displaying updated school name


