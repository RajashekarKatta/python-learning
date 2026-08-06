# Encapsulation is one of the fundamental concept in Oops.  Encapsulation means wrapping data (variables/attributes) and methods (functions that operate on the data) into a single unit called a class, while also controlling access to that data

# Access Modifiers (Visibility Levels)¶
# Encapsulation is controlled by using Access Modifiers

# Public → Accessible from anywhere.
# Protected → Accessible only within the class and its subclasses. # single underscore untey _variable = protected
# Private → Accessible only inside the same class. # Double underscore untey __variable = Private


# 1. Public Members
# Public members are variables or methods that can be accessed from anywhere inside the class, outside the class or from other modules. By default, all members in Python are public. They are defined without any underscore prefix (e.g., self.name).

# Example: This example shows how a public attribute (name) and a public method (display_name) can be accessed from outside the class using an object.

class Employee:
    def __init__(self, name):
        self.name = name   # public attribute

    def display_name(self):   # public method
        print(self.name)

emp = Employee("John")
emp.display_name()   # Accessible
print(emp.name)      # Accessible


# 2. Protected members
# Protected members are variables or methods that are intended to be accessed only within the class and its subclasses. They are not strictly private but should be treated as internal. In Python, protected members are defined with a single underscore prefix (e.g., self._name).

# Example: This example shows how a protected attribute (_age) can be accessed within a subclass, demonstrating that protected members are meant for use within the class and its subclasses.

class Employee:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected

class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)   # Accessible in subclass

emp = SubEmployee("Ross", 30)
print(emp.name)        # Public accessible
emp.show_age()         # Protected accessed through subclass


# 3. Private members
# Private members are variables or methods that cannot be accessed directly from outside the class. 
# They are used to restrict access and protect internal data. In Python, private members are defined with a double underscore prefix (e.g., self.__salary).
class Employee:
    def __init__(self, name, salary):
        self.name = name          # public
        self.__salary = salary    # private

    def show_salary(self):
        print("Salary:", self.__salary)

emp = Employee("Robert", 60000)
print(emp.name)          # Public accessible
emp.show_salary()        # Accessing private correctly
# print(emp.__salary)    # Error: Not accessible directly


# Encapsulation Without Access Modifiers
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Customer Name: {self.name}, Email: {self.email}")

    def update_email(self, new_email):
        self.email = new_email
        print(f"Email updated to: {self.email}")

s = Customer("Raja", "raja2355@gmail.com")
s.display_info()
s.update_email("rajas2325@gamil.com")
s.email = "Sam223@gamil.com"                # here we are directly accessing the email attribute and changing it without using the update_email method. 
s.display_info()


print("\n\n\n")
# Encapsulation With Access Modifiers
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.__email = email   # Private attribute

    def update_email(self, new_email):
        self.__email = new_email
        print(f"Email updated to: {self.__email}")

    def display_info(self):
        print(f"Customer Name: {self.name}, Email: {self.__email}")

s = Customer("Raja", "raja232@gmail.com")
s.display_info()
s.update_email("rajas2323@gmail.com")
# print(s.__email)   # This will not change the email attribute because it is private and cannot be accessed directly from outside the class.
s.display_info()


# Declaring Protected and Private Methods
# example for protected Method and Private Method
class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self._balance = balance   # Protected attribute
        self.__pin = pin   # Private     attribute

    def __validate_pin(self, entered_pin):
        self.__pin == entered_pin
        print(f"Validating pin for owner: {self.owner}")

    def withdraw(self, amount, entered_pin):
        if self.__validate_pin(entered_pin):
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrawal of {amount} successful. New balance: {self._balance}")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid PIN. Please Enter Correct PIN.")

s = BankAccount("Raja", 5000, 1234)
s.withdraw(1000, 1234)
s._BankAccount__validate_pin(1234)
print(s.__class__.__mro__) 



