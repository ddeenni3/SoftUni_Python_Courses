import re

string = input()
word = input()

pattern = fr'\b{word}\b'

match = re.findall(pattern, string, re.IGNORECASE)

print(len(match))
