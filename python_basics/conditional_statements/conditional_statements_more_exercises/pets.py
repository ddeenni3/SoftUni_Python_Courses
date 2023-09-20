import math
days_absent = int(input())
food_in_kgs = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
tortoise_food_per_day = float(input())

total_dog_food = dog_food_per_day * days_absent
total_cat_food = cat_food_per_day * days_absent
total_tortoise_food = (tortoise_food_per_day * days_absent) / 1000

total_food_needed = total_dog_food + total_cat_food + total_tortoise_food
diff = abs(total_food_needed - food_in_kgs)

if total_food_needed <= food_in_kgs:
    print(f'{math.floor(diff)} kilos of food left.')
else:
    print(f'{math.ceil(diff)} more kilos of food are needed.')

