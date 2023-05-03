# Duck Typing = the concept where a class of an object is less important tha the methods/attributes
#               class type is not checked if the minimum/attributes are present
#               "If it walks like a duck, and it quacks like a duck, then it must be a duck"


# We define two classes that have the same methods and attributes as each other (i.e walk and talk)

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuaking")


class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")


class Person:

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

    
duck = Duck()
chicken = Chicken()
person = Person()


person.catch(duck)

print()

# By passing in the chicken object, because it posessed the same methods and attributes, the program assumes it is the same and executes the functions
# If the methods and attributes are not exactly the same, it will throw an error. Overall the class type will not be checked as long as the functions are the same.

person.catch(chicken)