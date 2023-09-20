house_height_x = float(input())
side_wall_length_y = float(input())
roof_height_triangle_h = float(input())

# 1 litre of red paint needed for 4.3 m2
# 1 litre of green paint needed for 3.4 m2

door = 1.2 * 2
window = 1.5 * 1.5

front_wall = house_height_x * house_height_x - door
back_wall = house_height_x * house_height_x
side_wall_left = house_height_x * side_wall_length_y - window
side_wall_right = house_height_x * side_wall_length_y - window

green_paint_total = (front_wall + back_wall + side_wall_left + side_wall_right) / 3.4

roof_front = (house_height_x * roof_height_triangle_h) / 2
roof_back = (house_height_x * roof_height_triangle_h) / 2
roof_side = house_height_x * side_wall_length_y
roof_side_2 = house_height_x * side_wall_length_y

total_red_paint = (roof_side + roof_side_2 + roof_back + roof_front) / 4.3

print(f'{green_paint_total:.2f}')
print(f'{total_red_paint:.2f}')
