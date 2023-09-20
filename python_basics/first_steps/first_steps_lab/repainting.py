plastic_square_m = 1.50
paint = 14.50
diluter = 5.00

plastic_needed = int(input())
paint_needed = int(input())
diluter_needed = int(input())
labour_hours = int(input())

total_plastic = (plastic_needed + 2) * plastic_square_m

total_paint = (paint_needed * 1.10) * paint

total_diluter = diluter_needed * diluter

total_sum_materials = total_paint + total_plastic + total_diluter + 0.4

labour_sum = labour_hours * (total_sum_materials * 0.30)

total_sum = labour_sum + total_sum_materials

print(total_sum)




