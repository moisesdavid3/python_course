#strings
print("hi hello there")
username='supercoder'
password='supersecret'
long_str='''
WOW
O_O
---
'''
print(long_str)

first_name='Moises '
last_name='Medina'
full_name=first_name+last_name
print(full_name)

#concatenation
print('hello' + 'Moises')

#escape sequence 
# whatever after backsslash is string
# \t add tab
# \n add new line
weather = "\tit\'s \"kind of\" sunny\n hope you have a great day"
print(weather)

#formatted strings
name = 'Johnny'
age = 55

print('hi ' + name + '. You are ' + str(age) + ' years old') #long way to do it
print(f'hi {name}. You are {age} years old') #formatted for Python 3
print('hi {}. You are {} years old'.format(name,age)) #formatted for Python 2

# string indexes 

selfish = 'sourcemeridian'
        #  0123456789
# [start:stop:stepover] empty start index takes first value, empty stop index takes last value of the string
# negative indexes start from the last value, this means backwards
print(selfish[0:11:2])
print(selfish[::-1]) #print the reverse of the given string


# inmmutability -> strings cannot be changed

# once the string is created, I cannot change/reassign it
# the only way to change a string is to create something new


#string methods

greet='hellloooooooooo'
print(greet[0:len(greet)])

quote='to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.find('be')) #starts at position 3
print(quote.replace('be','me'))
