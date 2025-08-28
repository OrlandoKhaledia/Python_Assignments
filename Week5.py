# Designing my Own Class!
# Base class
class Bicycle:
    # Constructor to initialize unique attributes
    def __init__(self, brand, color, gear_count):
        self.brand = brand
        self.color = color
        self.gear_count = gear_count

    # Method to display info
    def display_info(self):
        print(f"This is a {self.color} {self.brand} bicycle with {self.gear_count} gears ")

    # Method to ride the bicycle
    def ride(self):
        print(f"The {self.brand} bicycle is moving ")

# Inheritance example: MountainBicycle inherits from Bicycle
class MountainBicycle(Bicycle):
    def __init__(self, brand, color, gear_count, suspension):
        super().__init__(brand, color, gear_count)  # Call parent constructor
        self.suspension = suspension  # Extra attribute

    # Override ride method (polymorphism)
    def ride(self):
        print(f"The {self.brand} mountain bike rides smoothly on rough terrain with {self.suspension} suspension")

# Create objects
bike1 = Bicycle("Giant", "blue", 18)
bike2 = MountainBicycle("Trek", "red", 21, "full")

bike1.display_info()
bike1.ride()

bike2.display_info()
bike2.ride()

# Q2
# Base class
class Vehicle:
    def move(self):
        pass  # Base method
class Car(Vehicle):
    def move(self):
        print("Driving on the road ")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water ")

# Demonstrate polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()  

