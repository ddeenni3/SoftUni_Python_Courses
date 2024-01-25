text = input()

explosion_strength = 0

output = ''

for index in range(len(text)):
    #  we have explosion
    if explosion_strength > 0 and text[index] != '>':
        explosion_strength -= 1
    # we have explosion mark
    elif text[index] == '>':
        output += text[index]
        explosion_strength += int(text[index + 1])
    # no explosion / no mark
    else:
        output += text[index]

print(output)



