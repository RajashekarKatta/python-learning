# Inheritance
# In python Object Oriented Programming Inheritance means deriving a new class from already exsisting class. 
# The child class automatically inherits properties and methods of the parent class.
# This helps in code reuse, reducing redundancy, and building a clear class hierarchy.

# Types of Inheritance in Python¶
# Single Inheritance – One parent, one child
# Multiple Inheritance – Child inherits from multiple parents
# Multilevel Inheritance – Child → Parent → Grandparent
# Hierarchical Inheritance – One parent, multiple children
# Hybrid Inheritance – Combination of the above

# Single Inheritance 
# In Pyhton Single inheitance means deriving a class from single base class is known as single inheriatance.
# The derived class inherits all properties and method from the base class.


# Example:
class Father:
    def vehicle(self):
        print("Father has One Car")

class Son(Father):      # Here Subclass/Derived/Child Class inheriting propeties and methods form super/base/parent class
    def pets(self):
        print("Son have 2 Pets")


s = Son()
s.pets()
s.vehicle()


print("\n\n\n")
# Multilevel Inheritance
# In python Multiple inheritance means derivring a class from more than one base class is known as multilevel Inheritance.
# Here the child class inherits properties and methods from a parent clas

# Example for Multilevel Inheritance
class Father:
    def vehicle(self):
        print("Father has one Car")

class Mother:
    def Shop(self):
        print("Mother has one shop")

class Son(Father, Mother):
    def pets(self):
        super().vehicle()
        super().Shop()
        print("Son have two pets")

s = Son()
s.pets()
# s.vehicle()
# s.Shop()
print(Son.mro())

# Method Overriding
# Method overloading happens when child class provides it's own implementaion of a method that already exists in the parent class
# The method name must be the same, the number of parameters should be same.

# Example
class bird:
    def fly(self):
        print("Birds can fly")

class Penguin(bird):
    def fly(self):   # here Child class implementing it's method name. This is called method Overriding
        print("Penguins cannot fly")

p = Penguin()
p.fly()


print("\n\n\n")
# Real Time Example
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print(f"Vehicle brand is: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, fuel):
        super().__init__(brand)
        self.fuel = fuel

    def show(self):
        print(f"vehicle Brand {self.brand}")

    def details(self):
        print(f"car brand: {self.brand}, fuel type: {self.fuel}")

c = Car("Toyata", "Petrol")
c.show()
c.details()


print("\n\n\n")
# Multiple Inheritance
# Multiple Inheritance is type of inheritance. In which a class inherits from another class. and that class is derived from yet another class.
# It’s like a grandparent → parent → child relationship.
# Example for Muitilevel inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f"Brand name: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, fuel_type):
        super().__init__(brand)
        self.fuel_type = fuel_type

    def show_fuel_type(self):
        print(f"fuel Type: {self.fuel_type}")

class Electric_car(Car):
    def __init__(self, brand, fuel_type, battery):
        super().__init__(brand, fuel_type)
        self.battery = battery

    def show_battery(self):
        print(f"Battery life: {self.battery}")

c = Electric_car("TATA", "Petrol", "50%")
c.show_brand()
c.show_fuel_type()
c.show_battery()



# Example for Muitilevel inheritance
class Animal:
    def eat(self):
        print("Animal Eats Food")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks on land")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")
d = Dog()
d.eat()
d.walk()
d.bark()




# MRo (Method Resolution Order)
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")

class C(A):
    def show(self):
        super().show()
        print("C")

class D(B,C):
    def show(self):
        super().show()
        print("D")

d = D()
d.show()
print(d.mro())      # It shows the Method exection Order 


