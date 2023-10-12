word = input()

new_word = [char for char in word if char.lower() not in ['a', 'o', 'u', 'e', 'i']]

print(''.join(new_word))
