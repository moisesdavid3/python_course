# OOP
class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod  # Can use the class to create, modify. remove objects
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod  # We dont care about class
    def adding_things2(num1, num2):
        return num1 + num2

#player1 = PlayerCharacter('Tom', 20)
#print(player1.adding_things(2, 3))


player3 = PlayerCharacter.adding_things(2, 3)
print(player3.age)
