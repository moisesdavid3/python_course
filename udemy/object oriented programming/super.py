class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged In')


class Wizard(User):
    def __init__(self, name, power, email):
        # Call of init of the User inside the Wizard to add email
        # User.__init__(self, email)
        # This also can be done with the function super(), this call the class above, in this case, User. 'self' is not needed
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attack with Power of {self.power}')


wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
print(wizard1.email)
wizard1.attack()

# Instrospection

# Shows to what the instance wizard1 has access to, including methods and attributes
print(dir(wizard1))
