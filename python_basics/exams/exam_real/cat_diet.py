fats_percentage = int(input())
protein_percentage = int(input())
carbs_percentage = int(input())
total_calories = int(input())
water_percentage = int(input())

fats_gr = (total_calories * (fats_percentage / 100)) / 9
protein_gr = (total_calories * (protein_percentage / 100)) / 4
carbs_gr = (total_calories * (carbs_percentage / 100)) / 4
total_gr = fats_gr + protein_gr + carbs_gr
calories_per_day = total_calories / total_gr
water = water_percentage / 100
calories_per_day *= 1 - water

print(f"{calories_per_day:.4f}")
