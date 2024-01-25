import re

text = input()

pattern = '\\b[A-Z][a-z]+ +[A-Z][a-z]+\\b'

result = re.findall(pattern, text)

for match in result:
    print(match, end=' ')
