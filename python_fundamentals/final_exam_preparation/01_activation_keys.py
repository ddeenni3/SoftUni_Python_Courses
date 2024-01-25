raw_activation_key = input()

while True:
    command = input().split('>>>')
    if command[0] == 'Generate':
        break
    elif command[0] == 'Contains':
        substring = command[1]
        if substring in raw_activation_key:
            print(f'{raw_activation_key} contains {substring}')
        else:
            print('Substring not found!')
    elif command[0] == 'Flip':
        start_index, end_index = int(command[2]), int(command[3])
        if command[1] == 'Upper':
            raw_activation_key = raw_activation_key[:start_index]\
                                 + raw_activation_key[start_index:end_index].upper() \
                                 + raw_activation_key[end_index:]

        elif command[1] == 'Lower':
            raw_activation_key = raw_activation_key[:start_index] \
                                 + raw_activation_key[start_index:end_index].lower() \
                                 + raw_activation_key[end_index:]
        print(raw_activation_key)
    elif command[0] == 'Slice':
        start_index, end_index = int(command[1]), int(command[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)

print(f'Your activation key is: {raw_activation_key}')
