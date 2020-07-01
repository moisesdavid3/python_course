#Encapsulation & Abstraction

class PlayerCharacter:  # Encapsulation - manage big amount of data with a big objects - classes
    def __init__(self, name, age):
        self.name = name  # Since there are not privacy on Python, by convencion programmers
        self.age = age  # Use `self._age` -> the underscore to let other that is private

    def run(self):
        return self

    def speak(self):
        print(f'My name is {self.name} and I am {self.age} years old')


player1 = PlayerCharacter('Centu', 54)
player1.speak()  # Abstraction - we don't need to know how the function was implemented
