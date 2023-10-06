def password_checker(password):
    length = True
    alphanum = True
    digits = True
    result = []
    digit_counter = 0
    if 6 > len(password) or len(password) > 10:
        result.append('Password must be between 6 and 10 characters')
        length = False
    if not password.isalnum():
        result.append('Password must consist only of letters and digits')
        alphanum = False
    for char in password:
        if char.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        result.append('Password must have at least 2 digits')
        digits = False

    if length and alphanum and digits:
        result.append('Password is valid')
    return result


user_password = input()
validation_list = password_checker(user_password)

print(*validation_list, sep='\n')

