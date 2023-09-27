number_of_commands = int(input())

combined_list = []
last_added_element = ''
is_balanced = True


for string in range(number_of_commands):
    command = input()
    if command == '(':
        combined_list.append(command)
        if last_added_element == command:
            is_balanced = False
            break
        last_added_element += command
    elif command == ')':
        combined_list.append(command)
        if last_added_element == command:
            is_balanced = False
            break
        last_added_element += command


if combined_list[0] == '(' and combined_list.count('(') == combined_list.count(')'):
    print('BALANCED')
else:
    print('UNBALANCED')





