def swap(elements: list, first_index: int, second_index: int):
    elements[first_index], elements[second_index] = elements[second_index], elements[first_index]
    return elements


def multiply(elements: list, first_index: int, second_index: int):
    elements[first_index] = elements[first_index] * elements[second_index]
    return elements


numbers = [int(x) for x in input().split()]

while True:
    command = input()
    if command == 'end':
        break
    current_command = command.split()
    if current_command[0] == 'decrease':
        numbers = [x - 1 for x in numbers]
    elif current_command[0] == 'swap':
        current_first_index = int(current_command[1])
        current_second_index = int(current_command[2])
        swap(numbers, current_first_index, current_second_index)
    elif current_command[0] == 'multiply':
        current_first_index = int(current_command[1])
        current_second_index = int(current_command[2])
        multiply(numbers, current_first_index, current_second_index)

print(', '.join(str(x) for x in numbers))
