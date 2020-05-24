#Sets
fset = {1,2,3,4,5,5}
fset.add(100)
fset.add(2)
print(fset) #Return unique values

my_list = [1,2,3,4,5,5]
print(set(my_list)) #function to convert list to sets

print(1 in fset)
print(len(fset))

#Sets methods - Sets are very useful when having more than 1 set to compare than each other

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set))
my_set.discard(5) # Modifies set
print(my_set)
my_set.difference_update(your_set) # Modifies set
print(my_set)
print(my_set.intersection(your_set)) # my_set & your_set
print(my_set.isdisjoint(your_set))
print(my_set.union(your_set)) # my_set | your_set
print(my_set.issubset(your_set)) # is my_set inside your_set? true or false
print(my_set.issuperset(your_set)) # my_set contains eeverything of your-set? true or false


