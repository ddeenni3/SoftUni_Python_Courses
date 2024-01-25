import re

pattern = r'([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)'

text = input()

matches = re.findall(pattern, text)
digits = re.findall(r'\d', text)
digits = [int(x) for x in digits]
emoji_ratings = {}

cool_threshold = 1
for digit in digits:
    cool_threshold *= digit

cool_emojis = []

for match in matches:
    total_score = 0
    word = match[1]
    for char in word:
        if char.isalpha():
            total_score += ord(char)
    if total_score >= cool_threshold:
            cool_emojis.append(match)

print(f'Cool threshold: {cool_threshold}')
if len(matches) > 0:
    print(f'{len(matches)} emojis found in the text. The cool ones are:')
    for emoji in cool_emojis:
        print(''.join(emoji))
