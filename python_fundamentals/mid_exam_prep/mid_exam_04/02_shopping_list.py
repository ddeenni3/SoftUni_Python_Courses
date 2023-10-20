def urgent(some_list: list, some_item: str):
    if some_item not in some_list:
        some_list.insert(0, some_item)
    return some_list


def unnecessary(some_list: list, some_item: str):
    if some_item in some_list:
        some_list.remove(some_item)
    return some_list


def correct(some_list: list, some_old_item: str, some_new_item: str):
    if some_old_item in some_list:
        item_index = some_list.index(some_old_item)
        some_list[item_index] = some_new_item
    return some_list


def rearrange(some_list: list, some_item: str):
    if some_item in some_list:
        item_index = some_list.index(some_item)
        popped_item = some_list.pop(item_index)
        some_list.append(popped_item)
    return some_list


groceries = input().split('!')

while True:
    command = input()
    if command == 'Go Shopping!':
        break
    current_command = command.split()
    if current_command[0] == 'Urgent':
        item = current_command[1]
        urgent(groceries, item)
    elif current_command[0] == 'Unnecessary':
        item = current_command[1]
        unnecessary(groceries, item)
    elif current_command[0] == 'Correct':
        old_item = current_command[1]
        new_item = current_command[2]
        correct(groceries, old_item, new_item)
    elif current_command[0] == 'Rearrange':
        item = current_command[1]
        rearrange(groceries, item)

print(', '.join(groceries))
