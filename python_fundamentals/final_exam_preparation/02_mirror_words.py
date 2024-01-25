import re

pattern = r'([@#])([A-Za-z]{3,})(\1)(\1)([A-Za-z]{3,})(\1)'

text = input()

matches = re.findall(pattern, text)

mirror_words = []

for match in matches:
    reversed_word = match[1]
    reversed_word = reversed_word[::-1]
    if reversed_word == match[4]:
        mirror_words.append(f'{match[1]} <=> {match[4]}')


if not matches:
    print('No word pairs found!')
else:
    print(f'{len(matches)} word pairs found!')
if not mirror_words:
    print('No mirror words!')
else:
    print('The mirror words are:')
    print(', '.join(mirror_words))
