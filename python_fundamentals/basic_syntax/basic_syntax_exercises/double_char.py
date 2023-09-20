command = input()

while command != 'End':
    current_print = ''
    if command != 'SoftUni':
        for char in command:
            current_print += char * 2
        print(current_print)
    command = input()
