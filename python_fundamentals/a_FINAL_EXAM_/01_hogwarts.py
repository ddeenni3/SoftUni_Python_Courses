spell_to_decipher = input()

while True:
    command = input().split()
    if command[0] == 'Abracadabra':
        break
    elif command[0] == 'Abjuration':
        spell_to_decipher = spell_to_decipher.upper()
        print(spell_to_decipher)
    elif command[0] == 'Necromancy':
        spell_to_decipher = spell_to_decipher.lower()
        print(spell_to_decipher)
    elif command[0] == 'Illusion':
        index, letter = int(command[1]), command[2]
        if index < len(spell_to_decipher):
            spell_to_decipher = spell_to_decipher[:index] + letter + spell_to_decipher[index+1:]
            print('Done!')
        else:
            print('The spell was too weak.')
    elif command[0] == 'Divination':
        first_substring, second_substring = command[1], command[2]
        if first_substring in spell_to_decipher:
            spell_to_decipher = spell_to_decipher.replace(first_substring, second_substring)
            print(spell_to_decipher)
    elif command[0] == 'Alteration':
        substring = command[1]
        if substring in spell_to_decipher:
            spell_to_decipher = spell_to_decipher.replace(substring, '')
            print(spell_to_decipher)
    else:
        print('The spell did not work!')
