class Car:

    wheels = 4 # class variable that applies for all unique objects within the class

    def __init__(self, make, model, year, colour):

        self.make = make # instance variable

        self.model = model # instance variable

        self.year = year # instance variable

        self.colour = colour # instance variable



    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " car is stopped")

    