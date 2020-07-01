# OOP let us to create our own data types with different attributes and methods
# paradigm: way to think and structure the code, in a way that is easy to maintain extend and write
# breaking up functionalities and data into different pieces that model the real world
# into separate objects so that different people can work in different parts and combine them afterwards

# Class - blueprint of what we wanna create, basic attributes, methods or actions that it can take

class NameOfClass():
    class_attribute = 'value'

    def __init__(self, param1, param2):  # instanciate
        self.param1 = param1
        self.param2 = param2

    def method(self):  # methods that the objects will have access to
        pass  # code

    @classmethod
    def cls_method(cls, param1, param2):
        pass  # code

    @staticmethod
    def stc_method(param1, param2):
        pass  # code


obj1 = NameOfClass()  # instanciate de class -> create a new object
print(type(obj1))


class PlayerCharacter:
    # Class object attribute - not dinamic, is static. It's available for all the objects
    membership = True

    def __init__(self, name, age):  # constructor method
        if(self.membership):
            self.name = name    # self refers to the player character
            self.age = age  # attributes for the objects we are going to create

    def shout(self):  # method to be used by objects
        print(f'my name is {self.name}')


player1 = PlayerCharacter('Cindy', 44)  # objects built from the class
# all the objects have different memory location
player2 = PlayerCharacter('Cindy', 21)

print(player1.name)
print(player2.name)
print(player1.age)
print(player2.age)
print(player1.membership)
print(player2.membership)
print(player1.shout())
