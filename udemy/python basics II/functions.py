# Functions

# parameters - variables to use inside the function
def say_hello(name,emoji): 
    print(f'hellloooo {name} {emoji}')

# default parameters - variables to use inside the function
def say_hello1(name='Darth',emoji='=O'): 
    print(f'hellloooo {name} {emoji}')

say_hello1()

# positional arguments - values we provide to the function when we call / invoke it
say_hello('Moises', ':)')

# keyword arguments - bad programming practice
say_hello(emoji='D=', name='Bibi')

# return
# used to gives the user a result, if we don't use it, the function won't show anything
# after the return, the interpreter exits the function

def sum(num1, num2):
    return num1 + num2
total=sum(4,5) # assign 9 to total
print(sum(10,total))

# should do one thing really well
# should return something

def sum(num1, num2):
    def sum2(n1, n2):
        return n1 + n2
    return sum2(num1,num2)
total = sum(10,20)
print(total)

# Docstrings - useful to add comment / definitions to the functions

def test(a):
    '''
    Info: this fn tests and prints param a
    '''
    print(a)
help(test)

# Clean Code

def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False

def is_even(num):  # Clean Code
    return num % 2 == 0

print(is_even(51))

# *Args (positional arguments) and **Kargs (keyword arguments)

def super_func(*args, **kwargs): # Let function receive as many arguments as I want
    total = 0
    for items in kwargs.values():
        total+=items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=10))

# Rule: params, *args, default parameters, **kargs


