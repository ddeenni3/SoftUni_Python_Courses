def collect(some_list: list, some_item: str):
    if some_item not in some_list:
        some_list.append(some_item)
    return some_list


def drop(some_list: list, some_item: str):
    if some_item in some_list:
        some_list.remove(some_item)
    return some_list


def combine(some_list: list, some_old_item: str, some_new_item: str):
    if some_old_item in some_list:
        old_index = some_list.index(some_old_item)
        some_list.insert(old_index + 1, some_new_item)
    return some_list


def renew(some_list: list, some_item: str):
    if some_item in some_list:
        index = some_list.index(some_item)
        popped_element = some_list.pop(index)
        some_list.append(popped_element)


journal = input().split(', ')

while True:
    command = input().split(' - ')
    if command[0] == 'Craft!':
        break
    if command[0] == 'Collect':
        item = command[1]
        collect(journal, item)
    elif command[0] == 'Drop':
        item = command[1]
        drop(journal, item)
    elif command[0] == 'Combine Items':
        old_item = command[1].split(':')[0]
        new_item = command[1].split(':')[1]
        combine(journal, old_item, new_item)
    elif command[0] == 'Renew':
        item = command[1]
        renew(journal, item)

print(', '.join(journal))
