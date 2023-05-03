from car_class import Car

car_1 = Car("Chevy", "Corvette", "2021", "Blue")

car_2 = Car("Ford", "Mustang", "2022", "Red")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.colour)

car_1.drive()
car_2.stop()

car_2.wheels = 2 # You can re-assign the car object's value

print(car_1.wheels)
print(car_2.wheels)

Car.wheels = 1 # You can re-assign the class variable's value as well

print(Car.wheels) 

