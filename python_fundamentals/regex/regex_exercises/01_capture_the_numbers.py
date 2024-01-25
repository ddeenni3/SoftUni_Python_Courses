import re

pattern = r'\d+'

command = input()

while command:
    match = re.findall(pattern, command)
    for num in match:
        print(num, end=' ')
    command = input()

