kgs_of_food = float(input())
kgs_of_hay = float(input())
kgs_of_cover = float(input())
pig_weight_kgs = float(input())

grams_of_food = kgs_of_food * 1000
grams_of_hay = kgs_of_hay * 1000
grams_of_cover = kgs_of_cover * 1000
pig_weight_grams = pig_weight_kgs * 1000

groceries_are_enough = True


for day in range(1, 31):
    if grams_of_food - 300 > 0:
        grams_of_food -= 300
    else:
        groceries_are_enough = False
        break
    if day % 2 == 0:
        if grams_of_hay - grams_of_food * 0.05 > 0:
            grams_of_hay -= grams_of_food * 0.05
        else:
            groceries_are_enough = False
            break
    if day % 3 == 0:
        if grams_of_cover - pig_weight_grams / 3 > 0:
            grams_of_cover -= pig_weight_grams / 3
        else:
            groceries_are_enough = False
            break

if groceries_are_enough:
    print(f'Everything is fine! Puppy is happy!'
          f' Food: {grams_of_food / 1000:.2f},'
          f' Hay: {grams_of_hay / 1000:.2f},'
          f' Cover: {grams_of_cover / 1000:.2f}.')
else:
    print('Merry must go to the pet store!')
    