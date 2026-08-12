# python-learning

# Python OOP & Problem-Solving Practice

Welcome to my Python learning repository! 

This repository is focused mainly on **Object-Oriented Programming (OOP) in Python**. I have spent time learning the OOP concepts in detail and practicing them with multiple examples so that I can understand not only the theory but also how these concepts are used in real Python programs.

If you are interested in learning **Python OOP from the basics**, feel free to explore this repository. There are plenty of examples to help you understand each concept step by step. 

## 📚 What I Have Learned

###  Object-Oriented Programming

I have studied and practiced the major OOP concepts in Python, including:

- Classes and Objects
- Constructors (`__init__`)
- Instance Variables
- Class Variables
- Instance Methods
- Class Methods
- Static Methods
- Encapsulation
- Inheritance
- Single Inheritance
- Multiple Inheritance
- Multilevel Inheritance
- Hierarchical Inheritance
- Hybrid Inheritance
- Polymorphism
- Method Overriding
- Method Overloading concepts in Python
- Abstraction
- Abstract Classes
- Abstract Methods
- `super()`
- `self`
- Composition
- Association
- Aggregation
- Getters and Setters
- Properties
- Magic/Dunder Methods
- Access Modifiers
- And many practical examples

##  OOP Examples

Each concept contains examples designed to make the topic easier to understand.

For example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


student = Student("Raja", 24)

student.display()