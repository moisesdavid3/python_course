#operator precedence
print((20 - 3) + 2 ** 3)

# 1. ()
# 2. **
# 3. * /
# 4. + -

# Guess the output of each answer before you click RUN
# Try to write down your answer before and see how you do... keep it mind I made it a little tricky for you :)

print((5 + 4) * 10 / 2) #45

print(((5 + 4) * 10) / 2) #45

print((5 + 4) * (10 / 2)) #45

print(5 + (4 * 10) / 2) #25

print(5 + 4 * 10 // 2) #25