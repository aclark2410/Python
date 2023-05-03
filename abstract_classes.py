# Prevents a user from creating an object of that class
# compels the user to override abstract methods in a child class

# Abstract Class = a class which contains one or more abstract methods

# Abstract Method = a method that has a declaration but does not have an implementation

# By importing the built in abc class into our parent class as an argument
# and use the @abstractmethod decorator, it restricts using the class as an object

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    
    def go(self):
        print("You drive the car")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")


# vehicle = Vehicle()

car = Car()

motorcycle = Motorcycle()

#vehicle.go()

car.go()

motorcycle.go()