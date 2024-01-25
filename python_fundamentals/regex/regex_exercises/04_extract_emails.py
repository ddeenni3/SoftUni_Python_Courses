import re

pattern = r'\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)'

sentence = input()

match = re.findall(pattern, sentence)

for email in match:
    print(email[0])
