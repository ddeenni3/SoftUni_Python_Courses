alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']


shift = 5

message_to_do = 'e'

current_action = 'decode'


def cypher(message_to_cypher: str, cypher_letters: list, shift_range: int, action: str):
    message_to_cypher = [x for x in message_to_cypher]
    if action == 'encode':
        for current_letter_index in range(len(message_to_cypher)):
            if message_to_cypher[current_letter_index] in cypher_letters:
                index = cypher_letters.index(message_to_cypher[current_letter_index])
                if index + shift_range > len(cypher_letters):
                    index = (index + shift_range) % len(cypher_letters)
                    message_to_cypher[current_letter_index] = cypher_letters[index]
                else:
                    message_to_cypher[current_letter_index] = cypher_letters[index + shift_range]
    elif action == 'decode':
        for current_letter_index in range(len(message_to_cypher)):
            if message_to_cypher[current_letter_index] in cypher_letters:
                index = cypher_letters.index(message_to_cypher[current_letter_index])
                message_to_cypher[current_letter_index] = cypher_letters[index - shift_range]

    return ''.join(message_to_cypher)


print(cypher(message_to_do, alphabet, shift, current_action))