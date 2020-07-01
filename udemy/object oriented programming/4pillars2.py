# Inheritance

class User:
    def sign_in(self):
        print('Logged In')


class Wizard(User):  # Inheritance from class `User` to a different class
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attack with Power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def arrows(self):
        print(f'Attack with arrows: arrows left - {self.num_arrows}')

    def run(self):
        print('run fast')


class Hybrid(Wizard, Archer):  # Multiple Inheritance
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hybrid1 = Hybrid('Borgie', 50, 100)
print(hybrid1.run())
print(hybrid1.arrows())


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

wizard1.attack()
archer1.arrows()

# wizard1 is instance of class Wizard, class User and the main class of Python, Object
print(isinstance(wizard1, object))


# # Polymorphism

# def player_attack(char):
#     char.attack()


# player_attack(wizard1)
# player_attack(archer1)


# for char in [wizard1, archer1]:
#     char.attack()
