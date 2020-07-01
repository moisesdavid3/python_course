class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        # print(f'{self.name} is just walking around')
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# 1 Add another Cat


class Ivo(Cat):
    def jump(self):
        print('Ivo jumps a lot')


# 2 Create a list of all of the pets (create 3 cat instances from the above)
cat1 = Simon('Negrita', 5)
cat2 = Sally('Juy', 7)
cat3 = Ivo('Abril', 1)
my_cats = [cat1, cat2, cat3]

# 3 Instantiate the Pet class with all your cats use variable my_pets
# pet1 = Pets(cat1)
# pet2 = Pets(cat2)
# pet3 = Pets(cat3)
my_pets = Pets(my_cats)

# 4 Output all of the cats walking using the my_pets instance

my_pets.walk()
