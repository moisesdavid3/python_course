# Scope - what variables do I have access to?

a=1 # global scope

def parent():
    a=10 # parent of local scope
    def confusion():
        a=5  # local scope
        return a
        def func():
            return sum

print(a)
print(confusion())

# Rules

#1 - start with local - inside functions
#2 - parent of local
#3 - global scope
#4 - built in python functions

#----------------------------------------
# # Global keyword

total = 0

def count():
    global total 
    total += 1
    return total

count()
count()
count()
print(count())

#----------------------------------------
# Non Local keyword

def outer():
    x="local"
    def inner():
        nonlocal x
        x="nonlocal"
        print("inner:", x)
    inner()
    print("outer:",x)
outer()



