username = input()
password_DB = input()

password = input()

while password_DB != password:
    password = input()

print(f'Welcome {username}!')
