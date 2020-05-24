# lists - ordered sequence of objects that can be of any type
li = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [1,2,'a',True]

#List slicing

amazon_cart=[
    'notebook',
    'sunglasses',
    'toys',
    'grapes'
    ]
amazon_cart[0] = 'laptop'
new_cart = amazon_cart #assign what is in memory from amazon to new
new_cart = amazon_cart[:] #copy the original amazon to new list
newcart1 = amazon_cart.copy() #copy the original amazon to new list
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

#Matrix

matrix = [
    [1,2,3],
    [2,4,6],
    [7,8,9]
    ]
print(matrix[0][1])


#list unpacking

a,b,c, *e, d=[1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(e)
print(d)



# List Methods
basket = ['a','x','b','c','m','d','e']

#adding
basket.append(100) #adds the value at the end
print(basket)

basket.insert(4,100) #insert object in place of the index
print(basket)

basket.extend([100,101])
print(basket)

#removing
basket.pop() #removes whatever at the index indicated - empty remove last value
print(basket)

basket.remove(4) #removes the value user enter
print(basket)

basket.clear() #removes eveything in the list
print(basket)


print(basket.index('d', 0, 4)) #returns the index of the entered object

print('i' in 'my name is moises')

basket.sort() # sort in ascending order on the original list
print(basket)

print(sorted(basket)) # function - produce a new list

basket.sort()
basket.reverse()
print(basket[::-1]) # list slicing - new list
print(basket) # original list

print(list(range(100))) # produces a list of 100 numbers

sentence='! '
new=sentence.join(['hi','my','name','is','jojo'])
print(new)