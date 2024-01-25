concealed_message = input()

while True:
    command = input().split(':|:')
    if command[0] == 'Reveal':
        break
    elif command[0] == 'InsertSpace':
        index = int(command[1])
        concealed_message = concealed_message[:index] + ' ' + concealed_message[index:]
        print(concealed_message)
    elif command[0] == 'Reverse':
        substring = command[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, '', 1)
            concealed_message = concealed_message + substring[::-1]
            print(concealed_message)
        else:
            print('error')
    elif command[0] == 'ChangeAll':
        substring, replacement = command[1], command[2]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
            print(concealed_message)

print(f'You have a new text message: {concealed_message}')
