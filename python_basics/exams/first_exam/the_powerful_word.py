from math import *

word = input()

winner_points = 0
winner_word = None

while word != 'End of words':
    current_points = 0
    for i in range(len(word)):
        current_char = word[i]
        current_points += ord(current_char)

    if word[0] in ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'):
        current_points *= len(word)
    else:
        current_points /= len(word)
        current_points = ceil(current_points)
    if current_points > winner_points:
        winner_word = word
        winner_points = current_points

    word = input()
print(f'The most powerful word is {winner_word} - {winner_points}')
