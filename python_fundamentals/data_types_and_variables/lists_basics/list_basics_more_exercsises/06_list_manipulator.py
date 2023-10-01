list_as_string = input().split()
list_as_integers = [int(x) for x in list_as_string]


while True:
    command = input()
    if command == "end":
        break
    current_command = command.split(' ')
    action = current_command[0]
    if action == 'exchange':
        index = int(current_command[1])
        if 0 <= index <= len(list_as_integers):
            list_as_integers = list_as_integers[index + 1:] + list_as_integers[:index + 1]
        else:
            print('Invalid index')
    elif action == 'max' or action == 'min':
        max_num = 0
        min_num = 0
        if current_command[1] == 'even':
            evens_list = []
            for num in list_as_integers:
                if num % 2 == 0:
                    evens_list.append(num)
            if len(evens_list) > 0:
                reversed_list = list_as_integers[::-1]
                if action == 'max':
                    max_num = max(evens_list)
                    print(reversed_list.index(max_num))
                else:
                    min_num = min(evens_list)
                    print(reversed_list.index(min_num))
            else:
                print('No matches')
        elif current_command[1] == 'odd':
            odds_list = []
            for num1 in list_as_integers:
                if num1 % 2 != 0:
                    odds_list.append(num1)
            if len(odds_list) > 0:
                reversed_list = list_as_integers[::-1]
                if action == 'max':
                    max_num = max(odds_list)
                    reversed_list = list_as_integers[::-1]
                    print(reversed_list.index(max_num))
                else:
                    min_num = min(odds_list)
                    print(reversed_list.index(min_num))
            else:
                print('No matches')
    elif action == 'first' or action == 'last':
        count = int(current_command[1])
        if count > len(list_as_integers):
            print('Invalid count')
            continue
        if current_command[2] == 'even':
            evens_list = []
            for num in list_as_integers:
                if num % 2 == 0:
                    evens_list.append(num)
            if action == 'first':
                print(evens_list[:count])
            else:
                print(evens_list[len(evens_list) - count:])
        elif current_command[2] == 'odd':
            odds_list = []
            for num1 in list_as_integers:
                if num1 % 2 != 0:
                    odds_list.append(num1)
            if action == 'first':
                print(odds_list[:count])
            else:
                print(odds_list[len(odds_list) - count:])
print(list_as_integers)