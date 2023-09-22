number_of_messages = int(input())

for message in range(number_of_messages):
    msg = int(input())
    if msg == 88:
        print('Hello')
    elif msg == 86:
        print('How are you?')
    elif msg < 88:
        print('GREAT!')
    else:
        print('Bye.')
