import re

pattern = r'\b_([A-Za-z0-9]+)\b'

string = input()

match = re.findall(pattern, string)

print(','.join(match))
