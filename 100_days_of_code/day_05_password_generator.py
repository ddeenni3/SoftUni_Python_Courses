import random

password_length = int(input('Please enter the length of your desired password: '))

new_password = ''

for symbol in range(password_length):
    if symbol % 2 == 0:
        current_char = random.randrange(97, 123)
        new_password += chr(current_char)
    elif symbol % 3 == 0:
        current_char = random.randrange(0, 11)
        new_password += str(current_char)
    elif symbol % 5 == 0:
        current_char = random.randrange(33, 47)
        new_password += chr(current_char)
    elif symbol % 7 == 0:
        current_char = random.randrange(65, 91)
        new_password += chr(current_char)
    else:
        current_char = random.randrange(33, 123)
        new_password += chr(current_char)

print(f'Your new password is: {new_password}')


