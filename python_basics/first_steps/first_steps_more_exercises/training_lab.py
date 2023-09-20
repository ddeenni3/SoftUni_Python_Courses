width = float(input())
height = float(input())

width_cm = width * 100
height_cm = height * 100

height_cm -= 100

desks_per_line = height_cm // 70

lines_in_room = width_cm // 120

total_working_places = (desks_per_line * lines_in_room) - 3

print(int(total_working_places))
