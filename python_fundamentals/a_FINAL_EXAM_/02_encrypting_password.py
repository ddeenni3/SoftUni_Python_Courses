import re

pattern = r'^(.+)>([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]+)<(\1)'

number_of_attempts = int(input())

for attempt in range(number_of_attempts):
    password = input()
    matches = re.findall(pattern, password)
    if matches:
        for match in matches:
            group_one = match[1]
            group_two = match[2]
            group_three = match[3]
            group_four = match[4]
            password = group_one + group_two + group_three + group_four
            print(f'Password: {password}')
    else:
        print('Try another password!')
