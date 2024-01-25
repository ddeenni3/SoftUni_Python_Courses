import re
pattern = r'((www)\.([A-Za-z0-9\-]+)(\.[a-z]+)+)'

sentence = input()

while sentence:
    match = re.search(pattern, sentence)
    if match:
        print(match[0])
    sentence = input()