# Polymorphism
# The word Polymorphism comes from Greek: ---> Poly = many ---> Morphe = form

# polymorphism is the ability of a single function or operator to work on different types of objects. The word itself comes from Greek, meaning "many forms" (poly = many, morph = form). It allows you to have one interface for many underlying implementations.

# Why is Polymorphism Needed?
# Without polymorphism, you’d write separate methods for each object type, even if the action is conceptually the same. That makes code rigid and repetitive.

# Polymorphism gives:
# Flexibility → one method name, multiple behaviors.
# Reusability → less code duplication.
# Extensibility → easy to add new types without rewriting old logic.
# Clean design → code becomes closer to real-world modeling.


# Polymorphism:
# Polymorphism means "having many forms". It can be broadly classified into two types:

# Compile-Time Polymorphism (Static Polymorphism)
# Runtime Polymorphism (Dynamic Polymorphism)
# Compile-Time Polymorphism (Static Polymorphism/ Early Binding)
# Definition: The compiler knows which method or operation to execute before the program runs (during compilation time). This is called Early Binding.

# How it is achieved: Usually through Method Overloading or Operator Overloading. (Note: Traditional method overloading isn't natively supported in Python like in Java or C++, but operator overloading serves as a great example).

# Example 1: If numbers are given, it performs Addition

print(5 + 10)  # Output: 15

# Example 2: If strings are given, it performs Concatenation (joining)
print("Hello " + "Raja")  # Output: Hello Raja


# Runtime Polymorphism (Dynamic Polymorphism / Late Binding)
# Definition: The decision of which method to run is made while the program is running (at runtime), depending on the object being processed. This is called Late Binding.
# How it is achieved: Through Method Overriding (which we used in our Employee Payroll and Payment Gateway examples).

# Example
class Employee:
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 55000

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 24000

# The magic that happens at runtime:
def run_payroll(employees):
    for emp in employees:
        # Python doesn't know in advance what class object 'emp' is!
        # During runtime, it identifies the object type and runs 
        # the appropriate calculate_salary() method.
        salary = emp.calculate_salary() 
        print(salary)


# What's happening here? The run_payroll function doesn't need to know the specific employee type beforehand. 
# When the program runs, it dynamically calls the correct calculate_salary() method based on whether emp is a FullTimeEmployee or a PartTimeEmployee. 
# Because this decision happens during execution, it is Runtime Polymorphism

# Example 1: 
class Animal:
    def Speak(self):
        print("Animal Speak")

class Dog(Animal):
    def Speak(self):
        print("Dog Barks")

class Cat(Animal):
    def Speak(self):
        print("Cat Meow")

class Cow(Animal):
    def Speak(self):
        print("Cow Moo")


animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.Speak()


