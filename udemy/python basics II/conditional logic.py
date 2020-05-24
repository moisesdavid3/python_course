# Conditional Logic

is_old = False
is_licenced = True

if is_old:
    print('you are enough to drive!')
elif is_licenced:
    print('you can drive now!')
else:
    print('you are not of age!')

print('ookooooko')


is_old = True
is_licenced = True

if is_old and is_licenced:
    print('you are enough to drive!')
else:
    print('you are not of age!')

# Truthy and Falsy

# Every value is Truthy
# Falsy is empty or just zero

# Ternary Operator - shortcut to make code cleaner

# condition_if_true if condition else condition_if_false

is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)

# Short Circuiting

is_friend = False
is_user = False

if is_friend or is_user:
    print('best friends')

