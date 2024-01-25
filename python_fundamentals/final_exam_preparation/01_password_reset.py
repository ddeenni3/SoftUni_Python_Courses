def takeodd(some_letters):
    new_letters = some_letters[1::2]
    return new_letters


def cut(some_letters, some_index, some_length):
    some_letters = some_letters[:some_index] + some_letters[some_index + some_length:]
    return some_letters


def substitute(some_letters, some_old_string, some_new_string):
    some_letters = some_letters.replace(some_old_string, some_new_string)
    return some_letters


letters = input()

while True:
    command = input().split()
    if command[0] == 'Done':
        break
    elif command[0] == 'TakeOdd':
        letters = takeodd(letters)
        print(letters)
    elif command[0] == 'Cut':
        index, length = int(command[1]), int(command[2])
        letters = cut(letters, index, length)
        print(letters)
    elif command[0] == 'Substitute':
        substring, new_string = command[1], command[2]
        if substring in letters:
            letters = substitute(letters, substring, new_string)
            print(letters)
        else:
            print('Nothing to replace!')

print(f'Your password is: {letters}')
