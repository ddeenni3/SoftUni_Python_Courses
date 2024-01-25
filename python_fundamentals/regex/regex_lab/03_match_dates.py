import re

text = input()

pattern = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'

result = re.findall(pattern, text)

for match in result:
    date = match[0]
    month = match[2]
    year = match[3]
    print(f'Day: {date}, Month: {month}, Year: {year}')
