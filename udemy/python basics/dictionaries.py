#Dictionary
dictionary = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}

my_list = [
    {
    'a': [1, 2, 3],
    'b': 'hello ',
    'x': True
    },
    {
    'a': [4, 5, 6],
    'b': 'moises',
    'x': False
    }
]

greet = my_list[0]['b'] + my_list[1]['b']

print(greet)
print(my_list[0]['b'][1])
print(dictionary)


#Dictionary keys -> Immutable and unique

diction = {
    'key1': [1,2,3],
    True: 'hello',
}

#Dictionary Methods

user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}

user2 = dict(name='Jhon') #Creates new dictionary
user3 = user.copy()

print(user.get('age', 55)) #Grab age from user dictionary, and if it doesn't exist, just put 55 (default)
print(user2)
print('basket' in user) # True
print('hello' in user.keys()) # False - hello is not key on user
print('hello' in user.values()) # True
print(user.update({'age': 55})) 
print(user.pop('age')) # Remove a key and value
print(user.items()) # Grab the complete item, key and value
print(user.clear()) # Remove everything
print(user3)

