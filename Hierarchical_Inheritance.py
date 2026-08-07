# Hierarchical Inheritance
# Hierarchical Inheritance is a type of Inheritance where one parent class is inheritedby multiple child classes

# Characteristics of Hierarchical Inheritance
# One parent, many children.
# Children inherit all public and protected attributes/methods from the parent.
# Children can override parent methods to customize behavior.
# Helps in code reusability and logical organization.

class Vehicle:
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost

    def display_info(self):
        print(f"Brand: {self.brand} Cost: {self.cost}")

class Car(Vehicle):
    def __init__(self, brand, cost, doors):
        super().__init__(brand, cost)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.doors}")

class Bike(Vehicle):
    def __init__(self, brand, cost, cc):
        super().__init__(brand, cost)
        self.cc = cc

    def display_info(self):
        super().display_info()
        print(f"Bike cc: {self.cc}")


class Truck(Vehicle):
    def __init__(self, brand, cost, capacity):
        super().__init__(brand, cost)
        self.capacity = capacity

    def __str__(self):
        return f"Load Capacity: {self.capacity}"

c = Car("Hyundai", 1800000, 4)
b = Bike("Yamaha", 150000, 150)
t = Truck("Tata", 7500000, 20)

c.display_info()
b.display_info()
print(t)




print("\n\n\n")
# Same problem Example for runtime polymorphism
class Vehicle:
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost

    def display_info(self):
        print(f"Brand: {self.brand}, Cost: {self.cost}")

class Car(Vehicle):
    def __init__(self, brand, cost, wheels):
        super().__init__(brand, cost)
        self.wheels = wheels

    def display_info(self):
        super().display_info()
        print(f"Car wheels: {self.wheels}")

class Bike(Vehicle):
    def __init__(self, brand, cost, cc):
        super().__init__(brand, cost)
        self.cc = cc

    def display_info(self):
        super().display_info()
        print(f"Bike CC: {self.cc}")

class Truck(Vehicle):
    def __init__(self, brand, cost, capacity):
        super().__init__(brand, cost)
        self.capacity = capacity

    def display_info(self):
        super().display_info()
        print(f"Truc load capacity: {self.capacity} Tons.")


def all_vehicles(Vehicles_list):
    for vehicle in Vehicles_list:
        vehicle.display_info()


c = Car("Volvo", 2500000, 4)
b = Bike("Pulsar", 150000, 150)
t = Truck("TATA", 7500000, 25)

Vehicles_list = [c, b, t]
all_vehicles(Vehicles_list)


print("\n\n\n")
# Same Example but implementing Encapsulaion
class Vehicle:
    def __init__(self, brand, cost, insurance):
        self.brand = brand
        self._cost = cost
        self.__insurance = insurance

    def display_info(self):
        print(f"Brand: {self.brand}, cost: {self._cost}")

    def get_insurance(self):
        print(f"Insurance Type: {self.__insurance}")

class Car(Vehicle):
    def __init__(self, brand, cost, insurance, wheels, color):
        super().__init__(brand, cost, insurance)
        self.wheels = wheels
        self.color = color

    def display_info(self):
        super().display_info()
        print(f"Car wheels: {self.wheels}, and Car color is : {self.color}")

    def get_insurance(self):
        super().get_insurance()

class Bike(Vehicle):
    def __init__(self, brand, cost, insurance, cc, model):
        super().__init__(brand, cost, insurance)
        self.cc = cc
        self.model = model

    def display_info(self):
        super().display_info()
        print(f"Bike CC: {self.cc}, and Bike Mode: {self.model}")

    def get_insurance(self):
        super().get_insurance()

class Truck(Vehicle):
    def __init__(self, brand, cost, insurance, capacity):
        super().__init__(brand, cost, insurance)
        self.capacity = capacity

    def display_info(self):
        super().display_info()
        print(f"Truck Brand: {self.brand}, cost: {self._cost} and the capacity: {self.capacity} Tons.")

    def get_insurance(self):
        super().get_insurance()


class All:
    print("--- Vehicle Details ---")
    def all_vehicles(Vehicle_list):
        for vehicle in Vehicle_list:
            vehicle.display_info()
            vehicle.get_insurance()
            
    def all_insurance(Vehicle_list):
        print("--- Insurance Details ---")
        for insur in Vehicle_list:
            insur.get_insurance()


c = Car("Volvo", 2500000, "Comprehensive", 4, "Black")
b = Bike("Pulsar", 150000, "Third-Party", 150, 2022)
t = Truck("TATA", 7500000, "Comprehensive", 25)

Vehicles_list = [c, b, t]
All.all_vehicles(Vehicles_list)
All.all_insurance(Vehicles_list)