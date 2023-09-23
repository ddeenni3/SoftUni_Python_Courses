number_of_commands = int(input())

combined_list = []
opening_list = []
closing_list = []
last_added_element = ''
is_balanced = True


for string in range(number_of_commands):
    command = input()
    if command == '(':
        opening_list.append(command)
        combined_list.append(command)
        if last_added_element == command:
            is_balanced = False
            break
        last_added_element += command
    elif command == ')':
        closing_list.append(command)
        combined_list.append(command)
        if last_added_element == command:
            is_balanced = False
            break
        last_added_element += command


if combined_list[0] == '(' and len(opening_list) == len(closing_list):
    print('BALANCED')
else:
    print('UNBALANCED')





