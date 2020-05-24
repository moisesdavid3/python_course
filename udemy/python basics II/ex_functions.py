def highest_even(li):
    evens=[]
    for i in li:
        if i % 2 ==0:
            evens.append(i)
    return max(evens)

print(highest_even([14,7,10,20,1,24,2,3,4,8,13]))
