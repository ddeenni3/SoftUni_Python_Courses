number_of_snowballs = int(input())

snowball_print = ''
snowball_highest_value = 0

for snowball in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight // time) ** quality
    if value > snowball_highest_value:
        snowball_highest_value = value
        snowball_print = f'{weight} : {time} = {value} ({quality})'

print(snowball_print)



