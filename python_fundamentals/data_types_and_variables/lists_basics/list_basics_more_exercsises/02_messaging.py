numbers = input().split(' ')
string = input()
allowed_elements = list(string)

for number in numbers:
    index = 0
    for element in number:
        index += int(element)
    if index < len(allowed_elements):
        print(allowed_elements.pop(index), end='')
    else:
        index -= len(allowed_elements)
        print(allowed_elements.pop(index), end='')


