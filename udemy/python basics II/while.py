# While

i=0
while i < 50: # Infinite Loop
    print(i)
    break # stop the loop and go to the next line

# stop the loop breaking the condition into False

i=0
while i<20:
    print(i)
    i += 1
else: # will only execute without a break in the while loop, only when the while condition turns into false
    print('done with all the work')


# for simple loops on iterable objects use for 

while True:
    response = input('say something: ')
    if (response == 'bye'):
        break

# While loops are useful for loops where the user doesn't know how many time it needs to iterate, the condition will decide it


