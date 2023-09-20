total_food_kg = int(input())
total_food_gr = total_food_kg * 1000

while True:
    command = input()
    if command == 'Adopted':
        break
    eat_per_day = int(command)
    total_food_gr -= eat_per_day

if total_food_gr >= 0:
    print(f'Food is enough! Leftovers: {total_food_gr} grams.')
else:
    print(f'Food is not enough. You need {abs(total_food_gr)} grams more.')
