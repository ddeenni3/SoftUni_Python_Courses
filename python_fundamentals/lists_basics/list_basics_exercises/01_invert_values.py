string = input()

list_string = string.split(' ')

absolute_string = []

for element in list_string:
    absolute_string.append(-int(element))

print(absolute_string)
