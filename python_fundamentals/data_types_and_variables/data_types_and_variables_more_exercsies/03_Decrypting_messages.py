key = int(input())
characters = int(input())

for ch in range(characters):
    character = input()
    print_char = ord(character) + key
    print(chr(print_char), end='')
