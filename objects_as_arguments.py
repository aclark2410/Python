# Defining two classes as objects 

class Car:

    color = None

class Motorcycle:

    color = None

# We define a function outside of both of the defined classes

def change_color(vehicle, color):

    vehicle.color = color

# Assigning the class objects to variables 

car_1 = Car()
car_2 = Car()
car_3 = Car()
bike_1 = Motorcycle()

# We can pass the class object variable into the function and change a property within that object

change_color(car_1, "red")
change_color(car_2, "white")
change_color(car_3, "blue")
change_color(bike_1, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)