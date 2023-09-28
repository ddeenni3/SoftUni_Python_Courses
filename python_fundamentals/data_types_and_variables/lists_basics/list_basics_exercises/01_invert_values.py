string = input()

list_string = string.split(' ')

absolute_string = []

for element in list_string:
    if int(element) > 0:
        absolute_string.append(-abs(int(element)))
    else:
        absolute_string.append(abs(int(element)))

print(absolute_string)
