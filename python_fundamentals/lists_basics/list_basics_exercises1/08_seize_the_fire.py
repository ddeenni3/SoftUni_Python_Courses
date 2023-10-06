fire_cells = input().split('#')
amount_of_water = int(input())

extinguished = []
effort = 0

for cell in fire_cells:
    current_cell = cell.split(' = ')
    fire_type = current_cell[0]
    fire_value = int(current_cell[1])
    is_extinguished = False
    if fire_type == 'High' and 81 <= fire_value <= 125:
        if amount_of_water - fire_value >= 0:
            is_extinguished = True
    elif fire_type == 'Medium' and 51 <= fire_value <= 80:
        if amount_of_water - fire_value >= 0:
            is_extinguished = True
    elif fire_type == 'Low' and 1 <= fire_value <= 50:
        if amount_of_water - fire_value >= 0:
            is_extinguished = True
    if is_extinguished:
        amount_of_water -= fire_value
        extinguished.append(fire_value)
        effort += fire_value * 0.25

print('Cells:')
for fire_value in extinguished:
    print(f' - {fire_value}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(extinguished)}')

