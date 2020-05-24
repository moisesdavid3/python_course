#Tuples - Inmutable
my_tuple = (1,2,3,4,5)
print(my_tuple)

user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age':20
}

print(user.items()) #Return tuples

new_tuple = my_tuple[1:4]
print(new_tuple)

x,y,z, *other = (6,7,8,9,10,11)
print(x)
print(y)
print(z)
print(other)

print(my_tuple.count(4))
print(my_tuple.index(5))
print(len(my_tuple))