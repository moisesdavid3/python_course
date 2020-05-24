# Loops

for item in "Zero To Mastery":
    print(item)

for item in [1,2,3,4,5]:
    print(item)

for item in {1,2,3,4,5}:
    for x in ('a','b','c'):
        print(item, x)

# For loops are able to iterate on whatever that be a collection of items

# iterable is a an object/collection that can iterated over - list, disctionary, string, tuple, set
# iterate -> one by one to check each item in the collection

user = {
    'name':'Golem',
    'age': 500,
    'can_swim': True
}

for key, value in user.items():
    print(key, value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)


# Counter

my_list = [1,2,3,4,5,6,7,8,9,10]

suma = 0
for sumi in my_list:
    suma+=sumi
print(suma)


# Range - type of object

for number in range(1,100,2): #ascending from 1 to 100 with a stepover of 2
    print(number)

for number in range(100,0,-5): #descending from 100 to 0 with a stepover of 5
    print(number)

for _ in range(2):
    print(list(range(10)))

# Enumerate - Gives the index of each item you want to iterate

for char in enumerate('hheelllloo'): 
    print(char)

for i, char in enumerate(list(range(0,100,2))):
    if char==50:
       print(f'index of 50 is {i}')


