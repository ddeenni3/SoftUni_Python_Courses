import sys

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
        if 0 <= index < len(list_as_integers):
            list_as_integers = list_as_integers[index + 1:] + list_as_integers[:index + 1]
        else:
            print('Invalid index')

    elif action == 'max':
        list_evens = [num for num in list_as_integers if num % 2 == 0]
        list_odds = [num for num in list_as_integers if num % 2 != 0]
        max_num = -sys.maxsize
        max_num_index = -1
        even_odd = current_command[1]
        if even_odd == 'even':
            for num in list_evens:
                if num > max_num:
                    max_num = num
            for index in range(len(list_as_integers) - 1, - 1, - 1):
                if list_as_integers[index] == max_num:
                    max_num_index = index
                    break
            if max_num_index > -1:
                print(max_num_index)
            else:
                print('No matches')
        elif even_odd == 'odd':
            for num in list_odds:
                if num > max_num:
                    max_num = num
            for index in range(len(list_as_integers) - 1, - 1, - 1):
                if list_as_integers[index] == max_num:
                    max_num_index = index
                    break
            if max_num_index > -1:
                print(max_num_index)
            else:
                print('No matches')
    elif action == 'min':
        list_evens = [num for num in list_as_integers if num % 2 == 0]
        list_odds = [num for num in list_as_integers if num % 2 != 0]
        min_num = sys.maxsize
        min_num_index = -1
        even_odd = current_command[1]
        if even_odd == 'even':
            for num in list_evens:
                if num < min_num:
                    min_num = num
            for index in range(len(list_as_integers) - 1, - 1, - 1):
                if list_as_integers[index] == min_num:
                    min_num_index = index
                    break
            if min_num_index > -1:
                print(min_num_index)
            else:
                print('No matches')
        elif even_odd == 'odd':
            for num in list_odds:
                if num < min_num:
                    min_num = num
            for index in range(len(list_as_integers) - 1, - 1, - 1):
                if list_as_integers[index] == min_num:
                    min_num_index = index
                    break
            if min_num_index > -1:
                print(min_num_index)
            else:
                print('No matches')
    elif action == 'first':
        list_evens = [num for num in list_as_integers if num % 2 == 0]
        list_odds = [num for num in list_as_integers if num % 2 != 0]
        count = int(current_command[1])
        even_odd = current_command[2]
        if even_odd == 'even':
            if count > len(list_as_integers):
                print('Invalid count')
            else:
                print(list_evens[:count])
        elif even_odd == 'odd':
            if count > len(list_as_integers):
                print('Invalid count')
            else:
                print(list_odds[:count])
    elif action == 'last':
        list_evens = [num for num in list_as_integers if num % 2 == 0]
        list_odds = [num for num in list_as_integers if num % 2 != 0]
        count = int(current_command[1])
        even_odd = current_command[2]
        if even_odd == 'even':
            if count > len(list_as_integers):
                print('Invalid count')
            else:
                if count > len(list_evens):
                    print(list_evens)
                else:
                    print(list_evens[len(list_evens) - count:])

        elif even_odd == 'odd':
            if count > len(list_as_integers):
                print('Invalid count')
            else:
                if count > len(list_odds):
                    print(list_odds)
                else:
                    print(list_odds[len(list_odds) - count:])

print(list_as_integers)
