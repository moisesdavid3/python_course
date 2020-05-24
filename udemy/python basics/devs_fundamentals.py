#password checker
username=input('Please add your username')
password=input('Please add your password')
secret='*' * len(password)
print(f'{username}, your password {secret} is {len(password)} long')

