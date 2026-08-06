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


# Example for abstract method
from abc import ABC, abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    def validate_payment(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be grreater than zero.")
        else:
            print(f"Validating Pyment of {amount}...")

class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing Credit card payment of {amount}")
        print("payment Successful via creadit card")

class UPIPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing UPI payment of {amount}")
        print("payment successful via UPI")

class NetBankingPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing Net Banking Payment of {amount}")
        print("Payment successful via Net Banking")

class Order:
    def __init__(self, amount, payment_gateway):
        self.amount = amount
        self.payment_gateway = payment_gateway

    def process_order(self):
        print("Order confirmed! Processing your payment...\n")
        self.payment_gateway.process_payment(self.amount)
        print("\nThank you for your purchase!\n")

# Example usage:
if __name__ == "__main__":
    # Example 1: Credit Card Payment
    order1 = Order(1500, CreditCardPayment())
    order1.payment_gateway.validate_payment(order1.amount)  # Validate payment before processing
    order1.process_order()

    # Example 2: UPI Payment
    order2 = Order(999, UPIPayment())
    order2.payment_gateway.validate_payment(order2.amount)
    order2.process_order()

    # Example 3: Net Banking Payment
    order3 = Order(2450, NetBankingPayment())
    order3.payment_gateway.validate_payment(order3.amount)
    order3.process_order()




# Another Real Time Example
from abc import ABC, abstractmethod
class Employee(ABC):

    def __init__(self, name, eid):
        self.name = name
        self.eid = eid

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, eid, monthly_salary, bonus):
        super().__init__(name, eid)
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def calculate_salary(self):
        total_salary = self.monthly_salary + self.bonus
        print(f"Full-Time Employee: {self.name}, ID:{self.eid}, bonus:{self.bonus}, Total_salary: {total_salary}")
        return total_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, eid, hourly_rate, hours_worked):
        super().__init__(name, eid)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        total_salary = self.hourly_rate * self.hours_worked
        print(f"Part Time Employee: {self.name}, ID: {self.eid}, hourly_rate: {self.hourly_rate}, hours_works: {self.hours_worked}, total_salary: {total_salary}")
        return total_salary


class Contractor(Employee):
    def __init__(self, name, eid, project_fee):
        super().__init__(name, eid)
        self.project_fee = project_fee

    def calculate_salary(self):
        total_salary = self.project_fee
        print(f"Contractor: {self.name}, ID: {self.eid}, project_fee: {self.project_fee}, total_salary: {total_salary}")
        return total_salary

def run_payroll(employees):
    total_expense = 0
    for emp in employees:
        salary = emp.calculate_salary()
        total_expense += salary

    print(f"\n Total Monthly Expense:{total_expense}")

    
# Example usage:
if __name__ == "__main__":
    emp1 = FullTimeEmployee("Alice", 101, 10000, 2000)
    emp2 = PartTimeEmployee("Bob", 102, 100, 80)
    emp3 = Contractor("Charlie", 130, 7500)

    all_employees = [emp1, emp2, emp3]
    run_payroll(all_employees)

    

