fire_levels = input().split('#')
available_water = int(input())

effort = 0
total_fire = 0

extinguished_fires = []

for fire in fire_levels:
    current_fire = fire.split(' = ')
    fire_type = current_fire[0]
    fire_value = int(current_fire[1])
    is_valid = False
    if fire_type == 'High' and 81 <= fire_value <= 125:
        is_valid = True
    elif fire_type == 'Medium' and 51 <= fire_value <= 80:
        is_valid = True
    elif fire_type == 'Low' and 1 <= fire_value <= 50:
        is_valid = True
    if available_water - fire_value >= 0 and is_valid:
        available_water -= fire_value
        total_fire += fire_value
        effort += fire_value * 0.25
        extinguished_fires.append(fire_value)

print('Cells:')
for element_index in range(len(extinguished_fires)):
    print(f'- {extinguished_fires[element_index]}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
