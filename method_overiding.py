# An object will associate a method that is more closely related to its own class than one that it has inherited from a parent class

class Animal:
    
    def eat(self):
        print("This animal is eating")


class Rabbit(Animal):

    # The name and arguments of the method should be exactly the same as the parent class to overide it
    def eat(self):
        print("This Rabbit is eating a carrot")

rabbit = Rabbit()

rabbit.eat()