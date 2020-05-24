# Exercise: Check for duplicates in list:

some_list = ['a','b','c','b','m','n','n']

repeated = [] 
for i in range(len(some_list)): 
    k = i + 1
    for j in range(k, len(some_list)): 
        if some_list[i] == some_list[j] and some_list[i] not in repeated: 
            repeated.append(some_list[i]) 
print(repeated)
  

dup=[]
setof=set()
for item in some_list:
    if item in setof:
        dup.append(item)
    else:
        set.add(setof,item)
print(dup)            
        
        
dupli=[]
for value in some_list:
    if some_list.count(value)>1:
        if value not in dupli:
            dupli.append(value)
print(dupli)