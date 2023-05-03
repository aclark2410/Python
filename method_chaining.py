# Method Chaining = is used to call multiple methods sequentially,
#                   each call performs an action on the same object
#                   and returns self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()

# Normal we can assign one method at a time to the car object

car.turn_on()
car.drive()
car.brake()
car.turn_off()

print()

# By returning self in the methods allows us to chain methods sequentially

car.turn_on().drive().brake().turn_off()

