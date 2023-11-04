text = list(input())
text = [x for x in text if x != ' ']

letters = {}

for letter in text:
    if letter not in letters.keys():
        letters[letter] = 0
    letters[letter] += 1


for letter, occurrence in letters.items():
    print(f'{letter} -> {occurrence}')
