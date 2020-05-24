#Type Conversion
a=str(100)
b=int(a)
c=type(b)
print(c)

print(type(int(str(100))))

#Exercise

birth_year = input('what year were you born?')
print(type(birth_year))
age = 2020-int(birth_year)
print(f'Your age is {age}')
