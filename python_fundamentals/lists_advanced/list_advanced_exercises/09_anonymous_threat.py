def merge(some_list, start_index, end_index):
    if end_index > len(some_list) - 1:
        end_index = len(some_list) - 1
    if start_index < 0:
        start_index = 0
    merged = ''.join(some_list[start_index:end_index + 1])
    some_list[start_index:end_index + 1] = [merged]
    return some_list


def divide(some_element: str, number_of_partitions: int):
    divided_partition = []
    partitions_length = len(some_element) // number_of_partitions
    for partition in range(number_of_partitions):
        if partition != number_of_partitions - 1:
            divided_partition.append(some_element[partition * partitions_length:(partition + 1) * partitions_length])
        else:
            divided_partition.append(some_element[partition * partitions_length:])
    return divided_partition


commands = input().split()

while True:
    command = input().split()
    if command[0] == '3:1':
        break
    if command[0] == 'merge':
        starting_index = int(command[1])
        ending_index = int(command[2])
        commands = merge(commands, starting_index, ending_index)
    elif command[0] == 'divide':
        index = int(command[1])
        partitions = int(command[2])
        element = commands[index]
        commands[index:index + 1] = divide(element, partitions)

print(' '.join(commands))
