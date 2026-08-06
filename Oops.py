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

