# Exercise!
# Display the image below to the right 
# hand side where the 0 is going to be ' ', 
# and the 1 is going to be '*'. This will 
# reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for row in picture:
    for pixel in row:
        if (pixel == 0):
            print(' ',end=' ')
        elif (pixel == 1):
            print('*',end=' ')
    print(' ') # need a new line after every row


# clean - code following styles and best practices. every line is readable
# readibility - read your own code, can you unsterdand it? is it easy to understand
# predictability - easy to understand and prectictable for other users
# dry - don't repeat yourself, make code reusable

for row in picture:
    for pixel in row:
        if pixel == 0:
            print(' ',end=' ')
        elif pixel:
            print('$',end=' ')
    print(' ') # need a new line after every row
