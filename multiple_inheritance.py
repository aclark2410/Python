# Multiple Inheritance = when a child class is derived from more than one parent class

class Prey:

    def flee(self):
        print("This animal flees")


class Predator:

    def hunt(self):
        print("This animal hunts")

# Rabbit is Prey

class Rabbit(Prey):
    pass

# Hawk is a Predator

class Hawk(Predator):
    pass

# A fish can be Prey but can also be a Predator. We pass both of these arguments into the Fish class

class Fish(Prey, Predator):
    pass


rabbit = Rabbit()

hawk = Hawk()

fish = Fish()

# Here we are able to access methods from both the Prey and Predator classes

fish.flee()

fish.hunt()