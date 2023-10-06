def chars_in_range(first, second):
    result = []
    for char in range(ord(first_character) + 1, ord(second_character)):
        result.append(chr(char))
    return result


first_character = input()
second_character = input()

print(' '.join(chars_in_range(first_character, second_character)))
