alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']


def cypher(message_to_cypher: str, cypher_letters: list, shift_range: int, action: str):
    message_to_cypher = [x for x in message_to_cypher]
    if action == 'decode':
        shift_range *= -1
    for current_index, current_letter in enumerate(message_to_cypher):
        if current_letter in cypher_letters:
            index = (cypher_letters.index(current_letter) + shift_range) % len(cypher_letters)
            message_to_cypher[current_index] = cypher_letters[index]
    return ''.join(message_to_cypher)


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print(cypher(text, alphabet, shift, direction))
    restart_program = input('Would you like to encode/decode another message? Y/N:\n').lower()
    if restart_program == 'n':
        break
