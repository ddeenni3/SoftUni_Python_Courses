secret_messages = input().split()

deciphered_message = ''

for message in secret_messages:
    current_word = list(message)
    deciphered_word = ''
    number = ''
    for char in current_word[::-1]:
        if char.isdigit():
            number += char
            current_word.remove(char)
    current_word[0], current_word[-1] = current_word[-1], current_word[0]
    deciphered_message += f'{chr(int(number[::-1]))}{"".join(current_word)} '
print(deciphered_message.strip())
