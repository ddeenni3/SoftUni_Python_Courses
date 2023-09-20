age = float(input())
sex = input()

user_output = ''

if age >= 16:
    if sex == 'm':
        user_output = 'Mr.'
    elif sex == 'f':
        user_output = 'Ms.'
elif age <= 16:
    if sex == 'm':
        user_output = 'Master'
    elif sex == 'f':
        user_output = 'Miss'

print(user_output)
